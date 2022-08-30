# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:51:48 2022

@author: asus
"""

#!pip install mysql-connector-python
#Import the Tkinter module
#Tkinter adalah antarmuka Python ke toolkit GUI Tk yang dikirimkan bersama Python
from tkinter import *
#Import the mysql.connector as mysql
import mysql.connector as mysql
#Import the messagebox module from tkinter
from tkinter import messagebox
#Import the ttk module from tkinter
from  tkinter import ttk

#Membuat window utama baru untuk aplikasi GUI dengan nama variabel window
window = Tk()

#Mendeklarasikan variabel my_table dengan nilai ttk.Treeview(window)
my_table = ttk.Treeview(window)

#Membuat title untuk window utama baru untuk aplikasi GUI dengan nama 'Perpustakaan Apps 195314142'
window.title('Perpustakaan Apps 195314142')
#Membuat size untuk window utama baru untuk aplikasi GUI dengan ukuran "1067x620"
window.geometry("1067x620")
#Membuat background untuk window utama baru untuk aplikasi GUI dengan warna "salmon"
window.config(bg="salmon")

#Mengatur resizable window GUI agar tidak dapat di minimize dan maximize 
window.resizable(0,0)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_window dimana pada label tersebut terletak pada window dengan nama "PERPUSTAKAAN AUDY", dengan jenis font "Times New Roman", dengan ukuran 20 dengan background "salmon", dengan batas atas dan bawah 5
label_window = Label(window, text="PERPUSTAKAAN AUDY", font=("Times New Roman", 20), bg="salmon", pady=5)
#Mengatur posisi widget pada grid label_window di window utama
label_window.grid(row=0, column=0, columnspan=2, sticky=N)

#Function
#Membuat method bernama connection untuk melakukan connection dengan database
def connection():
    #Mendeklarasikan variabel host dengan nilai "localhost" merupakan host pada database
    host = "localhost"
    #Mendeklarasikan variabel user dengan nilai "root" merupakan nama user pada database
    user = "root"
    #Mendeklarasikan variabel passwd dengan nilai "" merupakan password pada database
    passwd = ""
    #Mendeklarasikan variabel database dengan nilai "perpustakaan" merupakan database yang berupa tabel 
    database = "perpustakaan"

    #Mendeklarasikan variabel db dengan nilai "host = host, user = user, passwd = passwd, database = database" merupakan connection ke database
    db = mysql.connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
        )
    #Memanggil kembali variabel db
    return db

#Membuat method bernama tambah untuk melakukan tambah data pada database
def tambah():
    #Mendeklarasikan variabel judul_buku dengan nilai dari data "entry_judulBuku" menggunakan get
    judul_buku = entry_judulBuku.get()
    #Mendeklarasikan variabel tahun_terbit dengan nilai dari data "entry_tahunTerbit" menggunakan get
    tahun_terbit = entry_tahunTerbit.get()
    #Mendeklarasikan variabel isbn dengan nilai dari data "entry_ISBN" menggunakan get
    isbn = entry_ISBN.get()
    #Mendeklarasikan variabel pengarang dengan nilai dari data "entry_Pengarang" menggunakan get
    pengarang = entry_Pengarang.get()
    #Mendeklarasikan variabel penerbit dengan nilai dari data "entry_Penerbit" menggunakan get
    penerbit = entry_Penerbit.get()
    #Mendeklarasikan variabel rak dengan nilai dari data "entry_Rak" menggunakan get
    rak = entry_Rak.get()
    #Mendeklarasikan variabel stok dengan nilai dari data "entry_Stok" menggunakan get
    stok = entry_Stok.get()
    
    #Membuat perulangan ketika user mengisi kosong pada "(judul_buku=="" or judul_buku==" ") or (tahun_terbit=="" or tahun_terbit==" ") or (isbn=="" or isbn==" ") or (pengarang=="" or pengarang==" ") or (penerbit=="" or penerbit==" ") or (rak=="" or rak==" ") or (stok=="" or stok==" ")", maka akan menjalankan perintah if ini
    if (judul_buku=="" or judul_buku==" ") or (tahun_terbit=="" or tahun_terbit==" ") or (isbn=="" or isbn==" ") or (pengarang=="" or pengarang==" ") or (penerbit=="" or penerbit==" ") or (rak=="" or rak==" ") or (stok=="" or stok==" "):
        #Membuat messagebox ketika user tidak menginputkan semua perintah pada perintah if
        messagebox.showinfo("Error", "Pastikan semua field terisi!")
        #Memanggil kembali perintah if 
        return
    #Membuat perulangan ketika user mengisi "(judul_buku=="" or judul_buku==" ") or (tahun_terbit=="" or tahun_terbit==" ") or (isbn=="" or isbn==" ") or (pengarang=="" or pengarang==" ") or (penerbit=="" or penerbit==" ") or (rak=="" or rak==" ") or (stok=="" or stok==" ")", maka akan menjalankan perintah else ini
    else:
        #Mencoba mengakses database
        try:
            #Mendeklarasikan variabel conn dengan nilai dari method connection
            conn = connection()
            #Mendeklarasikan variabel cursor dengan nilai dari method cursor
            cursor = conn.cursor()
            #Mendeklarasikan variabel sql dengan nilai dari request kedata base untuk menambah data (judul, tahun, isbn, pengarang, penerbit, rak, stok) 
            sql = """INSERT INTO perpustakaan
                        (judul, tahun, isbn, pengarang, penerbit, rak, stok)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            #Menjalankan request ke database untuk menyimpan data yang telah ditambah dengan disimpan pada variabel cursor
            cursor.execute(sql, (judul_buku, tahun_terbit, isbn, pengarang, penerbit, rak, stok))
            #Melakukan request ke database dengan disimpan pada variabel conn
            conn.commit()
            #Menutup request setelah berhasil menambahkan data
            conn.close()
            #Membuat messagebox ketika user berhasil menginputkan data
            messagebox.showinfo("Success", "Data buku berhasil ditambahkan!")
        #Menjalan kan perintah ini ketika gagal melakukan menambahkan data 
        except:
            #Membuat messagebox ketika user gagal menginputkan data
            messagebox.showinfo("Error", "Data buku gagal ditambahkan!")
            #Memanggil kembali perintah try 
            return
    #Melakukan refresh untuk GUI ketika mengklik tombol batal
    refreshTable()
    batal()

