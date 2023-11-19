import os
import pandas as pd
import time as ts
import datetime as dt
from tabulate import tabulate

def pembukaan():
    print("="*82)
    greating = "Selamat datang di aplikasi"
    greating_2 = "E-Parking by T4 Parkir"
    greating = greating.center(82)
    greating_2 = greating_2.center(82)
    print(greating)
    print(greating_2)
    print("="*82)

def menu():
    print("="*82)
    header = "Daftar Layanan E-Parking"
    header = header.center(82)
    print(header)
    print("="*82)
    print("[1] Kendaraan Masuk\n[2] Kendaraan Keluar\n[3] Biodata Pemilik\n[4] Data Member E - Parking\n[5] History Keluar Masuk Kendaraan\n[6] Tambah Member\n[7] Hapus Member\n[8] Edit Data Member\n[9] Exit")

def cek_plat ():
    plat = input("Plat Nomer : ")
    plat = plat.upper()
    os.system("cls")
    df = pd.read_csv("DataBase.csv")
    df = df['Plat Nomor'].tolist()
    if plat in df:
        df = pd.read_csv("History.csv")
        Plat = df["Plat Nomer"].tolist()

        if plat in Plat:
            lokasi = Plat.index(plat)
            status = df.iloc[lokasi,5]

            if status == "Ongoing":
                alert = "Kendaraan Belum Melakukan Check Out Pada Aktivitas Sebelumnya"
                alert = alert.center(82)
                print("="*82)
                print(alert)
                print("="*82)
        
            else:
                alert = f"Kendaraan Dengan Plat {plat} Berhasil Check In"
                alert = alert.center(82)
                print("="*82)
                print(alert)
                print("="*82)
                masuk(plat)

        else:
            alert = f"Kendaraan Dengan Plat {plat} Berhasil Check In"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
            masuk(plat)
    else:
        alert = f"Kendaraan Dengan Plat {plat} Belum Terdaftar"
        alert = alert.center(82)
        print("="*82)
        print(alert)
        print("="*82)

def navigasi():
    tanya = input("Pilihan : ")
    while tanya != "1" and tanya != "2":
        os.system("cls")
        print("[1] Home\n[2] Exit")
        tanya = input("Pilihan : ")
    match tanya:
        case "1":
            os.system("cls")
            
        case "2":
          os.system("cls")
          penutup()
          return "2"

def penutup():
    closing = "Terima Kasih Telah Menggunakan Layanan Kami"
    closing = closing.center(82)
    print("="*82)
    print(closing)
    print("="*82)
    gate = input("Tekan Enter Untuk Lanjut")

def biodata():
    os.system("cls")
    plat = input("Plat Nomor : ")
    plat = plat.upper()
    os.system("cls")
    df = pd.read_csv("DataBase.csv")
    data_plat = df['Plat Nomor'].tolist()
    if plat in data_plat:
        lokasi = data_plat.index(plat)
        biodata = df.iloc[lokasi]
        biodata = biodata.tolist()
        header = "Biodata"
        header = header.center(82)
        print("="*82)
        print(header)
        print("="*82)
        print(f"Plat Nomor : {biodata[0]}\nNama Pemilik : {biodata[1]}\nNIM : {biodata[2]}\nNomor Telepon : {biodata[3]}\nJenis Kendaraan : {biodata[4]}\nMerek Kendaraan : {biodata[5]}\nModel Kendaraan : {biodata[6]}\nWarna Kendaraan : {biodata[7]}")
        print("="*82)

    else:
        alert = f"Data Plat Nomor {plat} Tidak Tersedia"
        alert = alert.center(82)
        print("="*82)
        print(alert)
        print("="*82)
def masuk(plat):
        df = pd.read_csv("DataBase.csv")
        Data_Plat = df['Plat Nomor'].tolist()
        lokasi = Data_Plat.index(plat)
        biodata = df.iloc[lokasi]
        biodata = biodata.tolist()
        jam = ts.ctime(ts.time())
        jam = jam.split(" ")
        jam = jam[-2:-1]
        for x in jam :
            jam = x
        tanggal = dt.date.today()

        data = {"Tanggal":[tanggal],
                "Plat Nomer":[plat],
                "Jenis Kendaraan":[biodata[4]],
                "Nama Pemiliki":[biodata[1]],
                "Jam Masuk":[jam],
                "Jam Keluar":["Ongoing"],
                "Durasi":["Ongoing"]}
        
        data_frame = pd.DataFrame(data)
        data_lama = pd.read_csv("History.csv")
        data_baru = pd.concat([data_frame,data_lama])
        data_baru.to_csv("History.csv",index=False)

