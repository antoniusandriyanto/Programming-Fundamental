from tabulate import tabulate

nilai=[
    {'NIM':1001, 'Nama':'Alex', 'Jenis Kelamin':'Pria', 'Kota':'Jakarta','Nilai':85.0},
    {'NIM':1002,'Nama':'Janice','Jenis Kelamin':'Wanita','Kota':'Bandung','Nilai':95.0},
    {'NIM':1003,'Nama':'Martin','Jenis Kelamin':'Pria','Kota':'Depok','Nilai':75.0},
    {'NIM':1004,'Nama':'Tasya','Jenis Kelamin':'Wanita','Kota':'Medan','Nilai':80.0},
    {'NIM':1005,'Nama':'Tino','Jenis Kelamin':'Pria','Kota':'Makassar','Nilai':90.0}
]

daftarNilai=[]

def menampilkanNilai(nilai):
    if not nilai:
        print('Tidak ada data yang dapat ditampilkan. Mohon data diinput terlebih dahulu.')
    else:
        header = ['NIM', 'Nama', 'Jenis Kelamin', 'Kota', 'Nilai']
        data = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Kota'], nilai[i]['Nilai']] for i in range(len(nilai))]
        print(tabulate(data, headers=header, tablefmt='grid', stralign='center'))

def subMenu1():
        while True:
            menuTampil=input('''
                Data yang ingin ditampilkan adalah :
                1. Keseluruhan Data
                2. Data Tertentu Berdasarkan NIM
                3. Kembali Menu Utama
                Masukkan angka Menu yang ingin dijalankan :   ''')
            
            if(menuTampil=='1'):
              while True:
                    menampilkanNilai(nilai)
                    break
                    
            elif (menuTampil=='2'):
                while True:
                    menampilkanNilai(nilai)
                    if not nilai:
                        break
                    else:
                        tampilTertentu=input('Masukkan NIM siswa yang ingin ditampilkan : ')
                        if tampilTertentu.isdigit():
                            tampilTertentu=int(tampilTertentu)
                            found = False
                            data_to_display = []
                            for i in nilai:
                                if i['NIM'] == tampilTertentu:
                                    found = True
                                    data_to_display.append([i['NIM'], i['Nama'], i['Jenis Kelamin'], i['Kota'], i['Nilai']])
                                    break
                            if found:
                                header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                print(tabulate(data_to_display, headers=header, tablefmt='grid',stralign='center'))
                            else:
                                print('Maaf NIM yang anda input tidak ditemukan.')
                            break
                        else:
                            print('Mohon diisi menggunakan format numerik')

            elif (menuTampil=='3'):
                break

            else:
                print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')

