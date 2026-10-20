import streamlit as st
import copy
import os
from data import data_pemilu_konoha


from electionKonoha import validasi_dan_catat_suara, hitung_agregasi_dan_konversi, manual_sort


st.set_page_config(
    page_title="KONOHA PRESIDENTIAL ELECTION 2024",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.markdown("""
<style>
    /* Global Background & Typography */
    .stApp {
        background-color: #0B132B;
        color: #F8F9FA;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Broadcast Official Header */
    .broadcast-header {
        background-color: #1C2541;
        border-top: 3px solid #C5A059;
        border-bottom: 1px solid #2C3A5E;
        padding: 24px 20px;
        text-align: center;
        margin-bottom: 24px;
        border-radius: 4px;
    }

    .broadcast-tag {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #C5A059;
        margin-bottom: 6px;
    }

    .broadcast-title {
        color: #F8F9FA;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin: 4px 0 6px 0;
    }

    .broadcast-subtitle {
        color: #8D99AE;
        font-size: 0.88rem;
        letter-spacing: 1.2px;
        margin: 0;
        text-transform: uppercase;
    }

    /* Section Header */
    .section-header {
        font-size: 1.05rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #F8F9FA;
        border-left: 3px solid #C5A059;
        padding-left: 10px;
        margin: 22px 0 16px 0;
    }

    /* Large Candidate Master Card */
    .candidate-master-card {
        background-color: #111D38;
        border: 1.5px solid #1C2541;
        border-top: 4px solid #C5A059;
        border-radius: 6px;
        padding: 22px 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
    }

    .kandidat-badge {
        display: inline-block;
        background-color: transparent;
        color: #C5A059;
        border: 1px solid #C5A059;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        padding: 4px 12px;
        border-radius: 3px;
        margin-bottom: 16px;
        text-transform: uppercase;
    }

    .candidate-subcard {
        text-align: center;
        padding: 4px;
    }

    .candidate-role-tag {
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
        color: #C5A059;
        letter-spacing: 1.2px;
        margin-top: 10px;
        margin-bottom: 3px;
    }

    .candidate-main-title {
        font-size: 1.08rem;
        font-weight: 700;
        color: #F8F9FA;
        line-height: 1.35;
        min-height: 2.9em;
    }

    .stImage img {
        border-radius: 4px;
        border: 1px solid #2C3A5E;
    }

    /* Candidate District Tally Box */
    .candidate-tally-box {
        background-color: #0B132B;
        border: 1px solid #1C2541;
        border-radius: 4px;
        padding: 12px 14px;
        margin-top: 14px;
        font-size: 0.82rem;
    }

    .candidate-tally-row {
        display: flex;
        justify-content: space-between;
        margin-bottom: 4px;
        color: #8D99AE;
    }

    .candidate-tally-total {
        border-top: 1px solid #1C2541;
        padding-top: 6px;
        display: flex;
        justify-content: space-between;
        color: #C5A059;
        font-weight: 800;
    }

    /* Metric Summary Cards */
    .stat-card {
        background-color: #111D38;
        border: 1px solid #1C2541;
        border-radius: 4px;
        padding: 16px;
        text-align: center;
    }

    .stat-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #C5A059;
        letter-spacing: 1px;
    }

    .stat-label {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #8D99AE;
        margin-top: 4px;
    }

    /* Horizontal Progress Bar Visual Cards */
    .result-bar-card {
        background-color: #111D38;
        border: 1px solid #1C2541;
        border-radius: 4px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }

    .result-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 8px;
    }

    .result-kandidat-title {
        font-size: 1rem;
        font-weight: 700;
        color: #F8F9FA;
        letter-spacing: 0.5px;
    }

    .result-votes-count {
        font-size: 1rem;
        font-weight: 800;
        color: #C5A059;
    }

    .progress-track {
        background-color: #1C2541;
        border: 1px solid #2C3A5E;
        border-radius: 3px;
        height: 18px;
        width: 100%;
        overflow: hidden;
        margin-bottom: 10px;
    }

    .progress-fill {
        background: linear-gradient(90deg, #1E3A8A 0%, #2563EB 100%);
        height: 100%;
        border-radius: 2px;
        transition: width 0.5s ease;
    }

    .result-district-breakdown {
        display: flex;
        justify-content: space-between;
        font-size: 0.78rem;
        color: #8D99AE;
        border-top: 1px solid #1C2541;
        padding-top: 8px;
    }

    .result-district-breakdown b {
        color: #F8F9FA;
    }

    /* Form Submit Button */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #C5A059 !important;
        color: #0B132B !important;
        border: 1px solid #C5A059 !important;
        border-radius: 3px !important;
        font-weight: 700 !important;
        font-size: 0.88rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        width: 100% !important;
        padding: 10px 16px !important;
        transition: opacity 0.2s ease !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover {
        opacity: 0.88 !important;
    }

    /* Input & Select Controls */
    input, select, textarea {
        background-color: #0B132B !important;
        color: #F8F9FA !important;
        border: 1px solid #2C3A5E !important;
        border-radius: 3px !important;
    }
</style>
""", unsafe_allow_html=True)

if "pemilu" not in st.session_state:
    st.session_state["pemilu"] = copy.deepcopy(data_pemilu_konoha)

if "voters" not in st.session_state:
    st.session_state["voters"] = set()

st.markdown("""
<div class="broadcast-header">
    <span class="broadcast-tag">OFFICIAL ELECTION DESK - LIVE HEADQUARTERS</span>
    <h1 class="broadcast-title">KONOHA PRESIDENTIAL ELECTION 2024</h1>
    <p class="broadcast-subtitle">Sistem Rekapitulasi Suara dan E-Voting Nasional</p>
</div>
""", unsafe_allow_html=True)


total_suara_nasional = sum(
    sum(info["suara_distrik"].values())
    for info in st.session_state["pemilu"].values()
)
total_pemilih_terdaftar = len(st.session_state["voters"])

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{total_suara_nasional:,}</div>
        <div class="stat-label">TOTAL SUARA SAH MASUK</div>
    </div>
    """, unsafe_allow_html=True)

with col_m2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{total_pemilih_terdaftar}</div>
        <div class="stat-label">PEMILIH TERVERIFIKASI</div>
    </div>
    """, unsafe_allow_html=True)