#Membuat method bernama hapus untuk melakukan hapus data pada database
def hapus():
    #Mendeklarasikan variabel pilih_kode dengan nilai "" 
    pilih_kode = ""
    #Mencoba mengakses database
    try:
        #Mendeklarasikan variabel pilih_data dengan nilai dari "my_table.selection()" dengan indeks 0
        pilih_data = my_table.selection()[0]
        #Mendeklarasikan variabel pilih_kode dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 0
        pilih_kode = (my_table.item(pilih_data)['values'][0])
    #Menjalan kan perintah ini ketika gagal melakukan hapus data 
    except :
        #Membuat messagebox ketika user gagal hapus data karena belum memilih data yang akan dihapus
        messagebox.showinfo("Error", "Silahkan pilih data buku pada tabel terlebih dahulu!")
        #Memanggil kembali perintah except 
        return
    #Mendeklarasikan variabel desicion dengan nilai messagebox ketika memintah user untuk confirm data yang akan dihapus 
    desicion = messagebox.askquestion("Confirm", "Hapus data buku yang dipilih?")
    #Membuat perulangan ketika user mengisi nilai dari variabel desicion tidak sama dengan yes, maka akan menjalankan perintah if ini
    if desicion != "yes":
        #Memanggil kembali perintah if 
        return
    #Membuat perulangan ketika user mengisi nilai dari variabel desicion sama dengan yes, maka akan menjalankan perintah else ini
    else :
        #Mencoba mengakses database
        try:
            #Mendeklarasikan variabel conn dengan nilai dari method connection
            conn = connection()
            #Mendeklarasikan variabel cursor dengan nilai dari method cursor
            cursor = conn.cursor()
            #Menjalankan request ke database untuk menghapus data dengan disimpan pada variabel cursor
            cursor.execute("DELETE FROM perpustakaan WHERE kode='"+str(pilih_kode)+"'")
            #Melakukan request ke database dengan disimpan pada variabel conn
            conn.commit()
            #Menutup request setelah berhasil hapus data
            conn.close()
            #Membuat messagebox ketika user berhasil hapus data
            messagebox.showinfo("Success", "Data buku berhasil dihapus!")
        #Menjalan kan perintah ini ketika gagal melakukan hapus data 
        except:
            #Membuat messagebox ketika user gagal hapus data
            messagebox.showinfo("Error", "Data buku gagal dihapus!")
            #Memanggil kembali perintah try 
            return
    #Melakukan refresh untuk GUI ketika mengklik tombol batal
    refreshTable()