def subMenu2():
        while True:
            menuTambah=input('''
                Menu yang ingin dijalankan  :
                1. Menambahkan Data Siswa
                2. Kembali Menu Utama
                Masukkan angka Menu yang ingin dijalankan :   ''')
            
            if(menuTambah=='1'):
              while True:
                data_to_added=[]
                while True:
                    tambahNIM=input('Masukkan NIM Siswa (>1000) : ')
                    if tambahNIM.isdigit():
                        tambahNIM=int(tambahNIM)
                        if tambahNIM>1000:
                            exist=False
                            for i in nilai:
                                if tambahNIM == i['NIM']:
                                    exist=True
                                    print('Data yang diinput telah terdaftar')
                            else:
                                break    
                        else:
                            print('Diharapkan menginput NIM dengan ketentuan numerik >=1000')
                    else:
                        print('Diharapkan menginput NIM menggunakan numerik')
                if exist:
                    break
                
                while True:
                    tambahSiswa=input('Masukkan Nama Siswa : ')
                    if tambahSiswa.replace(' ', '').isalpha():
                        tambahSiswa=tambahSiswa.title()
                        break
                    else:
                        print('Diharapkan menginput nama siswa dengan menggunakan alphabetical')

                while True:
                    jenisKelamin=input('Masukkan Jenis Kelamin (Pria / Wanita) : ')
                    jenisKelamin=jenisKelamin.capitalize()
                    if jenisKelamin =="Pria" or jenisKelamin =="Wanita":
                        break
                    else:
                        print('Diharapkan menginput jenis kelamin dengan "Pria" atau "Wanita"')    
                
                while True:
                    tambahAsal=input('Masukkan Asal Siswa (isi alphabetical) : ')
                    if tambahAsal.replace(' ', '').isalpha():
                        tambahAsal=tambahAsal.title()
                        break
                    else:
                        print('Diharapkan menginput nama siswa dengan menggunakan alphabetical')

                while True: 
                    inputNilai=input('Masukkan Nilai : ')
                    if inputNilai.isdigit() or (inputNilai.replace('.', '').isdigit()):
                        inputNilai=float(inputNilai)
                        if inputNilai>=0 and inputNilai<=100:
                            break
                        else:
                            print('Diharapkan menginput nilai dengan numerik di range 0-100')
                    else:
                        print('Diharapkan menginput nilai dengan numerik di range 0-100')
                
                while True:
                    data_to_added.append([tambahNIM, tambahSiswa, jenisKelamin, tambahAsal, inputNilai])
                    header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                    print(tabulate(data_to_added, headers=header, tablefmt='grid', stralign='center'))

                    while True:
                        checkerMenuTambah = input('Apakah anda ingin menambahkan data ini? (ya/tidak): ')
                        if checkerMenuTambah.lower() == 'ya':
                            nilai.append({
                            'NIM':tambahNIM,
                            'Nama':tambahSiswa,
                            'Jenis Kelamin':jenisKelamin,
                            'Asal':tambahAsal,
                            'Nilai': inputNilai     
                            })
                            print('Data telah tersimpan')
                            break
                        elif checkerMenuTambah.lower() == 'tidak':
                            break
                        else:
                            print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')
                    break
                break

            elif(menuTambah=='2'):
                break
              
            else:
                print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')

def subMenu3():
        while True:
            menuHapus=input('''
                Menu yang ingin dijalankan  :
                1. Menghapus Data Siswa
                2. Kembali Menu Utama
                Masukkan angka Menu yang ingin dijalankan :   ''')
            
            if(menuHapus=='1'):
              while True:
                menampilkanNilai(nilai)
                if not nilai:
                        break
                else:
                 while True:
                    hapusData=input('Masukkan NIM siswa yang ingin dihapus : ')
                    if hapusData.isdigit():
                        hapusData=int(hapusData)
                        hapusSiswa=False
                        for i in range (len(nilai)):
                            if nilai[i]['NIM']==hapusData:
                                header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                hapusSiswa = True
                                break
                        if not hapusSiswa:
                            print('Data yang ingin dihapus tidak tersedia')
                        else:
                            while True:
                                checkerMenuHapus = input('Apakah anda ingin menghapus data ini? (ya/tidak): ')
                                if checkerMenuHapus.lower() == 'ya':
                                    del nilai[i]
                                    print('Data telah dihapus')
                                    break
                                elif checkerMenuHapus.lower() == 'tidak':
                                    break
                                else:
                                    print("Pilihan tidak valid. Silakan pilih 'ya' atau 'tidak'.")
                            break
                    else:
                        print('Diharapkan menginput NIM sesuai dengan data yang ingin dihapus')
                    break
                 break

            elif menuHapus == '2':
                break

            else:
                print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')

