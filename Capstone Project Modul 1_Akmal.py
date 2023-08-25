# Import modul pyinputplus untuk handle validasi input pengguna
import pyinputplus as pyip
from tabulate import tabulate

# Fungsi untuk menampilkan judul dengan garis pemisah
def title(text):
    print("="*50)
    print(text.center(50))
    print("="*50)

# Fungsi untuk mengatur pengurutan berdasarkan nim
def sort_key(student):
    return student["nim"]

# Fungsi untuk menampilkan data siswa
def read_student(student):
    print("=" * 50)
    print(f"NIM      : {student['nim']}")
    print(f"Nama     : {student['nama']}")
    print("-" * 50)
    print("| Mata Kuliah                    |    Nilai    |")
    print("|--------------------------------|-------------|")

    total_score = 0
    for matkul in student["Mata_kuliah"]:
        print(f"| {matkul['Mata_kuliah']:30} | {matkul['Score']:10}  |")
        total_score += matkul['Score']
        
    if len(student["Mata_kuliah"]) > 0:
        average_score = total_score / len(student["Mata_kuliah"])
        print("|--------------------------------|-------------|")
        print(f"| Rata-rata                      | {average_score:10.2f}  |")

        if average_score >= 80:
            print("| Keterangan                     |      Lulus  |")
        else:
            print("| Keterangan                     | Tidak Lulus |")
    
    print("=" * 50)

# Fungsi untuk membuat data siswa baru
def create_student(Daftar_student):
    nama = pyip.inputStr("Masukkan nama siswa: ").title()
    # Mengambil NIM berdasarkan entri terakhir dalam Daftar_student dan tambahkan 1
    last_nim = Daftar_student[-1]['nim'] if Daftar_student else 0
    nim = last_nim + 1
    print(f"NIM : {nim}")
    
    if Daftar_student:  # Pastikan Daftar_student tidak kosong
        available_courses = Daftar_student[0]["Mata_kuliah"]
    else:
        available_courses = []
    
    Mata_kuliah = []
    for matkul in available_courses:
        score = pyip.inputInt(f"Masukkan nilai untuk mata kuliah {matkul['Mata_kuliah']}: ",min=0, max=100)
        Mata_kuliah.append({"Mata_kuliah": matkul["Mata_kuliah"], "Score": score})
    
    return {"nama": nama, "nim": nim, "Mata_kuliah": Mata_kuliah}

# Fungsi untuk mengupdate data siswa
def update_student(student):
    while True:
        title("Edit Menu")
        print("1. Edit Nama")
        print("2. Edit Mata Kuliah dan Nilai")
        choice = pyip.inputInt("Pilih opsi: ")
        if choice == 1:
            new_nama = pyip.inputStr("Masukkan nama baru: ").title()
            student["nama"] = new_nama
            break
        elif choice == 2:
            for matkul in student["Mata_kuliah"]:
                new_score = pyip.inputInt(f"Masukkan nilai baru untuk mata kuliah {matkul['Mata_kuliah']}: ",min=0, max=100)
                matkul["Score"] = new_score
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih kembali")

# Fungsi untuk menghapus data siswa
def delete_student(student_list, deleted_students):
    nim_to_delete = input("Masukkan NIM atau nama siswa yang akan dihapus: ")
    for student in student_list:
        if str(student["nim"]) == nim_to_delete or nim_to_delete.lower() in student["nama"].lower():
            deleted_students.append(student)
            student_list.remove(student)
            print("Siswa telah dihapus sementara.")
            return
    print("NIM atau Nama siswa tidak ditemukan.")

# Fungsi untuk melihat data siswa yang telah dihapus
def view_deleted_students(deleted_students):
    if not deleted_students:
        print("Tidak ada data siswa yang dihapus.")
        return
     
    title("Deleted Students")
    for student in deleted_students:
        read_student(student)
        print("-" * 50)

# Fungsi untuk mengembalikan data siswa yang telah dihapus
def restore_deleted_student(student_list, deleted_students):
    if not deleted_students:
        print("Tidak ada siswa yang dapat dipulihkan.")
        return
    
    title("Restore Deleted Students") 
    print("Daftar Siswa yang Dapat Dipulihkan:")
    for i, student in enumerate(deleted_students, start=1):
        print(f"{i}. NIM: {student['nim']} - Nama: {student['nama']}")
    
    choice = pyip.inputInt("Pilih nomor siswa yang akan dipulihkan (0 untuk batal): ")
    if choice == 0:
        return
    
    if 1 <= choice <= len(deleted_students):
        student_to_restore = deleted_students.pop(choice - 1)
        student_list.append(student_to_restore)
        print("Siswa berhasil dipulihkan.")
    else:
        print("Pilihan tidak valid. Silahkan pilih kembali")

