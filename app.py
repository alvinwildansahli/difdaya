import streamlit as st
import pandas as pd
import base64
from datetime import datetime

# ====================================================================================================
# 1. KONFIGURASI HALAMAN & BRANDING UTAMA
# [BAGIAN INI MENJELASKAN: Pengaturan dasar browser, judul tab, ikon, dan inisialisasi branding]
# ====================================================================================================
st.set_page_config(
    page_title="DIFDAYA - Difabel Muda Berdaya | Official Partnership Dashboard", # Ganti judul tab di sini
    page_icon="♿", # Ganti ikon tab di sini
    layout="wide", # Layout: "wide" (lebar penuh) atau "centered" (terpusat)
    initial_sidebar_state="collapsed"
)

# [BAGIAN INI MENJELASKAN: Fungsi untuk memproses file logo komunitas Anda agar muncul di web]
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# Silakan simpan logo Anda dengan nama 'logo_difdaya.png' di folder yang sama dengan file ini
logo_base64 = get_base64_of_bin_file('ipb.png') 

# ====================================================================================================
# 2. SISTEM NAVIGASI & STATE MANAGEMENT
# [BAGIAN INI MENJELASKAN: Logika teknis perpindahan halaman tanpa memuat ulang browser secara penuh]
# ====================================================================================================
if 'page' not in st.session_state:
    st.session_state.page = "Beranda" # Halaman default saat pertama kali diakses

if 'selected_pilar' not in st.session_state:
    st.session_state.selected_pilar = None

def navigate_to(page_name):
    st.session_state.page = page_name
    # Reset sub-halaman jika pindah ke menu utama
    if page_name != "Detail":
        st.session_state.selected_pilar = None
    st.rerun()