def subMenu4():
        while True:
            menuUpdate=input('''
                Menu yang ingin dijalankan  :
                1. Mengupdate Data Siswa
                2. Kembali Menu Utama
                Masukkan angka Menu yang ingin dijalankan :   ''')

            if(menuUpdate=='1'):
              while True:
                data_to_update=[]
                menampilkanNilai(nilai)
                if not nilai:
                        break
                else:
                    updateData=input('Masukkan NIM siswa yang ingin diupdate : ')
                    if updateData.isdigit():
                            updateData=int(updateData)
                            updateSiswa=False
                            for i in range (len(nilai)):
                                if nilai[i]['NIM']==updateData:
                                    header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                    dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                    print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                    updateSiswa = True
                                    break
                            if not updateSiswa:
                                print('Data yang ingin diupdate tidak tersedia')
                                break
                            else:
                                while True:
                                    checkerMenuUpdate = input('Apakah anda ingin mengupdate data ini? (ya/tidak): ')
                                    if checkerMenuUpdate.lower() == 'ya':
                                        updateBagian= input('Data yang ingin diupdate adalah (NIM/Nama/Jenis Kelamin/Asal/Nilai) : ')
                                        if updateBagian.upper() == 'NIM':
                                            newValueNIM = input('Masukkan NIM siswa (>1000) (update) : ')
                                            if newValueNIM.isdigit():
                                                newValueNIM=int(newValueNIM)
                                                if newValueNIM > 1000:
                                                    nim_exists = False
                                                    for siswa in nilai:
                                                        if siswa['NIM']== newValueNIM:
                                                            nim_exists=True
                                                    if nim_exists:
                                                        print('Maaf NIM baru yang anda input telah digunakan')
                                                    else:
                                                        oldNIM = nilai[i]['NIM']
                                                        nilai[i]['NIM'] = newValueNIM
                                                        print('Data berhasil diupdate')
                                                        header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                                        dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                                        print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                                        confirm_update = input('Apakah anda yakin untuk mengupdate data ini? (ya/tidak): ')
                                                        if confirm_update.lower() == 'ya':
                                                            print('Data berhasil diperbarui')
                                                        else:
                                                            nilai[i]['NIM'] = oldNIM
                                                            print('Data batal diupdate')
                                                            break
                                                else:
                                                    print('Maaf NIM hanya dapat diinput menggunakan numerikal >1000')
                                            else:
                                                print('Maaf NIM hanya dapat diinput menggunakan numerikal')    
                                        
                                        elif updateBagian.lower() == 'nama':
                                            newValueNama = input('Masukkan nama siswa (update): ')
                                            if newValueNama.replace(' ', '').isalpha():
                                                newValueNama=newValueNama.title()
                                                oldNama = nilai[i]['Nama']
                                                nilai[i]['Nama'] = newValueNama
                                                print('Data berhasil diupdate')
                                                header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                                dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                                print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                                confirm_update = input('Apakah anda yakin untuk mengupdate data ini? (ya/tidak): ')
                                                if confirm_update.lower() == 'ya':
                                                    print('Data berhasil diperbarui')
                                                else:
                                                    nilai[i]['Nama'] = oldNama
                                                    print('Data batal diupdate')
                                                    break
                                            else:
                                                print('Diharapkan menginput nama siswa dengan menggunakan alphabetical')

                                        elif updateBagian.lower() == 'jenis kelamin':
                                            newValueJK = input('Masukkan jenis kelamin siswa (Pria/Wanita) (update) : ')
                                            if newValueJK.lower() in ['pria', 'wanita']:
                                                oldJK = nilai[i]['Jenis Kelamin']
                                                nilai[i]['Jenis Kelamin'] = newValueJK.capitalize()
                                                print('Data berhasil diupdate')
                                                header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                                dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                                print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                                confirm_update = input('Apakah anda yakin untuk mengupdate data ini? (ya/tidak): ')
                                                if confirm_update.lower() == 'ya':
                                                    print('Data berhasil diperbarui')
                                                else:
                                                    nilai[i]['Jenis Kelamin'] = oldJK
                                                    print('Data batal diupdate')
                                                    break
                                            else:
                                                print('Maaf jenis kelamin hanya dapat diisi dengan "Pria" atau "Wanita"')
                                        
                                        elif updateBagian.lower() == 'asal':
                                            newValueAsal = input('Masukkan asal siswa (update) : ')
                                            if newValueAsal.replace(' ', '').isalpha():
                                                oldAsal = nilai[i]['Asal']
                                                newValueAsal = newValueAsal.title()
                                                nilai[i]['Asal'] = newValueAsal
                                                print('Data berhasil diupdate')
                                                header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                                dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                                print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                                confirm_update = input('Apakah anda yakin untuk mengupdate data ini? (ya/tidak): ')
                                                if confirm_update.lower() == 'ya':
                                                    print('Data berhasil diperbarui')
                                                else:
                                                    nilai[i]['Asal'] = oldAsal
                                                    print('Data batal diupdate')
                                                    break
                                            else:
                                                print('Diharapkan menginput asal siswa dengan menggunakan alphabetical')

                                        elif updateBagian.lower() == 'nilai':
                                            newValueNilai = input('Masukkan nilai siswa (update) : ')
                                            if newValueNilai.isdigit() or (newValueNilai.replace('.', '').isdigit()):
                                                newValueNilai=float(newValueNilai)
                                                oldNilai = nilai[i]['Nilai']
                                                if newValueNilai>=0 and newValueNilai<=100:
                                                    nilai[i]['Nilai'] = newValueNilai
                                                    print('Data berhasil diupdate')
                                                    header = ['NIM', 'Nama', 'Jenis Kelamin', 'Asal', 'Nilai']
                                                    dataShow = [[nilai[i]['NIM'], nilai[i]['Nama'], nilai[i]['Jenis Kelamin'], nilai[i]['Asal'], nilai[i]['Nilai']]]
                                                    print(tabulate(dataShow, headers=header, tablefmt='grid',stralign='center'))
                                                    confirm_update = input('Apakah anda yakin untuk mengupdate data ini? (ya/tidak): ')
                                                    if confirm_update.lower() == 'ya':
                                                        print('Data berhasil diperbarui')
                                                    else:
                                                        nilai[i]['Nilai'] = oldNilai
                                                        print('Data batal diupdate')
                                                        break
                                                else:
                                                    print('Diharapkan menginput nilai dengan numerikal di range 0 - 100')
                                            else:
                                                print('Maaf nilai hanya dapat diinput menggunakan numerikal di range 0 - 100')
                                        else:
                                            print('Bagian yang ingin diupdate tidak tersedia')
                                        break
                                    elif checkerMenuUpdate.lower() == 'tidak':
                                        break
                                    else:
                                        print("Pilihan tidak valid. Silakan pilih 'ya' atau 'tidak'.")
                                        break
                    break

            elif menuUpdate == '2':
                break

            else:
                print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')