with col_m3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">AKTIF</div>
        <div class="stat-label">STATUS SISTEM TABULASI</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.markdown('<div class="section-header">PASANGAN CALON PRESIDEN DAN WAKIL PRESIDEN</div>', unsafe_allow_html=True)

card_cols = st.columns(3)

for idx, (nomor_paslon, info) in enumerate(st.session_state["pemilu"].items()):
    with card_cols[idx]:
        st.markdown(f"""
        <div class="candidate-master-card">
            <div class="kandidat-badge">KANDIDAT {nomor_paslon:02d}</div>
        """, unsafe_allow_html=True)

        col_c1, col_c2 = st.columns(2)


        with col_c1:
            p_capres = os.path.join(BASE_DIR, info["foto"]["Ketua"])
            st.image(p_capres, use_container_width=True)
            st.markdown(f"""
            <div class="candidate-subcard">
                <div class="candidate-role-tag">CAPRES</div>
                <div class="candidate-main-title">{info["kandidat"]["Ketua"]}</div>
            </div>
            """, unsafe_allow_html=True)

        with col_c2:
            p_cawapres = os.path.join(BASE_DIR, info["foto"]["Wakil"])
            st.image(p_cawapres, use_container_width=True)
            st.markdown(f"""
            <div class="candidate-subcard">
                <div class="candidate-role-tag">CAWAPRES</div>
                <div class="candidate-main-title">{info["kandidat"]["Wakil"]}</div>
            </div>
            """, unsafe_allow_html=True)


        u = info["suara_distrik"]["Distrik Utara"]
        p = info["suara_distrik"]["Distrik Pusat"]
        s = info["suara_distrik"]["Distrik Selatan"]
        tot = u + p + s

        st.markdown(f"""
            <div class="candidate-tally-box">
                <div class="candidate-tally-row">
                    <span>Utara: <b style="color: #F8F9FA;">{u:,}</b></span>
                    <span>Pusat: <b style="color: #F8F9FA;">{p:,}</b></span>
                    <span>Selatan: <b style="color: #F8F9FA;">{s:,}</b></span>
                </div>
                <div class="candidate-tally-total">
                    <span>TOTAL:</span>
                    <span>{tot:,} SUARA</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.write("")


col_kiri, col_kanan = st.columns([1, 1.35])


with col_kiri:
    st.markdown('<div class="section-header">BILIK SUARA ELEKTRONIK</div>', unsafe_allow_html=True)

    with st.form(key="form_bilik_suara"):
        nama_pemilih = st.text_input("Nama Lengkap Pemilih")
        pilihan_paslon = st.selectbox(
            "Pilihan Pasangan Calon",
            options=[1, 2, 3],
            format_func=lambda x: f"KANDIDAT {x:02d} - {st.session_state['pemilu'][x]['kandidat']['Ketua']} & {st.session_state['pemilu'][x]['kandidat']['Wakil']}"
        )
        pilihan_distrik = st.selectbox(
            "Asal Distrik",
            options=["Distrik Utara", "Distrik Pusat", "Distrik Selatan"]
        )
        submit_vote = st.form_submit_button("SUBMIT SUARA")

        if "vote_pesan_sukses" in st.session_state:
            st.success(st.session_state.pop("vote_pesan_sukses"))

        if submit_vote:
            sukses, pesan = validasi_dan_catat_suara(
                nama_pemilih,
                pilihan_paslon,
                pilihan_distrik,
                st.session_state["pemilu"],
                st.session_state["voters"]
            )
            if sukses:
                st.session_state["vote_pesan_sukses"] = pesan
                st.rerun()
            else:
                if pesan:
                    st.error(pesan)


with col_kanan:
    st.markdown('<div class="section-header">PAPAN PEROLEHAN SUARA NASIONAL</div>', unsafe_allow_html=True)

    kriteria_urut = st.selectbox(
        "Urutkan Berdasarkan Kriteria",
        options=["Total Suara", "Distrik Utara", "Distrik Pusat", "Distrik Selatan"],
        index=0
    )

    data_kandidat_list = hitung_agregasi_dan_konversi(st.session_state["pemilu"])
    data_kandidat_sorted = manual_sort(data_kandidat_list, kriteria_urut)

    if data_kandidat_sorted and isinstance(data_kandidat_sorted, list):
        total_kriteria = sum(item.get(kriteria_urut, 0) for item in data_kandidat_sorted)

        for item in data_kandidat_sorted:
            nilai = item.get(kriteria_urut, 0)
            persen = (nilai / total_kriteria * 100) if total_kriteria > 0 else 0.0

            st.markdown(f"""
            <div class="result-bar-card">
                <div class="result-header">
                    <span class="result-kandidat-title">
                        KANDIDAT {item.get('Nomor Urut', 0):02d} — {item.get('Nama Capres', '-')} & {item.get('Nama Cawapres', '-')}
                    </span>
                    <span class="result-votes-count">{nilai:,} Suara ({persen:.2f}%)</span>
                </div>
                <div class="progress-track">
                    <div class="progress-fill" style="width: {min(max(persen, 0.0), 100.0):.2f}%;"></div>
                </div>
                <div class="result-district-breakdown">
                    <span>Utara: <b>{item.get('Distrik Utara', 0):,}</b></span>
                    <span>Pusat: <b>{item.get('Distrik Pusat', 0):,}</b></span>
                    <span>Selatan: <b>{item.get('Distrik Selatan', 0):,}</b></span>
                    <span>Total Akumulasi: <b style="color: #C5A059;">{item.get('Total Suara', 0):,}</b></span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background-color: #111D38; border: 1px solid #1C2541; border-radius: 4px; padding: 20px; text-align: center; color: #8D99AE; font-size: 0.9rem;">
            Data perolehan suara belum tersedia pada sistem tabulasi.
        </div>
        """, unsafe_allow_html=True)

st.write("")

with st.expander("AUDIT TRAIL DAFTAR PEMILIH TERDAFTAR"):
    if not st.session_state["voters"]:
        st.write("Belum ada data pemilih yang terverifikasi.")
    else:
        daftar_nama = sorted(list(st.session_state["voters"]))
        for nama in daftar_nama:
            st.write(f"- {nama} (Verified)")

    st.write("")
    if st.button("RESET SIMULASI"):
        st.session_state["pemilu"] = copy.deepcopy(data_pemilu_konoha)
        st.session_state["voters"] = set()
        st.rerun()
