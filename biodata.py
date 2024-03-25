def buat_biodata():
    print("===== Program Pembuat Biodata =====")
    nama = input("Masukkan nama Anda: ")
    umur = input("Masukkan umur Anda: ")
    alamat = input("Masukkan alamat Anda: ")
    jenis_kelamin = input("Masukkan jenis kelamin Anda: ")
    hobi = input("Masukkan hobi Anda: ")

    print("\n===== Biodata Anda =====")
    print("Nama:", nama)
    print("Umur:", umur)
    print("Alamat:", alamat)
    print("Jenis Kelamin:", jenis_kelamin)
    print("Hobi:", hobi)

if __name__ == "__main__":
    buat_biodata()