def filterMinScore(nilai):
    while True:
            min_score = input("Masukkan nilai minimum yang ingin difilter: ")
            if min_score.replace('.', '').isdigit():
                min_score = float(min_score)
                if 0 <= min_score <= 100:
                    filtered_data = [data for data in nilai if data['Nilai'] >= min_score]
                    if filtered_data:
                        return filtered_data
                    else:
                        print("Tidak ada siswa yang memiliki nilai di atas atau sama dengan nilai minimum yang dimasukkan.")
                        break
                else:
                    print("Diharapkan menginput nilai dengan numerikal di range 0 - 100")
            else:
                print("Diharapkan menginput nilai dengan numerikal di range 0 - 100")

def subMenu5():
        while True:
            menuFilter=input('''
                Menu yang ingin dijalankan  :
                1. Memfilter Nilai Siswa
                2. Kembali Menu Utama
                Masukkan angka Menu yang ingin dijalankan :   ''')
            
            if menuFilter == '1':
                filtered_data = filterMinScore(nilai)
                if filtered_data:
                    menampilkanNilai(filtered_data)
            elif menuFilter == '2':
                break
            else:
                print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')

def subMenu6():
        while True:
            print("Anda berhasil keluar dari program.")
            break    

def menuUtama():
    while True:
        pilihanMenu=input('''
                    Selamat Datang di Sekolah Purwadikha
                        
                    List Menu:
                    1. Menampilkan Data Nilai Siswa
                    2. Menambah Data Siswa
                    3. Menghapus Data Siswa
                    4. Mengupdate Data Siswa
                    5. Memfilter Nilai Siswa
                    6. Exit Program
                    Masukkan angka Menu yang ingin dijalankan :   ''')
        
        if(pilihanMenu=='1'):
            subMenu1()
        elif(pilihanMenu=='2'):
            subMenu2()
        elif(pilihanMenu=='3'):
            subMenu3()
        elif(pilihanMenu=='4'):
            subMenu4()
        elif(pilihanMenu=='5'):
            subMenu5()
        elif(pilihanMenu=='6'):
            subMenu6()
            break
        else:
            print('Opsi yang anda pilih tidak tersedia, silahkan pilih opsi yang tersedia')

menuUtama()