#Membuat method bernama pilih untuk melakukan pilih data pada database
def pilih():
    #Mencoba mengakses database
    try:
        #Mendeklarasikan variabel pilih_data dengan nilai dari "my_table.selection()" dengan indeks 0
        pilih_data = my_table.selection()[0]
        
        #Mendeklarasikan variabel judul_buku dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 1
        judul_buku = (my_table.item(pilih_data)['values'][1])
        #Mendeklarasikan variabel tahun_terbit dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 2
        tahun_terbit = (my_table.item(pilih_data)['values'][2])
        #Mendeklarasikan variabel isbn dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 3
        isbn = (my_table.item(pilih_data)['values'][3])
        #Mendeklarasikan variabel pengarang dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 4
        pengarang = (my_table.item(pilih_data)['values'][4])
        #Mendeklarasikan variabel penerbit dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 5
        penerbit = (my_table.item(pilih_data)['values'][5])
        #Mendeklarasikan variabel rak dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 6
        rak = (my_table.item(pilih_data)['values'][6])
        #Mendeklarasikan variabel stok dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 7
        stok = (my_table.item(pilih_data)['values'][7])
        
        #Mengeset nilai judul_buku dengan nilai indeks 1 pada data base
        setNilai(judul_buku, 1)
        #Mengeset nilai tahun_terbit dengan nilai indeks 2 pada data base
        setNilai(tahun_terbit, 2)
        #Mengeset nilai isbn dengan nilai indeks 3 pada data base
        setNilai(isbn, 3)
        #Mengeset nilai pengarang dengan nilai indeks 4 pada data base
        setNilai(pengarang, 4)
        #Mengeset nilai penerbit dengan nilai indeks 5 pada data base
        setNilai(penerbit, 5)
        #Mengeset nilai rak dengan nilai indeks 6 pada data base
        setNilai(rak, 6)
        #Mengeset nilai stok dengan nilai indeks 7 pada data base
        setNilai(stok, 7)
    #Menjalan kan perintah ini ketika gagal melakukan pilih data 
    except:
        #Membuat messagebox ketika user gagal pilih data karena belum memilih data pada tabel
        messagebox.showinfo("Error", "Silahkan pilih data buku pada tabel terlebih dahulu!")

#Membuat method bernama batal untuk melakukan batal data pada GUI
def batal():
    #Mengeset nilai dari entry_judulBuku ketika user menekan button batal
    entry_judulBuku.delete(0,END)
    #Mengeset nilai dari entry_tahunTerbit ketika user menekan button batal
    entry_tahunTerbit.delete(0,END)
    #Mengeset nilai dari entry_ISBN ketika user menekan button batal
    entry_ISBN.delete(0,END)
    #Mengeset nilai dari entry_Pengarang ketika user menekan button batal
    entry_Pengarang.delete(0,END)
    #Mengeset nilai dari entry_Penerbit ketika user menekan button batal
    entry_Penerbit.delete(0,END)
    #Mengeset nilai dari entry_Rak ketika user menekan button batal
    entry_Rak.delete(0,END)
    #Mengeset nilai dari entry_Stok ketika user menekan button batal
    entry_Stok.delete(0,END)
    #Mengeset nilai dari entry_Pencarian ketika user menekan button batal
    entry_Pencarian.delete(0,END)
    #Melakukan refresh untuk GUI ketika mengklik tombol batal
    refreshTable()