# Fungsi Utama
def main():
    # Dibawah ini merupakan contoh data siswa
    # Anda bisa menambahkan lebih banyak data siswa di sini
    Daftar_student = [
        {
            "nama": "Akmal Azaki",
            "nim": 152170001,
            "Mata_kuliah": [
                {"Mata_kuliah": "Fundamental Programming", "Score": 90},
                {"Mata_kuliah": "Data Analysis", "Score": 85},
                {"Mata_kuliah": "Machine Learning", "Score": 80}
            ]
        },
        {
            "nama": "Agung Setiabudi",
            "nim": 152170002,
            "Mata_kuliah": [
                {"Mata_kuliah": "Fundamental Programming", "Score": 80},
                {"Mata_kuliah": "Data Analysis", "Score": 85},
                {"Mata_kuliah": "Machine Learning", "Score": 80}
            ]
        },
        {
            "nama": "Andika Santoso",
            "nim": 152170003,
            "Mata_kuliah": [
                {"Mata_kuliah": "Fundamental Programming", "Score": 95},
                {"Mata_kuliah": "Data Analysis", "Score": 75},
                {"Mata_kuliah": "Machine Learning", "Score": 80}
            ]
        }
    ]


    deleted_students = []

    while True: 
        title("Akmal International Technology School")
        print("1. Read Data Siswa")
        print("2. Create Data Siswa")
        print("3. Update Data Siswa")
        print("4. Delete Data Siswa")
        print("5. View Deleted Students")
        print("6. Restore Deleted Students")
        print("7. Exit")
        
        choice = pyip.inputInt("Pilih menu: ")
        
        if choice == 1:
             while True:
                 title("Read Menu")
                 print("1. Read Seluruh Data Siswa")
                 print("2. Search Siswa")
                 print("3. Kembali ke Menu Utama")

                 choice = pyip.inputInt("Pilih opsi: ")

                 if choice == 1:
                     if Daftar_student:
                         Daftar_student.sort(key=sort_key)
                         title("Seluruh Data Siswa")
                     
                         all_student_data = []
                         headers = ["NIM", "Nama"]
                         for i in range(3):  # Ganti 3 dengan jumlah maksimal mata kuliah per siswa
                             headers.extend([f"Mata Kuliah {i+1}", "Nilai"])
                         headers.append("Nilai rata-rata")

                         for student in Daftar_student:
                             student_data = [student['nim'], student['nama']]
                             total_score = 0
                             num_scores = 0
                             for matkul in student['Mata_kuliah']:
                                 student_data.extend([matkul['Mata_kuliah'], matkul['Score']])
                                 total_score += matkul['Score']
                                 num_scores += 1
                             if num_scores > 0:
                                  average_score = total_score / num_scores
                                  student_data.append(f"{average_score:.2f}")  # Format to 2 decimal places
                             else:
                                  student_data.append(0)  # Default average for no scores
                                  all_student_data.append(student_data)

                             all_student_data.append(student_data)
                        
                         table = tabulate(all_student_data, headers=headers, tablefmt="grid")
                         print(table)
        
                     else:
                         print("Belum ada data siswa yang tersedia.")

                 elif choice == 2:
                     search = input("Masukkan NIM atau Nama siswa yang ingin dicari: ")
                     if search:
                         found_students = []
                         for student in Daftar_student:
                             if str(student["nim"]) == search or search.lower() in student["nama"].lower():
                                 found_students.append(student)
                         if not found_students:
                             print("Siswa tidak ditemukan.")
                         else:
                             for student in found_students:
                                 read_student(student)
                                 print("-" * 50) 
                     else:
                         continue
                 elif choice == 3:
                     break
                 else:
                     print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 2:
            while True:
                title("Create Menu")
                print("1. Create Data Siswa")
                print("2. Kembali ke Menu Utama")
                choice = pyip.inputInt("Pilih opsi: ")
                if choice == 1:
                    new_student = create_student(Daftar_student)
                    Daftar_student.append(new_student)
                    print("Data siswa berhasil ditambahkan.")
                elif choice == 2:
                    break
                else:
                     print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 3:
            while True:
                title("Update Menu")
                print("1. Update Data Siswa")
                print("2. Kembali ke Menu Utama")

                choice = pyip.inputInt("Pilih opsi: ")

                if choice == 1:
                    nim_to_update = input("Masukkan NIM atau Nama siswa yang ingin diupdate: ")
                    for student in Daftar_student:
                        if str(student["nim"]) == nim_to_update or nim_to_update.lower() in student["nama"].lower():
                            update_student(student)
                            print("Data siswa berhasil diupdate.")
                            break
                    else:
                        print("NIM atau Nama siswa tidak ditemukan.")
                elif choice == 2:
                    break
                else:
                     print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 4:
            while True:
                title("Delete Menu")
                print("1. Delete Data Siswa")
                print("2. Kembali ke Menu Utama")

                choice = pyip.inputInt("Pilih opsi: ")

                if choice == 1:
                    delete_student(Daftar_student, deleted_students)
                elif choice == 2:
                    break
                else:
                     print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 5:
            while True:
                title("View Deleted Menu")
                print("1. View Deleted Students")
                print("2. Kembali ke Menu Utama")

                choice = pyip.inputInt("Pilih opsi: ")

                if choice == 1:
                    view_deleted_students(deleted_students)
                elif choice == 2:
                    break
                else:
                     print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 6:
            while True:
                title("Restore Deleted Menu")
                print("1. Restore Deleted Students")
                print("2. Kembali ke Menu Utama")

                choice = pyip.inputInt("Pilih opsi: ")

                if choice == 1:
                    restore_deleted_student(Daftar_student, deleted_students)
                elif choice == 2:
                    break
                else:
                     print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 7:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

# Blok kode dibawah ini akan dieksekusi hanya jika script ini dijalankan langsung (bukan diimpor sebagai modul)
# Memulai fungsi utama program
if __name__ == "__main__":
    main()