def login():
    import os
    user = input("Username : ")

    data = {'user' : ["Admin","User"],
        'Password' : ["Admin","User"]
    }

    data_user = data['user']
    data_pass = data['Password']

    if user in data_user:
        lokasi = data_user.index(user)
        pas = input("Password : ")
        if pas == data_pass[lokasi]:
            status = "Safe"
        else:
            status = "invalid"
    else:
        status = "invalid"

    if status == "invalid":
        for x in range(2):
            os.system("cls")
            alert = "Login Gagal"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
            print("[1] Retry\n[2] Exit")
            pilihan = input("Pilihan : ")
            os.system("cls")
            while pilihan != "1" and pilihan != "2":
                os.system("cls")
                alert = "Login Gagal"
                alert = alert.center(82)
                print("="*82)
                print(alert)
                print("="*82)
                print("[1] Retry\n[2] Exit")
                pilihan = input("Pilihan : ")
                os.system("cls")
            
            match pilihan:
                case "1":
                    os.system("cls")
                    pembukaan()
                    user = input("Username : ")
                    data_user = data['user']
                    data_pass = data['Password']

                    if user in data_user:
                        lokasi = data_user.index(user)
                        pas = input("Password : ")
                        if pas == data_pass[lokasi]:
                            status = "Safe"
                            break
                    else:
                        status = "invalid"
                
                case "2":
                    os.system("cls")
                    penutup()
                    break
        else:
            status = "invalid"
            os.system("cls")
            alert = "Anda Telalu Sering Gagal Login"
            alert = alert.center(82)
            print(alert)
            penutup()

    return status