#Membuat method bernama setNilai untuk mengatur nilai data pada GUI agar sesuai database
def setNilai(nilai, num):
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_judulBuku, maka akan menjalankan perintah if ini
    if num == 1:
        #Menyimpan nilai kedalaman variabel entry_judulBuku
        entry_judulBuku.insert(INSERT, nilai)
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_tahunTerbit, maka akan menjalankan perintah if ini
    if num == 2:
        #Menyimpan nilai kedalaman variabel entry_tahunTerbit
        entry_tahunTerbit.insert(INSERT, nilai)
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_ISBN, maka akan menjalankan perintah if ini
    if num == 3:
        #Menyimpan nilai kedalaman variabel entry_ISBN
        entry_ISBN.insert(INSERT, nilai)
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_Pengarang, maka akan menjalankan perintah if ini
    if num == 4:
        #Menyimpan nilai kedalaman variabel entry_Pengarang
        entry_Pengarang.insert(INSERT, nilai)
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_Penerbit, maka akan menjalankan perintah if ini
    if num == 5:
        #Menyimpan nilai kedalaman variabel entry_Penerbit
        entry_Penerbit.insert(INSERT, nilai)
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_Rak, maka akan menjalankan perintah if ini
    if num == 6:
        #Menyimpan nilai kedalaman variabel entry_Rak
        entry_Rak.insert(INSERT, nilai)
    #Membuat perulangan ketika user mengisi nilai dari variabel entry_Stok, maka akan menjalankan perintah if ini
    if num == 7:
        #Menyimpan nilai kedalaman variabel entry_Stok
        entry_Stok.insert(INSERT, nilai)

#Membuat method bernama cari untuk melakukan cari data pada database
def cari():
    #Mendeklarasikan variabel judul_buku dengan nilai "entry_Pencarian" menggunakan get
    judul_buku = entry_Pencarian.get()
    #Mendeklarasikan variabel conn dengan nilai dari method connection
    conn = connection()
    #Mendeklarasikan variabel cursor dengan nilai dari method cursor
    cursor = conn.cursor()
    #Menjalankan request ke database untuk mencari data dengan value judul_buku dengan disimpan pada variabel cursor
    cursor.execute("SELECT * FROM perpustakaan WHERE judul='"+judul_buku+"'")
    #Mencoba mengakses database
    try:
        #Mendeklarasikan variabel result dengan nilai dari "cursor.fetchall()" 
        result = cursor.fetchall()
        #Membuat perulangan for ketika user mengisi nilai dari variabel num sama dengan range antar untuk indeks 0 sampai 7, maka akan menjalankan perintah for ini
        for num in range(0,7):
            #Mengeset nilai hasil setelah mendapat kan data setelah melakukan pencarian
            setNilai(result[0][(num+1)], (num+1))
        #Melakukan request ke database dengan disimpan pada variabel conn
        conn.commit()
        #Menutup request setelah berhasil menemukan data
        conn.close()
    #Menjalan kan perintah ini ketika gagal menemukan data 
    except ValueError as e:
        #Membuat messagebox ketika user menemukan data 
        messagebox.showinfo("Error", "Buku tidak ditemukan!")
        #Mencetak nilai e 
        print(e)
