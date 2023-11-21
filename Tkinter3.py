import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

uiApp = tk.Tk()
uiApp.configure(background='green')
uiApp.geometry("600x800")
uiApp.title("nilai_siswa")


# make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10, fill="x", expand=True)

inputFrame1 = tk.Frame(uiApp)
inputFrame1.pack(padx=10, fill="x", expand=True)

# make label
inputLabel = ttk.Label(inputFrame, text="nilai_siswa")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

# 1. Membuat input nilai mapel
labelInputAIK = ttk.Label(inputFrame, text="Masukkan nama_siswa")
labelInputAIK.pack(padx=10, pady=5, fill="x", expand=True)

entryInputAIK = ttk.Entry(inputFrame)
entryInputAIK.pack(padx=10, pady=5, fill="x", expand=True)

# 2
labelInputMTK = ttk.Label(inputFrame, text="Masukkan nilai matkul biologi")
labelInputMTK.pack(padx=10, pady=5, fill="x", expand=True)

entryInputMTK = ttk.Entry(inputFrame)
entryInputMTK.pack(padx=10, pady=5, fill="x", expand=True)

# 3
labelInputBINDO = ttk.Label(inputFrame, text="Masukkan nilai matkul fisika")
labelInputBINDO.pack(padx=10, pady=5, fill="x", expand=True)

entryInputBINDO = ttk.Entry(inputFrame)
entryInputBINDO.pack(padx=10, pady=5, fill="x", expand=True)

# 4
labelInputBING = ttk.Label(inputFrame, text="Masukkan nilai B INGGRIS")
labelInputBING.pack(padx=10, pady=5, fill="x", expand=True)

entryInputBING = ttk.Entry(inputFrame)
entryInputBING.pack(padx=10, pady=5, fill="x", expand=True)

def klikButton():
    nama_siswa = entryInputAIK.get()
    nilai_biologi = (entryInputMTK.get())
    nilai_fisika = (entryInputBINDO.get())
    nilai_inggris = (entryInputBING.get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi =  "Kedokteran"
        outpul_label.config(text=prediksi)
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi =  "Teknik"
        outpul_label.config(text=prediksi)
    elif nilai_inggris > nilai_fisika and nilai_inggris > nilai_biologi:
        prediksi =  "Bahasa"
        outpul_label.config(text=prediksi)
    else: 
        prediksi = "error"

    messagebox.showinfo("HASIL PREDIKSI_FAKULTAS :", f"\n Prediksi Fakultas: {prediksi}")
    outpul_label.config(text=f"Prediksi Fakultas: {prediksi}")
    simpan_data_ke_sqlite(nama_siswa,nilai_biologi,nilai_fisika,nilai_inggris,prediksi)

def simpan_data_ke_sqlite(nama_siswa,nilaimatkulbiologi,nilaimatkulfisika,nilaimatkulinggris, Fakultas_terpilih):
# Membuka atau membuat database SQLite
    conn = sqlite3.connect("Tkinter.db")
    cursor = conn.cursor()
    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nilai_siswa INTEGER, 
    nama_siswa Text,
    nilaimatkulbiologi INTEGER,
    nilaimatkulfisika INTEGER,
    nilaimatkulinggris INTEGER,
    Fakultas_terpilih TEXT)''')
    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, nilaimatkulbiologi,nilaimatkulfisika,nilaimatkulinggris,Fakultas_terpilih)
     VALUES (?, ?, ?, ?,?)
     ''', (nama_siswa, nilaimatkulbiologi,nilaimatkulfisika,nilaimatkulinggris,Fakultas_terpilih))
    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

buttonSubmit = ttk.Button(inputFrame, text="HASIL PREDIKSI", command=klikButton)
buttonSubmit.pack(padx=10, pady=10, fill="x", expand=True)

outpul_label = ttk.Label(inputFrame1, text="")
outpul_label.pack()

uiApp.mainloop()
