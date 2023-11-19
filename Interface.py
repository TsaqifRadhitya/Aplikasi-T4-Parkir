import pandas as pd
import os
import fungsi as fs
import time as ts
import datetime as dt

os.system("cls")          
fs.pembukaan()
print("")
login = fs.login()
while login == "Safe":
    os.system("cls")
    fs.menu()
    print("")
    pilihan = input("Pilihan Layanan : ")
    print("="*82)
    os.system("cls")
    match pilihan:
        case "1":
            plat = fs.cek_plat()
            print("")
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break
                    
        case "3":
            fs.biodata()
            print("")
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break
        case "5":
            fs.History()
            print("")
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break
        case "9":
            fs.penutup()
            break
        case "4":
            fs.DataBase()
            print("")
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break
                    
        case "2":
            fs.kendaraan_keluar()
            print("")
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break

        case "6":
            fs.input_databaru()
            print("")
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break
        case "7":
            fs.hapus_data()
            print("[1] Home\n[2] Exit")
            tanya = fs.navigasi()
            if tanya == "2":
                break
        case "8":
            fs.edit_data()
            