#Membuat method bernama edit untuk melakukan edit data pada database
def edit():
    #Mendeklarasikan variabel pilih_kode dengan nilai "" 
    pilih_kode = ""
    #Mencoba mengakses database
    try:
        #Mendeklarasikan variabel pilih_data dengan nilai dari "my_table.selection()" dengan indeks 0
        pilih_data = my_table.selection()[0]
        #Mendeklarasikan variabel pilih_kode dengan nilai dari "my_table.item(pilih_data)['values']" dengan indeks 0
        pilih_kode = (my_table.item(pilih_data)['values'][0])
    #Menjalan kan perintah ini ketika gagal menemukan data 
    except :
        #Membuat messagebox ketika user gagal pilih data karena belum memilih data pada tabel
        messagebox.showinfo("Error", "Silahkan pilih buku pada tabel terlebih dahulu!")
        #Memanggil kembali perintah except 
        return
    
    #Mendeklarasikan variabel judul_buku dengan nilai dari data "entry_judulBuku" menggunakan get
    judul_buku = entry_judulBuku.get()
    #Mendeklarasikan variabel tahun_terbit dengan nilai dari data "entry_judulBuku" menggunakan get
    tahun_terbit = entry_tahunTerbit.get()
    #Mendeklarasikan variabel isbn dengan nilai dari data "entry_judulBuku" menggunakan get
    isbn = entry_ISBN.get()
    #Mendeklarasikan variabel pengarang dengan nilai dari data "entry_judulBuku" menggunakan get
    pengarang = entry_Pengarang.get()
    #Mendeklarasikan variabel penerbit dengan nilai dari data "entry_judulBuku" menggunakan get
    penerbit = entry_Penerbit.get()
    #Mendeklarasikan variabel rak dengan nilai dari data "entry_judulBuku" menggunakan get
    rak = entry_Rak.get()
    #Mendeklarasikan variabel stok dengan nilai dari data "entry_judulBuku" menggunakan get
    stok = entry_Stok.get()
    
    #Membuat perulangan ketika user mengisi kosong pada "(judul_buku=="" or judul_buku==" ") or (tahun_terbit=="" or tahun_terbit==" ") or (isbn=="" or isbn==" ") or (pengarang=="" or pengarang==" ") or (penerbit=="" or penerbit==" ") or (rak=="" or rak==" ") or (stok=="" or stok==" ")", maka akan menjalankan perintah if ini
    if (judul_buku=="" or judul_buku==" ") or (tahun_terbit=="" or tahun_terbit==" ") or (isbn=="" or isbn==" ") or (pengarang=="" or pengarang==" ") or (penerbit=="" or penerbit==" ") or (rak=="" or rak==" ") or (stok=="" or stok==" "):
        #Membuat messagebox ketika user tidak menginputkan semua perintah pada perintah if
        messagebox.showinfo("Error", "Pastikan semua field terisi!")
        #Memanggil kembali perintah if 
        return
    #Membuat perulangan ketika user mengisi "(judul_buku=="" or judul_buku==" ") or (tahun_terbit=="" or tahun_terbit==" ") or (isbn=="" or isbn==" ") or (pengarang=="" or pengarang==" ") or (penerbit=="" or penerbit==" ") or (rak=="" or rak==" ") or (stok=="" or stok==" ")", maka akan menjalankan perintah else ini
    else:
        #Mencoba mengakses database
        try:
            #Mendeklarasikan variabel conn dengan nilai dari method connection
            conn = connection()
            #Mendeklarasikan variabel cursor dengan nilai dari method cursor
            cursor = conn.cursor()
            #Mendeklarasikan variabel sql dengan nilai dari request kedata base untuk update data (judul, tahun, isbn, pengarang, penerbit, rak, stok) 
            sql = """UPDATE perpustakaan SET judul=%s, tahun=%s, isbn=%s, pengarang=%s, penerbit=%s, rak=%s, stok=%s WHERE kode=%s"""
            #Menjalankan request ke database untuk menyimpan data yang telah diupdate dengan disimpan pada variabel cursor
            cursor.execute(sql, (judul_buku, tahun_terbit, isbn, pengarang, penerbit, rak, stok, pilih_kode))
            #Melakukan request ke database dengan disimpan pada variabel conn
            conn.commit()
            #Menutup request setelah berhasil menemukan data
            conn.close()
            #Membuat messagebox ketika user berhasil diedit data
            messagebox.showinfo("Success", "Data buku berhasil diedit!")
        #Menjalan kan perintah ini ketika gagal diedit data 
        except:
            #Membuat messagebox ketika user gagal diedit data
            messagebox.showinfo("Error", "Data buku gagal diedit!")
            #Memanggil kembali perintah except 
            return
    #Melakukan refresh untuk GUI ketika mengklik tombol batal
    refreshTable()
    batal()

#Frame Data Buku
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_DataBuku dimana pada Frame tersebut terletak pada window dengan nama labelnya "Data Buku", dengan jenis font "Times New Roman", dengan ukuran 10 dengan background "salmon"
frame_DataBuku = LabelFrame(window, text="Data Buku", font=("Times New Roman", 10), bg="salmon")
#Mengatur posisi widget pada grid frame_DataBuku di window utama
frame_DataBuku.grid(row=1, column=0, padx=10, pady=10)

