import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()

def menu():
    tampilkan_tabel()
    print("""
===== Aplikasi CRUD sederhana =====
[1] Insert data
[2] Tampilkan data
[3] Update data
[4] Hapus data
[5] Cari Data
[0] Keluar
""")
    pilihan = (input("Pilih menu : "))
    if pilihan == "1":
        insert_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        cari_data()
    elif pilihan == "0":
        print("Terima kasih telah menggunakan aplikasi ini!")
        exit()
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        input("Tekan ENTER untuk kembali ke menu ")
        menu()
def buat_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS tugaskelompok3")
    db.commit()
    cursor.execute("USE tugaskelompok3")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        nama VARCHAR(255) NOT NULL,
        kota VARCHAR(255) NOT NULL
    )
    """)
    db.commit()
def tampilkan_tabel():
    cursor.execute("SELECT * FROM mahasiswa")
    result = cursor.fetchall()
    for data in result:
        print(f"({data[0]}, {data[1]}, {data[2]})")

def insert_data():
    print("Masukkan data mahasiswa")
    nama = input("Nama : ")
    kota = input("Kota : ")
    
    sql = "INSERT INTO mahasiswa(nama, kota) VALUES (%s, %s)"
    val = (nama, kota)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))
    input("Tekan ENTER untuk kembali ke menu ")
    menu()

def ubah_data():
    print("Masukkan id data mahasiswa yang ingin diubah")
    id = input("id : ")
    print("Masukkan data mahasiswa yang baru")
    nama = input("Nama : ")
    kota = input("Kota : ")
    
    sql = "UPDATE mahasiswa SET nama=%s, kota=%s WHERE id=%s"
    val = (nama, kota, id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))
    input("Tekan ENTER untuk kembali ke menu ")
    
    menu()

def hapus_data():
    print("Masukkan id data mahasiswa yang ingin dihapus")
    id = input("id : ")
    
    sql = "DELETE FROM mahasiswa WHERE id=%s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
    input("Tekan ENTER untuk kembali ke menu ")
    menu()

def tampilkan_data():
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
    input("Tekan ENTER untuk kembali ke menu ")
    
    menu()

def cari_data():
    print("Masukkan id data mahasiswa yang ingin dicari")
    id = input("id : ")
    
    sql = "SELECT * FROM mahasiswa WHERE id=%s"
    val = (id,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    if result:
        for data in result:
            print(data)
    else:
        print("Data tidak ditemukan")
    input("Tekan ENTER untuk kembali ke menu ")
    
    menu()



buat_database()
menu()