# ====================================================================================================
# 3. CSS KUSTOM ELIT (MODERN, STYLISH & PROFESIONAL)
# [BAGIAN INI MENJELASKAN: Pusat kendali visual. Anda bisa ubah Warna, Font, dan Ukuran di sini]
# ====================================================================================================
st.markdown("""
<style>
    /* ================================================================= */
    /* [IMPORT FONT]: Menggunakan Plus Jakarta Sans (Modern) & Outfit (Stylish Bold) */
    /* ================================================================= */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;700;800;900&display=swap');

    /* ================================================================= */
    /* [GLOBAL BACKGROUND LAYER]: Dasar halaman agar tidak terlihat kosong */
    /* ================================================================= */
    html, body, [class*="css"], .main {
        font-family: 'Plus Jakarta Sans', sans-serif; /* Mengatur font utama seluruh web */
        color: #0f172a; /* Warna teks gelap global */
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%) !important; /* Mengubah latar belakang dasar di balik semua kotak */
    }

    /* Efek pendaran cahaya (glow) di latar belakang saat scroll */
    body::before {
        content: "";
        position: fixed;
        top: -200px;
        left: -200px;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(96,165,250,0.15), transparent 70%); /* Cahaya biru halus kiri atas */
        z-index: -1;
    }

    body::after {
        content: "";
        position: fixed;
        bottom: -200px;
        right: -200px;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(37,99,235,0.15), transparent 70%); /* Cahaya biru kanan bawah */
        z-index: -1;
    }

    h1, h2, h3, .hero-title, .nav-brand {
        font-family: 'Outfit', sans-serif; /* Font khusus untuk semua judul besar */
    }

    /* [CONTAINER]: Mengatur lebar desain agar proporsional di tengah */
    .block-container {
        padding-top: 1.5rem !important; /* Jarak antara menu atas dengan batas browser */
        padding-bottom: 0rem !important;
        max-width: 1450px !important; /* Lebar maksimal konten utama */
        margin: 0 auto;
    }

    /* ================================================================= */
    /* [NAVBAR WRAPPER]: Biar tombol menu atas tidak "mengambang kosong" */
    /* ================================================================= */
    div[data-testid="column"] {
    background: red */ rgba(255,255,255,0.4)*/;
    backdrop-filter: blur(12px);
    padding: 10px;
    border-radius: 20px;
    }

    /* TOMBOL NAVIGASI */
    div[data-testid="column"] button {
        background: linear-gradient(
            135deg,
            #3b82f6,
            #2563eb,
            #1d4ed8
        ) !important;

        color: white !important;
        border: none !important;

        font-weight: 800 !important;
        border-radius: 16px !important;

        padding: 0.8rem 1rem !important;
        font-size: 15px !important;

        transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) !important;

        width: 100% !important;

        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.25) !important;
        text-transform: uppercase !important;
    }

    /* HOVER EFFECT */
    div[data-testid="column"] button:hover {
        background: linear-gradient(
            135deg,
            #2563eb,
            #1d4ed8
        ) !important;

        transform: translateY(-4px) scale(1.04);
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.4) !important;
    }

    /* CLICK EFFECT */
    div[data-testid="column"] button:active {
        transform: scale(0.95);
        box-shadow: 0 5px 10px rgba(37, 99, 235, 0.2);
    }

    /* ================================================================= */
    /* [HERO SECTION & DEPTH]: Banner biru utama di halaman depan */
    /* ================================================================= */
    .hero-container {
        position: relative;
        background: 
            radial-gradient(circle at 0% 0%, rgba(255,255,255,0.15), transparent 40%),
            linear-gradient(135deg, #1e40af, #2563eb, #60a5fa); /* Mengubah warna gradasi banner utama */
        background-blend-mode: overlay; /* Membuat warna biru terlihat lebih dalam dan kaya */
        color: white; 
        padding: 140px 5% 180px 5%; 
        border-radius: 0 0 100px 100px; 
        text-align: center; 
        margin-bottom: 80px; 
        box-shadow: 0 25px 50px -12px rgba(37, 99, 235, 0.25); 
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Layer cahaya tambahan di tengah banner utama */
    .hero-bg-center {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.15), transparent 70%); /* Glow putih transparan tengah */
        transform: translate(-50%, -50%);
        filter: blur(60px);
        z-index: 1;
        pointer-events: none;
    }

    /* [TITLE HERO]: Mengubah tulisan 'Membangun Martabat, Menyongsong Masa Depan' */
    .hero-title {
        position: relative;
        z-index: 10;
        font-size: clamp(48px, 7vw, 88px) !important; /* Ukuran tulisan judul raksasa */
        font-weight: 900; 
        letter-spacing: -3px; 
        line-height: 1; 
        margin-bottom: 25px; 
        text-shadow: 0 10px 30px rgba(0,0,0,0.15); 
    }

    /* Tulisan 'Martabat' (Yang berwarna kuning) */
    .hero-title span {
        background: linear-gradient(to right, #fbbf24, #fcd34d); /* Mengubah gradasi warna kuning pada kata Martabat */
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
    }

    /* [HERO SUBTITLE]: Tulisan 'Platform akselerasi kemandirian pemuda disabilitas...' */
    .hero-subtitle {
        position: relative;
        z-index: 10;
        font-size: 22px; 
        max-width: 800px; 
        margin: 0 auto 50px auto; 
        line-height: 1.6; 
        font-weight: 300; 
        background: rgba(255,255,255,0.05); /* Memberi latar bayangan halus di balik teks deskripsi banner */
        padding: 15px 25px; 
        border-radius: 16px; 
        backdrop-filter: blur(8px); /* Efek blur di belakang deskripsi agar teks lebih "keluar" */
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* [HERO BUTTONS]: Mengubah tombol 'Eksplor Program' dan 'Lihat Kisah Sukses' */
    /* Container untuk tombol agar pas di Hero */
    .hero-btn-container {
        display: flex;
        gap: 20px;
        margin-top: -80px;
        margin-left: 10%;
        margin-bottom: 100px;
        position: relative;
        z-index: 100;
    }

    /* Styling Tombol Kustom */
    .custom-btn {
        padding: 15px 35px;
        border-radius: 50px; /* Lebih lonjong agar modern */
        font-weight: 800;
        text-align: center;
        text-decoration: none;
        color: white !important;
        transition: all 0.4s ease;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        cursor: pointer;
    }

    /* Tombol 1: Blue Gradient */
    .btn-primary {
        background: linear-gradient(135deg, #2563eb, #1e40af);
    }
    .btn-primary:hover {
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.4);
    }

    /* Tombol 2: Glassmorphism / Outline */
    .btn-secondary {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border: 2px solid white;
        color: white !important;
    }
    .btn-secondary:hover {
        background: white;
        color: #1e293b !important;
        transform: translateY(-3px);
    }
    
    /* Styling Utama Tombol Streamlit */
    div.stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white !important;
        border-radius: 15px;
        padding: 12px 24px;
        font-size: 18px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: none;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3); /* Bayangan lembut */
        transition: all 0.2s ease-in-out;
        position: relative;
        overflow: hidden;
    }

    /* Efek Hover (Saat kursor di atas tombol) */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.5);
        transform: translateY(-2px); /* Tombol sedikit naik */
        color: white !important;
    }

    /* Efek Klik (Timbul/Menekan ke dalam) */
    div.stButton > button:active {
        transform: translateY(2px); /* Efek menekan ke bawah */
        box-shadow: inset 0 4px 8px rgba(0, 0, 0, 0.2); /* Bayangan ke dalam */
    }

    /* Efek Fokus agar tidak ada garis hitam mengganggu */
    div.stButton > button:focus:not(:active) {
        border: none;
        color: white;
        outline: none;
    }

    /* ================================================================= */
    /* [SECTION WRAPPER]: Biar tiap bagian konten punya “layer” sendiri */
    /* ================================================================= */
    .section-wrapper {
        background: linear-gradient(180deg, #ffffff, #f1f5f9); /* Latar belakang bagian seperti 'Dampak Kolaborasi' */
        padding: 80px 40px; 
        border-radius: 60px; 
        margin-bottom: 80px; 
        border: 1px solid rgba(255,255,255,0.5);
        box-shadow: 0 20px 40px rgba(0,0,0,0.02);
    }

    /* SEARCH BAR */
    div[data-testid="stTextInput"] {
        padding: 10px 0;
    }
    div[data-testid="stTextInput"] input {
        border-radius: 25px !important;
        border: 2px solid #2563eb !important;
        padding: 0.5rem 1rem !important;
    }

    /* CARD DESIGN */
    .p-card {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        height: 450px; /* Tinggi seragam */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.3s ease;
    }
    
    .p-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.1);
    }

    .p-category {
        color: #2563eb;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .p-title {
        font-size: 20px;
        font-weight: 800;
        color: #1e293b;
        margin: 15px 0;
    }

    .p-price {
        font-size: 18px;
        font-weight: 600;
        color: #475569;
    }

    /* Tombol WA Custom */
    .wa-button {
        background-color: #25d366;
        color: white !important;
        padding: 10px 20px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 15px;
        transition: 0.3s;
    }
    .wa-button:hover {
        background-color: #128c7e;
        color: white !important;
    }

    /* Efek saat kotak produk atau pilar disentuh mouse */
    .p-card:hover {
        transform: translateY(-15px) scale(1.02); /* Kotak sedikit melompat dan membesar */
        border-color: #2563eb; /* Garis tepi kotak berubah jadi biru saat disentuh */
        box-shadow: 0 35px 70px -15px rgba(37, 99, 235, 0.15);
    }
            
    /* Mengubah tampilan form agar lebih modern */
    [data-testid="stForm"] {
        border: 1px solid #e2e8f0 !important;
        border-radius: 30px !important;
        padding: 40px !important;
        background-color: #ffffff !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05) !important;
    }
    
    /* Memastikan input field memiliki border-radius yang konsisten */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px !important;
    }
            
    /* ================================================================= */
    /* [FOOTER]: Area penutup paling bawah yang berisi teks DIFDAYA */
    /* ================================================================= */
    .footer-section {
        background: linear-gradient(180deg, #020617, #0f172a); /* Mengubah warna gelap area paling bawah */
        color: #94a3b8; 
        padding: 120px 10%; 
        border-radius: 100px 100px 0 0; 
        text-align: center; 
        border-top: 1px solid rgba(255,255,255,0.05);
    }

    /* ================================================================= */
    /* [RESPONSIVE]: Penyesuaian otomatis untuk layar HP */
    /* ================================================================= */
    @media (max-width: 768px) {
        div[data-testid="column"] {
            background: transparent; /* Hilangkan background menu di HP agar tidak berantakan */
            backdrop-filter: none;
            padding: 0;
        }
        .section-wrapper {
            padding: 40px 20px; /* Kurangi jarak dalam kotak di HP */
        }
        .hero-container {
            padding: 100px 5% 80px 5%;
        }
        .hero-title {
            font-size: 42px !important; /* Judul mengecil otomatis di HP */
            letter-spacing: -1.5px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ====================================================================================================
# 4. DATA REPOSITORY (PUSAT KONTEN KOMPREHENSIF)
# [BAGIAN INI MENJELASKAN: Seluruh isi teks web. Ubah kalimat di sini untuk kustomisasi konten]
# ====================================================================================================

# [DATABASE PILAR]: Isi deskripsi lengkap tiap pilar program pemberdayaan
PILAR_DATA = {
    'Mental Health': {
        'subtitle': 'Layanan konseling adaptif dan penguatan kepercayaan diri.',
        'icon': '🧠',
        'color': '#ec4899', # Identitas warna Pink
        'summary': 'Membangun fondasi psikologis difabel muda agar memiliki ketahanan mental yang kuat.',
        'full_desc': """
            Program ini adalah jantung dari DIFDAYA. Kami percaya bahwa kemandirian dimulai dari pikiran. 
            Melalui sesi konseling profesional dan peer-support group, kami membantu peserta mengenali potensi diri 
            dan mengatasi stigma internal yang menghambat pertumbuhan mereka.
        """,
        'modules': ['Self-Love & Acceptance', 'Manajemen Stigma', 'Public Speaking Dasar', 'Komunikasi Asertif'],
        'agenda': ['Sesi Konseling Individu (By Request)', 'Gathering Bulanan - 15 Januari 2026']
    },
    'Pendidikan': {
        'subtitle': 'Kurikulum inklusif digital dan akademik yang adaptif.',
        'icon': '📖',
        'color': '#3b82f6', # Identitas warna Biru
        'summary': 'Membuka akses literasi dan skill teknis bagi difabel untuk bersaing di era digital.',
        'full_desc': """
            DIFDAYA Academy menyediakan pendidikan non-formal berstandar industri. Kurikulum kami dimodifikasi 
            agar aksesibel bagi teman tuli, netra, maupun daksa, dengan fokus utama pada keahlian teknologi informasi.
        """,
        'modules': ['Literasi Digital', 'Coding Dasar for Blind', 'Desain Grafis Isyarat', 'Bahasa Inggris Bisnis'],
        'agenda': ['Pembukaan Batch 5 - Februari 2026', 'Webinar Beasiswa Luar Negeri']
    },
    'Ekonomi': {
        'subtitle': 'Pelatihan kemandirian finansial melalui pengembangan UMKM.',
        'icon': '📈',
        'color': '#10b981', # Identitas warna Hijau
        'summary': 'Menciptakan peluang kerja dan ekosistem bisnis inklusif bagi wirausaha muda difabel.',
        'full_desc': """
            Ekonomi mandiri adalah tujuan akhir kami. Kami bertindak sebagai inkubator bisnis yang 
            mendampingi anggota dari tahap ide produk, branding, hingga pemasaran digital dan distribusi pasar.
        """,
        'modules': ['Business Plan Dasar', 'Social Media Marketing', 'Manajemen Keuangan', 'Pengemasan Produk'],
        'agenda': ['Bazaar Produk Inklusi - April 2026', 'Workshop Marketplace']
    },
    'Religi': {
        'subtitle': 'Metode belajar Al-Quran khusus (Braille/Isyarat).',
        'icon': '🕌',
        'color': '#a855f7', # Identitas warna Ungu
        'summary': 'Memastikan hak akses spiritualitas terpenuhi melalui media adaptif yang inovatif.',
        'full_desc': """
            Sebagai bagian dari Yayasan Cahaya Quran, pilar religi berfokus pada penyediaan fasilitas belajar 
            agama yang ramah disabilitas, seperti Al-Quran Braille dan kajian dalam Bahasa Isyarat.
        """,
        'modules': ['Tahsin Isyarat', 'Sejarah Islam Inklusif', 'Fiqih Ibadah Difabel', 'Akhlak & Etika'],
        'agenda': ['Wisuda Hafidz Isyarat - Maret 2026', 'Ramadhan Camp Inklusi']
    },
    'Sosial': {
        'subtitle': 'Advokasi hak disabilitas dan inklusi sosial aktif.',
        'icon': '🤝',
        'color': '#f97316', # Identitas warna Oranye
        'summary': 'Membangun kesadaran publik dan jejaring relawan pendukung hak-hak disabilitas.',
        'full_desc': """
            Pilar sosial bergerak di luar komunitas. Kami melakukan audit aksesibilitas fasilitas publik 
            dan memberikan pelatihan kepada masyarakat umum tentang etika berinteraksi dengan difabel.
        """,
        'modules': ['Dasar-dasar Advokasi', 'Etika Interaksi Disabilitas', 'Campaign Management', 'Audit Aksesibilitas'],
        'agenda': ['Kampanye Hari Disabilitas', 'Volunteer Training Batch 3']
    }
}

# [DATABASE KATALOG]: Daftar produk yang dijual untuk mendukung operasional komunitas
KATALOG_DATA = [
    {'name': 'Kopi Bubuk Difdaya Blend', 'price': 'Rp 55.000', 'cat': 'F&B', 'icon': '☕'},
    {'name': 'Tas Anyaman Bambu Premium', 'price': 'Rp 145.000', 'cat': 'Fashion', 'icon': '👜'},
    {'name': 'Lukisan Kanvas Inklusif', 'price': 'Rp 750.000', 'cat': 'Seni', 'icon': '🎨'},
    {'name': 'Paket Buku Belajar Isyarat', 'price': 'Rp 95.000', 'cat': 'Edukasi', 'icon': '📖'},
    {'name': 'T-Shirt "Berdaya Tanpa Batas"', 'price': 'Rp 110.000', 'cat': 'Fashion', 'icon': '👕'},
    {'name': 'Madu Murni Bina Difabel', 'price': 'Rp 85.000', 'cat': 'Kesehatan', 'icon': '🍯'}
]

# [DATABASE BERITA]: Berita dan kegiatan terbaru
BERITA_DATA = [
    {'title': 'DIFDAYA Raih Penghargaan Impact Sosial 2025', 'date': '20 Des 2025', 'tag': 'Prestasi'},
    {'title': 'Kolaborasi Strategis dengan Perusahaan Teknologi', 'date': '15 Des 2025', 'tag': 'Kemitraan'},
    {'title': 'Peluncuran Al-Quran Isyarat Digital Pertama', 'date': '10 Des 2025', 'tag': 'Inovasi'}
]

# ====================================================================================================
# 5. RENDERER: HEADER & NAVIGATION
# [BAGIAN INI MENJELASKAN: Menampilkan logo, nama brand, dan susunan menu navigasi atas]
# ====================================================================================================
st.markdown("<br>", unsafe_allow_html=True)
c_h_logo, c_h_nav = st.columns([1.5, 3])

with c_h_logo:
    # Menampilkan Logo Komunitas Anda
    if logo_base64:
        st.markdown(f"""
            <div style='display: flex; align-items: center; gap: 15px; margin-left: 8%;'>
                <img src="data:image/png;base64,{logo_base64}" width="65" style="border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
                <div style='line-height: 1;'>
                    <h2 style='margin: 0; color: #0f172a; font-size: 28px; font-weight: 800; letter-spacing: -1.5px;'>DIFDAYA</h2>
                    <small style='color: #2563eb; font-weight: 800; text-transform: uppercase; font-size: 10px;'>Yayasan Cahaya Quran</small>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Tampilan Inisial Jika Logo Belum Ada
        st.markdown("""
            <div style='display: flex; align-items: center; gap: 15px; margin-left: 8%;'>
                <div style='background: #2563eb; color: white; width: 60px; height: 60px; border-radius: 18px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 30px; box-shadow: 0 10px 25px rgba(37,99,235,0.3);'>D</div>
                <div style='line-height: 1;'>
                    <h2 style='margin: 0; color: #0f172a; font-size: 28px; font-weight: 800; letter-spacing: -1.5px;'>DIFDAYA</h2>
                    <small style='color: #2563eb; font-weight: 800; text-transform: uppercase; font-size: 10px;'>Yayasan Cahaya Quran</small>
                </div>
            </div>
        """, unsafe_allow_html=True)

with c_h_nav:
    # Membuat 6 Tombol Navigasi yang Stylish
    n_cols = st.columns(6)
    pages = ["Beranda", "Tentang", "Program", "Berita", "Katalog", "Kontak"]
    for i, p_name in enumerate(pages):
        # Tombol navigasi fungsional dengan Bold dan Hover effect
        if n_cols[i].button(p_name, key=f"nav_top_{p_name}", use_container_width=True):
            navigate_to(p_name)

st.markdown("<hr style='margin: 10px 0; opacity: 0.05;'>", unsafe_allow_html=True)

# ====================================================================================================
# 6. PAGE RENDERING LOGIC
# [BAGIAN INI MENJELASKAN: Inti dari tampilan tiap halaman saat menu diklik]
# ====================================================================================================

# --- HALAMAN: BERANDA ---
if st.session_state.page == "Beranda":
    # HERO SECTION (BANNER UTAMA)
    st.markdown("""
        <div class="hero-container">
            <span style="background: rgba(255,255,255,0.15); padding: 8px 24px; border-radius: 50px; font-size: 13px; font-weight: 700; letter-spacing: 2px;">YAYASAN CAHAYA QURAN PRESENTS</span>
            <h1 class="hero-title">Membangun <span>Martabat,</span><br>Menyongsong Masa Depan.</h1>
            <p class="hero-subtitle">
                Platform strategis untuk akselerasi kemandirian pemuda disabilitas melalui sinergi 
                kesehatan mental, kapasitas intelektual, dan pemberdayaan ekonomi inklusif.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # TOMBOL INTERAKTIF DI DALAM HERO (Fungsional & Berwarna)
    st.markdown('<div class="hero-btn-container">', unsafe_allow_html=True)

    col1, col2, _ = st.columns([1.5, 1.8, 4])

    with col1:
        # Kita bungkus button streamlit agar ukurannya mengikuti CSS kita
        if st.button("Eksplor Program", key="hero_p_btn", use_container_width=True):
            st.session_state.page = "Program"
            st.rerun()

    with col2:
        if st.button("Lihat Kisah Sukses", key="hero_c_btn", use_container_width=True):
            st.session_state.page = "Berita"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # VISI STRATEGIS MITRA
    st.markdown("<h2 style='text-align: center; font-size: 48px; font-weight: 800; margin-bottom: 20px;'>Dampak Kolaborasi Kami</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 20px; max-width: 800px; margin: 0 auto 60px auto;'>DIFDAYA bekerja sama dengan puluhan institusi untuk menciptakan ekosistem di mana disabilitas bukan lagi penghalang profesionalitas.</p>", unsafe_allow_html=True)
    
    # Grid Statistik
    st_col1, st_col2, st_col3, st_col4 = st.columns(4)
    impact_stats = [("1.2k+", "Penerima Manfaat"), ("45+", "Mitra Strategis"), ("Rp 1.5M+", "Dana Terkelola"), ("15+", "Sertifikasi Profesi")]
    for i, (val, label) in enumerate(impact_stats):
        with [st_col1, st_col2, st_col3, st_col4][i]:
            st.markdown(f"""
                <div style='text-align: center;'>
                    <h1 style='color: #2563eb; font-size: 52px; margin-bottom: 0;'>{val}</h1>
                    <p style='color: #94a3b8; font-weight: 800; text-transform: uppercase; font-size: 13px;'>{label}</p>
                </div>
            """, unsafe_allow_html=True)

# --- HALAMAN: TENTANG KAMI ---
elif st.session_state.page == "Tentang":
    st.markdown("<div style='padding: 30px 10%;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 56px; font-weight: 900; text-align: center;'>Mewujudkan Indonesia Inklusif</h1>", unsafe_allow_html=True)
    
    # Struktur Konten Tentang Kami
    ta1, ta2 = st.columns([1.5, 1])
    with ta1:
        st.markdown("""
            ### Filosofi Kami
            DIFDAYA (Difabel Muda Berdaya) lahir dari keresahan atas minimnya akses pemuda disabilitas terhadap pendidikan dan lapangan kerja yang layak. 
            Kami menolak belas kasihan, kami menawarkan martabat melalui keahlian.
            
            ### Visi Strategis
            Menjadi platform inklusi nomor satu di Indonesia yang menjembatani potensi difabel dengan jaringan ekonomi global pada tahun 2030.
            
            ### Nilai-Nilai Inti
            1. **Inklusivitas Total**: Tidak ada disabilitas yang tertinggal.
            2. **Inovasi Adaptif**: Selalu mencari solusi teknologi terbaru.
            3. **Integritas Amanah**: Mengelola dukungan mitra dengan transparansi penuh.
        """)
    with ta2:
        # Simulasi Foto Komunitas (Placeholder)
        st.markdown("""
            <div style='background: #f1f5f9; height: 400px; border-radius: 40px; display: flex; align-items: center; justify-content: center; color: #94a3b8;'>
                
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- HALAMAN: PROGRAM (PILAR) ---
elif st.session_state.page == "Program":
    st.markdown("<div style='padding: 20px 8%;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 56px; font-weight: 900; text-align: center; margin-bottom: 60px;'>Pilar Pemberdayaan Kami</h1>", unsafe_allow_html=True)
    
    # Grid 3 Kolom untuk Pilar
    p_grid_cols = st.columns(3)
    pilar_names = list(PILAR_DATA.keys())
    
    for i, p_name in enumerate(pilar_names):
        with p_grid_cols[i % 3]:
            p_info = PILAR_DATA[p_name]
            st.markdown(f"""
                <div class="p-card">
                    <div style="font-size: 52px; margin-bottom: 25px;">{p_info['icon']}</div>
                    <h2 style="font-weight: 800; margin-bottom: 12px; color: #1e293b;">{p_name}</h2>
                    <p style="color: #64748b; font-size: 16px; line-height: 1.6; margin-bottom: 30px;">{p_info['summary']}</p>
                </div>
            """, unsafe_allow_html=True)
            # Tombol detail program fungsional
            if st.button(f"Lihat Detail {p_name} →", key=f"prog_btn_{i}", use_container_width=True):
                st.session_state.selected_pilar = p_name
                navigate_to("Detail")
            st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- HALAMAN: DETAIL PILAR (DEEP DIVE) ---
elif st.session_state.page == "Detail":
    sel_p_name = st.session_state.get('selected_pilar', 'Mental Health')
    sel_p_data = PILAR_DATA[sel_p_name]
    
    st.markdown("<div style='padding: 20px 10%;'>", unsafe_allow_html=True)
    if st.button("← Kembali ke Daftar Program", key="back_to_p_list"):
        navigate_to("Program")
    
    st.markdown(f"""
        <div style='margin-top: 40px;'>
            <h1 style='font-size: 72px; font-weight: 900; letter-spacing: -3px; color: #1e293b; margin-bottom: 10px;'>{sel_p_name}</h1>
            <p style='font-size: 26px; color: {sel_p_data['color']}; font-weight: 800;'>{sel_p_data['subtitle']}</p>
            <hr style='opacity: 0.1; margin: 40px 0;'>
        </div>
    """, unsafe_allow_html=True)
    
    dc1, dc2 = st.columns([2, 1])
    with dc1:
        st.markdown(f"### Strategi Program")
        st.write(sel_p_data['full_desc'])
        st.markdown("<br>### Kurikulum Utama", unsafe_allow_html=True)
        for mod in sel_p_data['modules']:
            st.info(f"**{mod}**")
    with dc2:
        st.markdown(f"""
            <div style='background: #f8fafc; padding: 40px; border-radius: 40px; border: 1px solid #e2e8f0;'>
                <h4 style='font-weight: 800; margin-bottom: 25px;'>📅 Agenda Terdekat</h4>
                {''.join([f'<div style="margin-bottom:15px; font-weight:700;">✅ {a}</div>' for a in sel_p_data['agenda']])}
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- HALAMAN: BERITA & KEGIATAN ---
elif st.session_state.page == "Berita":
    st.markdown("<div style='padding: 20px 10%;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 56px; font-weight: 900; text-align: center; margin-bottom: 60px;'>Warta & Kegiatan</h1>", unsafe_allow_html=True)
    
    for i, news in enumerate(BERITA_DATA):
        st.markdown(f"""
            <div style='background: white; padding: 40px; border-radius: 40px; border: 1px solid #e2e8f0; margin-bottom: 30px; display: flex; gap: 40px; align-items: center;'>
                <div style='background: #f1f5f9; width: 120px; height: 120px; border-radius: 30px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 40px;'>📰</div>
                <div>
                    <span style='background: #2563eb15; color: #2563eb; padding: 4px 12px; border-radius: 50px; font-size: 11px; font-weight: 800;'>{news['tag']}</span>
                    <h2 style='margin: 10px 0; font-weight: 800;'>{news['title']}</h2>
                    <p style='color: #94a3b8; font-weight: 600;'>Diterbitkan: {news['date']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"Baca Selengkapnya: {news['title']}", key=f"news_btn_{i}", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


# --- HALAMAN: KATALOG PRODUK ---

elif st.session_state.page == "Katalog":
    import urllib.parse

    # 1. Bagian Header & Search Bar
    st.markdown("<div style='padding: 20px 8% 20px 8%;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 48px; font-weight: 900; text-align: center; margin-bottom: 10px;'>Katalog Karya Difdaya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 18px; margin-bottom: 30px;'>Dukung kemandirian komunitas kami dengan membeli produk karya binaan DIFDAYA.</p>", unsafe_allow_html=True)
    
    # Input Pencarian
    search_query = st.text_input("", placeholder="Cari nama produk atau kategori...", key="search_katalog")
    st.markdown("</div>", unsafe_allow_html=True)

    # 2. Filter Data Berdasarkan Pencarian
    filtered_data = [
        prod for prod in KATALOG_DATA 
        if search_query.lower() in prod['name'].lower() or search_query.lower() in prod['cat'].lower()
    ]

    # 3. Grid Produk
    st.markdown("<div style='padding: 0 8% 80px 8%;'>", unsafe_allow_html=True)
    
    if not filtered_data:
        st.info(f"Produk dengan kata kunci '{search_query}' tidak ditemukan.")
    else:
        # Membuat baris (rows) secara otomatis
        cols = st.columns(3)
        for i, prod in enumerate(filtered_data):
            with cols[i % 3]:
                # Logika WhatsApp
                nomor_wa = "6281575431109"
                pesan_wa = f"Halo DIFDAYA, saya ingin memesan:\n\n*Produk:* {prod['name']}\n*Kategori:* {prod['cat']}\n*Harga:* {prod['price']}\n\nMohon informasi selanjutnya. Terima kasih!"
                encoded_msg = urllib.parse.quote(pesan_wa)
                wa_url = f"https://wa.me/{nomor_wa}?text={encoded_msg}"

                # Render Card (HTML)
                st.markdown(f"""
                    <div class="p-card">
                        <div style='font-size: 72px; margin-bottom: 20px;'>{prod['icon']}</div>
                        <span class="p-category">Kategori: {prod['cat']}</span>
                        <h3 class="p-title">{prod['name']}</h3>
                        <p class="p-price">{prod['price']}</p>
                        <a href="{wa_url}" target="_blank" class="wa-button" style="text-decoration: none; display: block; text-align: center;">
                            🛒 Pesan via WA
                        </a>
                    </div>
                """, unsafe_allow_html=True)
                
                # Spacer antar baris
                st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
                
    st.markdown("</div>", unsafe_allow_html=True)

# --- HALAMAN: KONTAK & KERJASAMA ---
elif st.session_state.page == "Kontak":
    import urllib.parse

    st.markdown("<div style='padding: 20px 10%;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 52px; font-weight: 900; text-align: center; margin-bottom: 20px;'>Mulai Jalin Kolaborasi</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 18px; margin-bottom: 60px;'>Mari bersama menciptakan ekosistem inklusif yang mandiri.</p>", unsafe_allow_html=True)
    
    con1, con2 = st.columns([1, 1.2], gap="large")
    
    with con1:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #eff6ff); padding: 30px; border-radius: 25px; border: 1px solid #e2e8f0;">
                <h3 style="color: #1e293b; margin-bottom: 20px;">Hubungi Kami</h3>
                <p style="color: #64748b;">Terbuka untuk kolaborasi strategis, donasi mitra, atau pendaftaran anggota baru.</p>
                <div style="margin-top: 25px;">
                    <p>📧 <b>Email:</b><br>alvinalvin@apps.ipb.ac.id</p>
                    <p>📱 <b>WhatsApp:</b><br>+62 815-7543-1109</p>
                    <p>📍 <b>Lokasi:</b><br>Yayasan Cahaya Quran, Jakarta Selatan.</p>
                    <p>📸 <b>Media Sosial:</b><br>@difdaya_official</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with con2:
        with st.form("professional_contact_form", clear_on_submit=False):
            st.markdown("<h4 style='margin-bottom: 20px;'>Formulir Kerjasama Mitra</h4>", unsafe_allow_html=True)
            f_name = st.text_input("Nama Lengkap / Instansi")
            f_email = st.text_input("Email Bisnis")
            f_subject = st.selectbox("Subjek Kolaborasi", ["Kemitraan Donasi", "Penyaluran Tenaga Kerja", "Inkubasi Bisnis", "Volunteer", "Lainnya"])
            f_msg = st.text_area("Rencana Kolaborasi / Pesan", height=120)
            
            # Tombol Submit (Menggunakan desain CSS tombol yang sudah kita buat sebelumnya)
            submit_btn = st.form_submit_button("Ajukan Kerjasama Sekarang", use_container_width=True)
            
            if submit_btn:
                if f_name and f_email and f_msg:
                    # Persiapan Data
                    my_email = "alvinalvin@apps.ipb.ac.id"
                    my_wa = "6281575431109"
                    
                    body_text = f"Halo Tim DIFDAYA,\n\nSaya {f_name} ({f_email}) ingin mengajukan kolaborasi.\n\nSubjek: {f_subject}\nRencana: {f_msg}"
                    
                    # 1. Link WhatsApp
                    wa_url = f"https://wa.me/{my_wa}?text={urllib.parse.quote(body_text)}"
                    
                    # 2. Link Email
                    email_url = f"mailto:{my_email}?subject={urllib.parse.quote('Kolaborasi: ' + f_subject)}&body={urllib.parse.quote(body_text)}"
                    
                    st.success("✅ Data telah disiapkan! Silahkan pilih jalur pengiriman di bawah:")
                    
                    # Menampilkan 2 tombol aksi setelah klik submit
                    btn_col1, btn_col2 = st.columns(2)
                    with btn_col1:
                        st.markdown(f'<a href="{wa_url}" target="_blank" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:12px; border-radius:15px; text-align:center; font-weight:bold;">Kirim via WhatsApp</div></a>', unsafe_allow_html=True)
                    with btn_col2:
                        st.markdown(f'<a href="{email_url}" target="_blank" style="text-decoration:none;"><div style="background-color:#ea4335; color:white; padding:12px; border-radius:15px; text-align:center; font-weight:bold;">Kirim via Email</div></a>', unsafe_allow_html=True)
                else:
                    st.error("Mohon lengkapi semua data formulir.")

    st.markdown("</div>", unsafe_allow_html=True)

# ====================================================================================================
# 7. FOOTER (EXTENDED & STYLISH)
# [BAGIAN INI MENJELASKAN: Bagian akhir website dengan informasi kontak, navigasi cepat, dan copyright]
# ====================================================================================================
st.markdown(f"""
    <div class="footer-section">
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 80px; margin-bottom: 80px;">
            <div>
                <h2 style="color: white; font-weight: 900; font-size: 38px; letter-spacing: -2px; margin-bottom: 25px;">DIFDAYA</h2>
                <p style="font-size: 16px; line-height: 1.8; opacity: 0.6; max-width: 400px;">
                    Inisiatif strategis Yayasan Cahaya Quran untuk memanusiakan martabat disabilitas melalui pemberdayaan 
                    mental, kapasitas intelektual, dan kemandirian ekonomi inklusif.
                </p>
            </div>
            <div>
                <h4 style="color: white; font-weight: 800; margin-bottom: 25px;">Navigasi Cepat</h4>
                <div style="display: grid; gap: 12px; opacity: 0.6;">
                    <span>Tentang Yayasan</span>
                    <span>Laporan Dampak Publik</span>
                    <span>Pusat Relawan</span>
                    <span>Syarat & Ketentuan</span>
                </div>
            </div>
            <div>
                <h4 style="color: white; font-weight: 800; margin-bottom: 25px;">Saluran Resmi</h4>
                <div style="display: grid; gap: 12px; opacity: 0.6;">
                    <span>Instagram</span>
                    <span>LinkedIn Professional</span>
                    <span>YouTube Channel</span>
                    <span>WhatsApp Partnership</span>
                </div>
            </div>
        </div>
        <hr style="opacity: 0.05; margin-bottom: 40px;">
        <div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; opacity: 0.4; font-weight: 600;">
            <span>© {datetime.now().year} DIFDAYA by Yayasan Cahaya Quran. All rights reserved.</span>
            <span>Built with Passion & Inclusivity</span>
        </div>
    </div>
""", unsafe_allow_html=True)