#Judul Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_judulBuku dimana pada label tersebut terletak pada Frame Data Buku dengan nama "Judul Buku :", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_judulBuku = Label(frame_DataBuku, text="Judul Buku :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_judulBuku di Frame Data Buku
label_judulBuku.grid(row=0, column=0, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_judulBuku dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_judulBuku =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_judulBuku di Frame Data Buku
entry_judulBuku.grid(row=0, column=1, padx=10, pady=10)

#Kode Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_tahunTerbit dimana pada label tersebut terletak pada Frame Data Buku dengan nama "Tahun Terbit :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_tahunTerbit = Label(frame_DataBuku, text="Tahun Terbit :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_tahunTerbit di Frame Data Buku
label_tahunTerbit.grid(row=1, column=0, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_tahunTerbit dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_tahunTerbit =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_tahunTerbit di Frame Data Buku
entry_tahunTerbit.grid(row=1, column=1, padx=10, pady=10)

#ISBN Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_ISBN dimana pada label tersebut terletak pada Frame Data Buku dengan nama "ISBN :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_ISBN = Label(frame_DataBuku, text="ISBN :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_ISBN di Frame Data Buku
label_ISBN.grid(row=2, column=0, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_ISBN dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_ISBN =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_ISBN di Frame Data Buku
entry_ISBN.grid(row=2, column=1, padx=10, pady=10)

#Pengarang Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_Pengarang dimana pada label tersebut terletak pada Frame Data Buku dengan nama "Pengarang :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_Pengarang = Label(frame_DataBuku, text="Pengarang :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_Pengarang di Frame Data Buku
label_Pengarang.grid(row=4, column=0, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_Pengarang dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_Pengarang =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_Pengarang di Frame Data Buku
entry_Pengarang.grid(row=4, column=1, padx=10, pady=10)

#Penerbit Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_Penerbit dimana pada label tersebut terletak pada Frame Data Buku dengan nama "Penerbit :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_Penerbit = Label(frame_DataBuku, text="Penerbit :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_Penerbit di Frame Data Buku
label_Penerbit.grid(row=5, column=0, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_Penerbit dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_Penerbit =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_Penerbit di Frame Data Buku
entry_Penerbit.grid(row=5, column=1, padx=10, pady=10)

#Rak Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_Rak dimana pada label tersebut terletak pada Frame Data Buku dengan nama "Rak Buku :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_Rak = Label(frame_DataBuku, text="Rak Buku :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_Rak di Frame Data Buku
label_Rak.grid(row=0, column=2, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_Rak dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_Rak =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_Rak di Frame Data Buku
entry_Rak.grid(row=0, column=3, padx=10, pady=10)

#Stok Buku
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_Stok dimana pada label tersebut terletak pada Frame Data Buku dengan nama "Stok Persediaan :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_Stok = Label(frame_DataBuku, text="Stok Persediaan :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_Stok di Frame Data Buku
label_Stok.grid(row=1, column=2, padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_Stok dimana pada entry tersebut terletak pada Frame Data Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_Stok =  Entry(frame_DataBuku, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_Stok di Frame Data Buku
entry_Stok.grid(row=1, column=3, padx=10, pady=10)

#Button Pilih
#Membuat sebuah button dengan nama variabel button_pilih dimana pada button tersebut terletak pada Frame Data Buku dengan nama "Pilih Data", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "grey", dengan fungsi pilih
button_pilih = Button(frame_DataBuku, text="Pilih Data", font=("Times New Roman", 17), bg="grey", command=pilih)
#Mengatur posisi widget pada grid button_pilih di Frame Data Buku
button_pilih.grid(row=2, rowspan=4, column=2, columnspan=2, padx=10, pady=10)

#Frame Pencarian
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_pencarian dimana pada Frame tersebut terletak pada window dengan nama labelnya "Pencarian Buku", dengan jenis font "Times New Roman", dengan ukuran 10 dengan background "salmon"
frame_pencarian = LabelFrame(window, text="Pencarian Buku", font=("Times New Roman", 10), bg="salmon")
#Mengatur posisi widget pada grid frame_pencarian di window utama
frame_pencarian.grid(row=1, column=1, sticky=S, padx=10, pady=10)

#Pencarian
#Membuat sebuah label untuk window utama GUI dengan nama variabel label_Pencarian dimana pada label tersebut terletak pada Frame Pencarian Buku dengan nama "Pencarian :"", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "salmon"
label_Pencarian = Label(frame_pencarian, text="Pencarian :", font=("Times New Roman", 12), bg="salmon")
#Mengatur posisi widget pada grid label_Pencarian di Frame Pencarian Buku
label_Pencarian.grid(row=0, column=0,  padx=5, pady=5)
#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel entry_Pencarian dimana pada entry tersebut terletak pada Frame Pencarian Buku dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 10 dengan panjang text 20
entry_Pencarian =  Entry(frame_pencarian, text="", font=('Times New Roman',10,'normal'), width=20)
#Mengatur posisi widget pada grid entry_Pencarian di Frame Pencarian Buku
entry_Pencarian.grid(row=0, column=1, padx=10, pady=10)

#Button Cari
#Membuat sebuah button dengan nama variabel button_cari dimana pada button tersebut terletak pada Frame Pencarian Buku dengan nama "Cari", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "grey", dengan fungsi cari
button_cari = Button(frame_pencarian, text="Cari", font=("Times New Roman", 17), bg="grey", command=cari)
#Mengatur posisi widget pada grid button_cari di Frame Pencarian Buku
button_cari.grid(row=0, column=3, padx=10, pady=10)

#Buat Tabel
#Membuat method bernama refreshTable untuk melakukan refreshTable data dan membuat tabel data buku pada GUI
def refreshTable():
    #Membuat perulangan for ketika user menekan button batal, maka akan menjalankan perintah for ini
    for data in my_table.get_children():
        #Menghaspus isi pada setiap entry di GUI ketika menekan button batal 
        my_table.delete(data)
        
    #Membuat perulangan for ketika data array di baca oleh method read, maka akan menjalankan perintah for ini
    for array in read():
        #Mengeset nilai tabel sama dengan nilai array 
        my_table.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    
    #Mengatur bentuk tabel, warna bacground tabel warna putih, dengan font Times New Roman dengan ukuran 12
    my_table.tag_configure('orow', background="#EEEEEE", font=("Times New Roman", 12))
    #Mengatur posisi widget pada grid my_table di window utama
    my_table.grid(row=2, columnspan=2, padx=10, pady=10)

#Membuat method bernama read untuk membaca data pada database
def read():
    #Mendeklarasikan variabel conn dengan nilai dari method connection
    conn = connection()
    #Mendeklarasikan variabel cursor dengan nilai dari method cursor
    cursor = conn.cursor()
    #Menjalankan request ke database untuk mencari data dalam database perpustakaan
    cursor.execute("SELECT * FROM perpustakaan")
    #Mendeklarasikan variabel result dengan nilai dari "cursor.fetchall()" 
    result = cursor.fetchall()
    #Melakukan request ke database dengan disimpan pada variabel conn
    conn.commit()
    #Menutup request setelah berhasil membaca data
    conn.close()
    #Memanggil kembali nilai variabel result
    return result

#Mendeklarasikan variabel conn dengan nilai dari ttk.Style()
style = ttk.Style()
#Mengatur setiap heading dari tabel dengan jenis font Times New Roman dengan ukuran 12
style.configure("Treeview.Heading", font=("Times New Roman", 12))
#Membuat sebuah kolom tabel dengan isi ("Kode Buku", "Judul Buku", "Tahun Terbit", "ISBN", "Pengarang", "Penerbit", "Rak Buku", "Stok Buku")
my_table['column'] = ("Kode Buku", "Judul Buku", "Tahun Terbit", "ISBN", "Pengarang", "Penerbit", "Rak Buku", "Stok Buku")

#Mengatur posisi kolom heading
my_table.column("#0", width=0, stretch=NO)
#Mengatur posisi kolom Kode Buku dengan lebar kolom 100
my_table.column("Kode Buku", anchor=W, width=100)
#Mengatur posisi kolom Judul Buku dengan lebar kolom 170
my_table.column("Judul Buku", anchor=W, width=170)
#Mengatur posisi kolom Tahun Terbit dengan lebar kolom 100
my_table.column("Tahun Terbit", anchor=W, width=100)
#Mengatur posisi kolom ISBN dengan lebar kolom 170
my_table.column("ISBN", anchor=W, width=170)
#Mengatur posisi kolom Pengarang dengan lebar kolom 170
my_table.column("Pengarang", anchor=W, width=170)
#Mengatur posisi kolom Penerbit dengan lebar kolom 170
my_table.column("Penerbit", anchor=W, width=170)
#Mengatur posisi Rak Kode Buku dengan lebar kolom 80
my_table.column("Rak Buku", anchor=W, width=80)
#Mengatur posisi kolom Stok Buku dengan lebar kolom 80
my_table.column("Stok Buku", anchor=W, width=80)

#Mengatur posisi heading kolom Kode Buku dengan text "Kode Buku"
my_table.heading("Kode Buku", text="Kode Buku", anchor=W)
#Mengatur posisi heading kolom Judul Buku dengan text "Judul Buku"
my_table.heading("Judul Buku", text="Judul Buku", anchor=W)
#Mengatur posisi heading kolom Tahun Terbit dengan text "Tahun Terbit"
my_table.heading("Tahun Terbit", text="Tahun Terbit", anchor=W)
#Mengatur posisi heading kolom ISBN dengan text "ISBN"
my_table.heading("ISBN", text="ISBN", anchor=W)
#Mengatur posisi heading kolom Pengarang dengan text "Pengarang"
my_table.heading("Pengarang", text="Pengarang", anchor=W)
#Mengatur posisi heading kolom Penerbit dengan text "Penerbit"
my_table.heading("Penerbit", text="Penerbeit", anchor=W)
#Mengatur posisi heading kolom Rak Buku dengan text "Rak Buku"
my_table.heading("Rak Buku", text="Rak Buku", anchor=W)
#Mengatur posisi heading kolom Stok Buku dengan text "Stok Buku"
my_table.heading("Stok Buku", text="Stok Buku", anchor=W)

#Melakukan refresh untuk GUI ketika mengklik tombol batal
refreshTable()

#Frame Button
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_button dimana pada Frame tersebut terletak pada window dengan nama labelnya "", dengan jenis font "Times New Roman", dengan background "salmon"
frame_button = LabelFrame(window, bg="salmon")
#Mengatur posisi widget pada grid frame_button di window utama
frame_button.grid(row=3, columnspan=2, padx=10, pady=10)

#Button Tambah
#Membuat sebuah button dengan nama variabel button_tambah dimana pada button tersebut terletak pada Frame Button dengan nama "Tambah", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "grey", dengan fungsi tambah
button_tambah = Button(frame_button, text="Tambah", font=("Times New Roman", 17), bg="grey", command=tambah)
#Mengatur posisi widget pada grid button_tambah di Frame Button
button_tambah.grid(row=0, column=0, padx=10, pady=10)

#Button Edit
#Membuat sebuah button dengan nama variabel button_edit dimana pada button tersebut terletak pada Frame Button dengan nama "Edit", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "grey", dengan fungsi edit
button_edit = Button(frame_button, text="Edit", font=("Times New Roman", 17), bg="grey", command=edit)
#Mengatur posisi widget pada grid button_edit di Frame Button
button_edit.grid(row=0, column=1, padx=10, pady=10)

#Button Hapus
#Membuat sebuah button dengan nama variabel button_hapus dimana pada button tersebut terletak pada Frame Button dengan nama "Hapus", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "grey", dengan fungsi hapus
button_hapus = Button(frame_button, text="Hapus", font=("Times New Roman", 17), bg="grey", command=hapus)
#Mengatur posisi widget pada grid button_hapus di Frame Button
button_hapus.grid(row=0, column=2, padx=10, pady=10)

#Button Batal
#Membuat sebuah button dengan nama variabel button_Batal dimana pada button tersebut terletak pada Frame Button dengan nama "Batal", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "grey", dengan fungsi batal
button_Batal = Button(frame_button, text="Batal", font=("Times New Roman", 17), bg="grey", command=batal)
#Mengatur posisi widget pada grid button_Batal di Frame Button
button_Batal.grid(row=0, column=3, padx=10, pady=10)

#Ada metode yang dikenal dengan nama mainloop() yang digunakan saat aplikasi Anda siap dijalankan yaitu mainloop() adalah infinite loop yang digunakan untuk menjalankan aplikasi, menunggu event terjadi dan memproses event tersebut selama window tidak ditutup
window.mainloop()