def input_databaru ():
        df = pd.read_csv("DataBase.csv")
        Data_Plat = df['Plat Nomor'].tolist()
        Plat = input("Plat Nomor : ")
        Plat = Plat.upper()
        status = True
        os.system("cls")
        while len(Plat) < 5 or Plat.isnumeric() == True :
            alert = "Anda Salah Memasukkan Nomor Plat"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
            print("Retry ?\n[1] Yes\n[2] No")
            Pilihan = input("Pilihan : ")
            os.system("cls")
            while Pilihan != "1" and Pilihan != "2":
                print("="*82)
                print(alert)
                print("="*82)
                print("Retry ?\n[1] Yes\n[2] No")
                Pilihan = input("Pilihan : ")
                os.system("cls")
            match Pilihan:
                case "1":
                    Plat = input("Plat Nomor : ")
                    Plat = Plat.upper()
                    os.system("cls")
                    status = True
                case "2":
                    status = False
                    break
        if Plat in Data_Plat and status == True:
            os.system("cls")
            alert = f"Plat Nomer {Plat} Sudah Terdaftar"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
        elif Plat not in Data_Plat and status == True:
            data_nim = df['NIM'].tolist()
            data_nim_string_list = []
            for x in data_nim:
                data_nim_string_list.append(str(x))
            Nim = input("NIM : ")
            status = True
            os.system("cls")

            while Nim.isnumeric() == False or len(Nim) != 12:
                alert = "Anda Salah Memasukkan NIM"
                alert = alert.center(82)
                print("="*82)
                print(alert)
                print("="*82)
                print("Retry ?\n[1] Yes\n[2] No")
                Pilihan = input("Pilihan : ")
                os.system("cls")
                while Pilihan != "1" and Pilihan != "2":
                    print("="*82)
                    print(alert)
                    print("="*82)
                    print("Retry ?\n[1] Yes\n[2] No")
                    Pilihan = input("Pilihan : ")
                    os.system("cls")
                match Pilihan:
                    case "1":
                        Nim = input("NIM : ")
                        os.system("cls")
                        status = True
                    case "2":
                        status = False
                        break

            if Nim in data_nim_string_list and status == True:
                alert = f"NIM {Nim} Telah Terdaftar"
                alert = alert.center(82)
                print("="*82)
                print(alert)
                print("="*82)

            elif Nim not in data_nim and status == True:
                
                Pemilik = input("Nama Lengkap : ")
                Pemilik = Pemilik.upper()
                os.system("cls")    

                Nomer = input("Nomor Telepon(+62) : ")
                status = True
                os.system("cls")
                while Nomer[0] != "+" or len(Nomer) < 14:
                    alert ="Format Nomor Telepon Anda Salah"
                    alert = alert.center(82)
                    print("="*82)
                    print(alert)
                    print("="*82)
                    print("Retry ?\n[1] Yes\n[2] No")
                    Pilihan = input("Pilihan : ")
                    os.system("cls")
                    match Pilihan:
                        case "1":
                            Nomer = input("Nomor Telepon(+62) : ")
                            os.system("cls")
                            status = True
                        case "2":
                            status = False
                            break

                while status == True:
                    print("Tipe Kendaraan")
                    print("[1] Motor\n[2] Mobil")
                    print("")
                    Pilihan = input("Pilihan : ")
                    os.system("cls")
                    match Pilihan:
                        case "1":
                            jenis_kendaraan = "MOTOR"
                            break
                        case "2":
                            jenis_kendaraan = "MOBIL"
                            break
            
                merek = input("Merek Kendaraan : ")
                merek = merek.upper()
                os.system("cls")
                while merek == "":
                    merek = input("Merek Kendaraan : ")
                    merek = merek.upper()
                    os.system("cls")

                model_kendaraan = input("Model Kendaraan : ")
                model_kendaraan = model_kendaraan.upper()
                os.system("cls")
                while model_kendaraan == "":
                    model_kendaraan = input("Model Kendaraan : ")
                    model_kendaraan = model_kendaraan.upper()
                    os.system("cls")

                warna_kendaraan = input("Warna Kendaraan : ")
                warna_kendaraan = warna_kendaraan.upper()
                os.system("cls")
                while warna_kendaraan == "":
                    warna_kendaraan = input("Warna Kendaraan : ")
                    warna_kendaraan = warna_kendaraan.upper()
                    os.system("cls")
                
                data = {"Plat Nomor":[Plat],
                        "Nama Pemilik":[Pemilik],
                        "NIM":[Nim],
                        "Nomer Telepon":[Nomer],
                        "Jenis Kendaraan":[jenis_kendaraan],
                        "Merek Kendaraan":[merek],
                        "Model Kendaraan":[model_kendaraan],
                        "Warna Kendaraan":[warna_kendaraan]}

                data = pd.DataFrame(data)
                konfirmasi = "Biodata"
                konfirmasi = konfirmasi.center(54)

                biodata = f"Plat Nomor : {Plat}\nNama Pemilik : {Pemilik}\nNIM : {Nim}\nNomor Telepon : {Nomer}\nJenis Kendaraan : {jenis_kendaraan}\nMerek Kendaraan : {merek}\nModel Kendaraan : {model_kendaraan}\nWarna Kendaraan : {warna_kendaraan}"
                print("="*82)
                print(konfirmasi)
                print("="*82)
                print(biodata)
                print("="*82)
                print("[1] Upload Biodata\n[2] Batalkan")
                perintah = input("Pilihan : ")
                
                while perintah != "1" and perintah != "2":
                    print("="*82)
                    print(konfirmasi)
                    print("="*82)
                    print(biodata)
                    print("="*82)
                    print("[1] Upload Biodata\n[2] Batalkan")
                    perintah = input("Pilihan : ")

                match perintah:
                    case "1":
                        os.system("cls")
                        final =pd.concat([data,df])
                        final.to_csv("DataBase.csv",index=False)
                        sukses = "Upload Biodata Berhasil"
                        sukses = sukses.center(82)
                        print("="*82)
                        print(sukses)
                        print("="*82)
                    case "2":
                        os.system("cls")
                        gagal = "Upload Biodata Telah Dibatalkan"
                        gagal = gagal.center(82)
                        print("="*82)
                        print(gagal)
                        print("="*82)

def History():
    df = pd.read_csv("History.csv")
    
    data = []

    for x in range (len(df)):
        data_sementara = []
        for y in range(len(df.columns)):
            item = df.iloc[x,y]
            data_sementara.append(str(item).upper())
        data.append(data_sementara)
    
    Header = ["Tanggal","Plat Nomor","Jenis Kendaraan","Nama Pemilik","Jam Masuk","Jam Keluar","Durasi"]
    frame = tabulate(data,headers=Header,tablefmt="fancy_grid")
    print(frame)

def DataBase():
    df=pd.read_csv("DataBase.csv")
    
    data = []

    for x in range (len(df)):
        data_sementara = []
        for y in range(len(df.columns)-3):
            item = df.iloc[x,y]
            data_sementara.append(str(item).upper())
        data.append(data_sementara)
    
    Header = ["Plat Nomor","Nama Pemilik","NIM","Nomer Telepon","Jenis Kendaraan"]
    frame = tabulate(data,headers=Header,tablefmt="fancy_grid")
    print(frame)


