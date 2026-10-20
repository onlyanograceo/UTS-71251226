import streamlit as st
import random as rand

st.title("Rumah Berhantu 👻")
st.image("image.png", width=450)
xNilai = st.number_input("Masukan ukuran", 5, 10, step=1)
ghost = st.number_input("ghost", 0, xNilai // 2, step=1)

# Cara mengerjakan:
#   - Ganti setiap "..." dengan jawabanmu.
#   - Baris yang bertanda "(diberikan)" sudah benar, tidak perlu diubah.
#   - Kerjakan dari SOAL 1 sampai SOAL 6, lalu jalankan: streamlit run nama_file.py


# ============================================================
# SOAL 1: Inisialisasi state
# Streamlit menjalankan ulang script setiap tombol diklik, jadi data game
# disimpan di st.session_state dan hanya dibuat jika belum ada.
#
# Contoh untuk "started" sudah diberikan. Ikuti pola yang sama:
#   - "loc"    : posisi kucing berupa list [baris, kolom], awalnya [0, 0]
#   - "ghosts" : kumpulan nomor kotak hantu, awalnya set kosong -> set()
# ============================================================
if "started" not in st.session_state:        # (diberikan)
    st.session_state.started = False         # (diberikan)

if "loc" not in st.session_state:
    st.session_state.loc = ...              # TODO 1a

if "ghosts" not in st.session_state:
    st.session_state.ghosts = ...            # TODO 1b


# ============================================================
# SOAL 2: Gambar peta
# Setiap kotak ditulis sebagai teks, diakhiri tab (\t) supaya rapi:
#   kucing -> "[😿]\t"     hantu -> "[👻]\t"     kosong -> "[  ]\t"
#
# Petunjuk:
#   2a. Kucing ada di kotak (i, j) jika [i, j] == st.session_state.loc
#   2b. Hantu ada di kotak ini jika nomor in st.session_state.ghosts
#   2c. Selain itu, kotak kosong
# ============================================================
def write_map():
    rows = []
    for i in range(xNilai):
        row = ""
        for j in range(xNilai):
            nomor = i * xNilai + j           # (diberikan) nomor kotak
            if ...:                          # TODO 2a: ada kucing?
                row += "[😿]\t"              # (diberikan)
            elif ...:                        # TODO 2b: ada hantu?
                row += "[👻]\t"              # (diberikan)
            else:
                row += ...                   # TODO 2c: kotak kosong
        rows.append(row)                     # (diberikan)
    return "\n".join(rows)                   # (diberikan)


# ============================================================
# SOAL 3: Gerakkan kucing
# di = perubahan baris, dj = perubahan kolom.
# Kucing TIDAK boleh keluar dari peta.
# Nomor baris dan kolom yang valid adalah 0 sampai xNilai - 1.
#
# Petunjuk:
#   3a. Syarat di dalam peta: ni dan nj sama-sama >= 0 dan < xNilai.
#       Gabungkan dua syarat dengan kata "and".
#   3b. Jika syarat terpenuhi, simpan posisi baru: [ni, nj]
# ============================================================
def move(di, dj):
    i, j = st.session_state.loc              # (diberikan) posisi sekarang
    ni = i + di                              # (diberikan) baris baru
    nj = j + dj                              # (diberikan) kolom baru
    if ...:                                  # TODO 3a: posisi baru masih di dalam peta?
        st.session_state.loc = ...           # TODO 3b: pindahkan kucing


# ============================================================
# SOAL 4: Tombol start
# Saat diklik, lakukan 3 hal:
#   4a. started menjadi True
#   4b. kucing kembali ke posisi awal [0, 0]
#   4c. pilih `ghost` kotak acak untuk hantu
#
# Petunjuk 4c:
#   rand.sample(kotak, jumlah) mengambil `jumlah` angka acak tanpa duplikat
#   dari daftar `kotak`. Hasilnya list, jadi bungkus dengan set(...).
#   Daftar `kotak` sudah dimulai dari 1, jadi hantu tidak pernah
#   muncul di kotak awal kucing (nomor 0).
# ============================================================
if st.button("start"):
    st.session_state.started = True           # TODO 4a
    st.session_state.loc =                # TODO 4b
    kotak = list(range(1, xNilai ** 2))      # (diberikan)
    st.session_state.ghosts = ...            # TODO 4c


# ============================================================
# SOAL 5: Tampilan game
# 5a. Kondisinya: game sudah dimulai (lihat st.session_state.started).
# 5b. Isi args=(di, dj) untuk tiap tombol arah:
#       Up    -> baris berkurang 1, kolom tetap
#       Down  -> baris bertambah 1, kolom tetap
#       Left  -> baris tetap, kolom berkurang 1
#       Right -> baris tetap, kolom bertambah 1
# ============================================================
if tampilan game:                                      # TODO 5a
    c1, c2, c3 = st.columns(3)
    c2.button("Up", on_click=move, args=(baris berkuranng 1, kolom tetap))        # TODO 5b

    c1, c2, c3 = st.columns(3)
    c1.button("Left", on_click=move, args=(baris tetap, kolom berkurang 1))      # TODO 5b
    c3.button("Right", on_click=move, args=(..., ...))     # TODO 5b

    c1, c2, c3 = st.columns(3)
    c2.button("Down", on_click=move, args=(..., ...))      # TODO 5b

    st.text(write_map())                     # (diberikan)

    # ========================================================
    # SOAL 6: Tampilkan st.error("Kena hantu! 👻")
    # jika kucing berada di kotak hantu.
    #
    # Petunjuk: nomor kotak kucing sudah dihitung di bawah.
    # Cek apakah nomor itu ada di st.session_state.ghosts.
    # ========================================================
    nomor_kucing = st.session_state.loc[0] * xNilai + st.session_state.loc[1]   # (diberikan)
    if st error:                                  # TODO 6a
        st.error("Kena hantu! 👻")           # (diberikan)