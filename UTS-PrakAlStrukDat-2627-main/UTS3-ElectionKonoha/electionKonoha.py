def validasi_dan_catat_suara(nama_pemilih: str, paslon_id: int, distrik: str, pemilu_data: dict, voters_set: set) -> tuple:
    # TODO:
    # 1. Validasi: nama pemilih tidak boleh kosong dan belum pernah memilih di voters_set (case-insensitive)
    # 2. Validasi: paslon_id dan distrik harus valid di pemilu_data
    # 3. Jika valid: tambahkan 1 suara ke distrik paslon terkait, daftarkan nama ke voters_set
    # Format Return: (status_sukses: bool, pesan_keterangan: str)

    # [Tulis logika validasi dan pencatatan suara di sini]

    return False, "Fungsi validasi belum diimplementasikan."


def hitung_agregasi_dan_konversi(pemilu_data: dict) -> list:
    # TODO:
    # 1. Hitung total perolehan suara tiap paslon dan persentasenya terhadap total suara nasional
    # 2. Konversikan struktur nested dict pemilu_data menjadi list of dictionary
    
    list_kandidat = []

    # [Lengkapi perulangan ekstraksi, agregasi suara, dan pembentukan dictionary kandidat di sini]
    # Format skema dictionary yang harus dimasukkan ke list_kandidat:
    # {
    #     "Nomor Urut": int,
    #     "Nama Capres": str,
    #     "Nama Cawapres": str,
    #     "Distrik Utara": int,
    #     "Distrik Pusat": int,
    #     "Distrik Selatan": int,
    #     "Total Suara": int,
    #     "Persentase": float
    # }

    return list_kandidat


def manual_sort(data_list: list, target_key: str) -> list:
    # TODO:
    # Urutkan elemen data_list secara DESCENDING (terbesar ke terkecil) berdasarkan target_key
    # ATURAN: Dilarang menggunakan fungsi bawaan sorted() atau method .sort()

    data_terurut = [dict(item) for item in data_list]

    # [Tulis algoritma sorting manual Anda di sini]

    return data_terurut