def hapus_data():
    os.system("cls")
    Nim = input("NIM : ")
    acces = True
    os.system("cls")
    while Nim.isnumeric() == False or len(Nim) != 12 :
        alert = "Anda Salah Memasukkan NIM"
        alert = alert.center(82)
        print("="*82)
        print(alert)
        print("="*82)
        print("Retry ?\n[1] Yes\n[2] No")
        Pilihan = input("Pilihan : ")
        os.system("cls")
        while Pilihan != "1" and Pilihan != "2":
            print("Retry ?\n[1] Yes\n[2] No")
            Pilihan : input("Pilihan : ")
            os.system("cls")

        match Pilihan:
            case "1":
                Nim = input("NIM : ")
                os.system("cls")

            case "2":
                acces = False

    df = pd.read_csv("DataBase.csv")
    df = df['NIM'].tolist()
    data_nim = []
    for x in df:
        data_nim.append(str(x))

    if Nim in data_nim and acces == True:
        df = pd.read_csv("DataBase.csv")
        os.system("cls")
        lokasi = data_nim.index(Nim)
        data_member = df.iloc[lokasi]
        data_member = data_member.tolist()
        Header = "Biodata"
        Header = Header.center(82)
        print("="*82)
        print(Header)
        print("="*82)
        data_hapus = f"Plat Nomor : {data_member[0]}\nNama Pemilik : {data_member[1]}\nNIM : {data_member[2]}\nNomor Telepon : {data_member[3]}\nJenis Kendaraan : {data_member[4]}\nMerek Kendaraan : {data_member[5]}\nModel Kendaraan : {data_member[6]}\nWarna Kendaraan : {data_member[7]}"
        print(data_hapus)
        print("="*82)
        while True:
            os.system("cls")
            print("="*82)
            print(Header)
            print("="*82)
            print(data_hapus)
            print("="*82)
            print("[1] Hapus Data\n[2] Batalkan")
            opsi = input("Pilihan : ")
            match opsi:
                case "1":
                    os.system("cls")
                    df = df.drop(lokasi)
                    df.to_csv("DataBase.csv",index=False)
                    alert = "Penghapusan Data Berhasil"
                    alert = alert.center(82)
                    print("="*82)
                    print(alert)
                    print("="*82)
                    break
                case "2":
                    os.system("cls")
                    alert = "Penghapusan Data Telah dibatalkan"
                    alert = alert.center(82)
                    print("="*82)
                    print(alert)
                    print("="*82)
                    break
    elif Nim not in data_nim and acces == True: 
        os.system("cls")
        print("="*82)
        alert = "Plat Nomor Belum Terdaftar"
        alert = alert.center(82)
        print(alert)
        print("="*82)

def kendaraan_keluar():
    plat = input("Plat Nomor : ")
    os.system("cls")
    plat = plat.upper()
    df = pd.read_csv("DataBase.csv")
    data_plat = df["Plat Nomor"].tolist()

    if plat in data_plat:
        History= pd.read_csv("History.csv")
        Lokasi_History = History["Plat Nomer"].tolist()
        lokasi = Lokasi_History.index(plat)
        status = History.iloc[lokasi,5]
        if status == "Ongoing":
            jam_pertama = History["Jam Masuk"].tolist()
            jam_pertama = jam_pertama[lokasi]

            jam_Kedua = ts.ctime(ts.time())
            jam_Kedua = jam_Kedua.split(" ")
            jam_Kedua = jam_Kedua[-2:-1]
            for x in jam_Kedua:
                jam_Kedua = x


            x = dt.datetime.strptime(jam_pertama, "%H:%M:%S")
            y = dt.datetime.strptime(jam_Kedua, "%H:%M:%S")

            durasi = y-x
            durasi = str(durasi)
            durasi = durasi.split(":")

            if durasi[0] == "0":
                if durasi[1] == "00":
                    format = f"{durasi[2]} detik"
                elif durasi[1] == "00" and durasi[2] == "00":
                    format = "Telalu Cepat"
                else:
                    format = f"{durasi[1]} Menit {durasi[2]} Detik"
        
            else:
                if durasi[1] == "00":
                    format = f"{durasi[0]} Jam {durasi[2]} Detik"
                elif durasi[2] == "00":
                    format = f"{durasi[0]} Jam {durasi[1]} Menit"
                elif durasi[1] == "00" and durasi[2] == "00":
                    format = f"{durasi[2]} Detik"
                else:
                    format = f"{durasi[0]} Jam {durasi[1]} Menit {durasi[2]} Detik"
            alert = f"Plat Nomor {plat} Berhasil Melakukan Check Out"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
            History.iloc[lokasi,5] = jam_Kedua
            History.iloc[lokasi,6] = format
            History.to_csv("History.csv",index=False)

        else:
            alert = "Kendaraan Belum Melakukan Check In"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
    else:
        alert = f"Plat Nomor {plat} Belum Terdaftar"
        alert = alert.center(82)
        print("="*82)
        print(alert)
        print("="*82)

def edit_data():
    user_nim = input("NIM : ")
    os.system("cls")
    acces = True
    while user_nim.isnumeric() == False or len(user_nim) != 12:
        alert = "Anda Salah Memasukkan NIM"
        alert = alert.center(82)
        print("="*82)
        print(alert)
        print("="*82)
        print("")
        print("[1] Retry\n[2] Home")
        pilihan = input("Pilihan : ")
        os.system("cls")
        while pilihan != "1" and pilihan != "2":
            print("="*82)
            print(alert)
            print("="*82)
            print("")
            print("[1] Retry\n[2] Home")
            pilihan = input("Pilihan : ")
            os.system("cls")

        match pilihan:
            case "1":
                user_nim = input("NIM : ")
                os.system("cls")
            case "2":
                acces = False
                break
    
    df = pd.read_csv("DataBase.csv")
    data_nim = df['NIM'].tolist()
    data_nim_str =[]
    for x in data_nim:
        data_nim_str.append(str(x))

    if user_nim in data_nim_str and acces == True:
        lokasi = data_nim_str.index(user_nim)
        print(lokasi)
        data_user = df.iloc[lokasi].tolist()
        data_base = f"Plat Nomer : {data_user[0]}\nNama Pemilik : {data_user[1]}\nNIM : {data_user[2]}\nNomor Telepon : {data_user[3]}\nJenis Kendaraan : {data_user[4]}\nMerek Kendaraan : {data_user[5]}\nModel Kendaraan : {data_user[6]}\nWarna Kendaraan : {data_user[7]}"
        header = "Biodata"
        header = header.center(82)
        print("="*82)
        print(header)
        print("="*82)
        print(data_base)
        print("="*82)
        print("")
        print("[1] Edit Data Plat Nomer\n[2] Edit Data Kendaraan\n[3] Home")
        Pilihan = input("Pilihan : ")
        os.system("cls")
        while Pilihan not in ["1","2","3"]:
            print("="*82)
            print(header)
            print("="*82)
            print(data_base)
            print("="*82)
            print("")
            print("[1] Edit Data Plat Nomer\n[2] Edit Data Kendaraan\n[3] Home")
            Pilihan = input("Pilihan : ")
            os.system("cls")
        match Pilihan:
            case "1":
                Plat_baru = input("Plat Nomor : ")
                Plat_baru = Plat_baru.upper()
                os.system("cls") 
                while len(Plat_baru) < 5 :
                    alert = "Plat Nomer Anda Salah"
                    alert = alert.center(82)
                    print("="*82)
                    print(alert)
                    print("="*82)
                    Plat_baru = input("Plat Nomor : ")

                data_baru = f"Plat Nomer : {Plat_baru}\nNama Pemilik : {data_user[1]}\nNIM : {data_user[2]}\nNomor Telepon : {data_user[3]}\nJenis Kendaraan : {data_user[4]}\nMerek Kendaraan : {data_user[5]}\nModel Kendaraan : {data_user[6]}\nWarna Kendaraan : {data_user[7]}"
                header = "Biodata"
                header = header.center(82)
                print("="*82)
                print(header)
                print("="*82)
                print(data_baru)
                print(("="*82))
                print("[1] Perbarui Data\n[2] Batalkan")
                Pilihan = input("Pilihan : ")
                os.system("cls")
                while Pilihan not in ["1","2"]:
                    os.system("cls")
                    print("="*82)
                    print(header)
                    print("="*82)
                    print(data_baru)
                    print(("="*82))
                    print("[1] Perbarui Data\n[2] Batalkan")
                    Pilihan = input("Pilihan : ")
                        
                match Pilihan:
                    case "1":
                        df.iloc[lokasi,0] = Plat_baru
                        df.to_csv("DataBase.csv",index=False)
                            
                    case "2":
                        alert = "Perbaruan Data Telah Dibatalkan"
                        alert = alert.center(82)
                        print("="*82)
                        print(alert)
                        print("="*82)
                        Pilihan = input("Tekan Enter Untuk Lanjut")
                        os.system("cls")
                       
                        match Pilihan:
                            case "":
                                os.system("cls")
                    
            case "2":
                Plat_baru = input("Plat Nomor : ")
                Plat_baru = Plat_baru.upper()
                os.system("cls")
                while len(Plat_baru)<5 or Plat_baru.isnumeric == True:
                    alert = "Plat Nomer Salah"
                    alert = alert.center(82)
                    print("="*82)
                    print(alert)
                    print("="*82)
                    Plat_baru = input("Plat Nomor : ")
                    Plat_baru = Plat_baru.upper()
                    os.system("cls")

                print("Jenis Kendaraan\n[1] Motor\n[2] Mobil")
                Pilihan = input("Pilihan : ")
                os.system("cls")
                while Pilihan not in ["1","2"]:
                    print("Jenis Kendaraan\n[1] Motor\n[2] Mobil")
                    Pilihan = input("Pilihan : ")
                    os.system("cls")

                match Pilihan:
                    case "1":
                        jenis_kendaraan = "MOTOR"
                    case "1":
                        jenis_kendaraan = "MOBIL"
                
                Merek_kendaraan = input("Merek Kendaraan : ")
                Merek_kendaraan = Merek_kendaraan.upper()
                os.system("cls")
                while Merek_kendaraan == "":
                    Merek_kendaraan = input("Merek Kendaraan : ")
                    Merek_kendaraan = Merek_kendaraan.upper()
                    os.system("cls")

                Model_kendaraan = input("Model Kendaraan : ")
                Model_kendaraan = Model_kendaraan.upper()
                os.system("cls")
                while Model_kendaraan == "":
                    Model_kendaraan = input("Model Kendaraan : ")
                    Model_kendaraan = Model_kendaraan.upper()
                    os.system("cls")
                
                warna_kendaraan = input("Warna Kendaraan : ")
                warna_kendaraan = warna_kendaraan.upper()
                os.system("cls")
                while warna_kendaraan == "":
                    warna_kendaraan = input("Warna Kendaraan : ")
                    warna_kendaraan = warna_kendaraan.upper()
                    os.system("cls")

                data_baru = f"Plat Nomer : {Plat_baru}\nNama Pemilik : {data_user[1]}\nNIM : {data_user[2]}\nNomor Telepon : {data_user[3]}\nJenis Kendaraan : {jenis_kendaraan}\nMerek Kendaraan : {Merek_kendaraan}\nModel Kendaraan : {Model_kendaraan}\nWarna Kendaraan : {warna_kendaraan}"
                header = "Biodata"
                header = header.center(82)
                print("="*82)
                print(header)
                print("="*82)
                print(data_baru)
                print(("="*82))
                print("[1] Perbarui Data\n[2] Batalkan")
                Pilihan = input("Pilihan : ")
                os.system("cls")
                while Pilihan not in ["1","2"]:
                    os.system("cls")
                    print("="*82)
                    print(header)
                    print("="*82)
                    print(data_baru)
                    print(("="*82))
                    print("[1] Perbarui Data\n[2] Batalkan")
                    Pilihan = input("Pilihan : ")
                        
                match Pilihan:
                    case "1":
                        df.iloc[lokasi,0] = Plat_baru
                        df.iloc[lokasi,3] = jenis_kendaraan
                        df.iloc[lokasi,4] = Merek_kendaraan
                        df.iloc[lokasi,5] = Model_kendaraan
                        df.iloc[lokasi,6] = warna_kendaraan
                        df.to_csv("DataBase.csv",index=False)
                            
                    case "2":
                        alert = "Perbaruan Data Telah Dibatalkan"
                        alert = alert.center(82)
                        print("="*82)
                        print(alert)
                        print("="*82)
                        Pilihan = input("Tekan Enter Untuk Lanjut")
                        os.system("cls")

                        match Pilihan:
                            case "":
                                os.system("cls")

            case "3":
                os.system("cls")

    elif user_nim not in data_nim_str and acces == True:
        alert = f"Data Pada NIM {user_nim} Tidak Tersedia"
        alert = alert.center(82)
        print("="*82)
        print(alert)
        print("="*82)
        Pilihan = input("Tekan Entek Untuk Kembali Ke Home")

        match Pilihan:
            case "":
                os.system("cls")
         