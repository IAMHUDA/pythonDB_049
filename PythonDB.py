import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk


class NilaiSiswaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Nilai Siswa")
        self.root.geometry("540x1200")
        self.root.resizable(False, False)


        self.image_path = "bg4.jpeg"
        self.bg_image = Image.open(self.image_path)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)
        bg_label.pack()
        # Create a container (Frame) for entry widgets
        self.entry_container = tk.Frame(root, bg="#e3ff00")
        self.entry_container.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        entry_font = ("Helvetica", 16)
        entry_width = 20

        # Create entry widgets inside the container
        self.nama_label = tk.Label(self.entry_container, text="Nama Siswa", font=entry_font, bg="#e3ff00")
        self.nama_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,highlightthickness=7,highlightbackground="#00FFFF")

        self.biologi_label = tk.Label(self.entry_container, text="Biologi", font=entry_font, bg="#e3ff00")
        self.biologi_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,highlightbackground="#00FFFF",highlightthickness=7)

        self.fisika_label = tk.Label(self.entry_container, text="Fisika", font=entry_font, bg="#e3ff00")
        self.fisika_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,highlightbackground="#00FFFF",highlightthickness=7)

        self.inggris_label = tk.Label(self.entry_container, text="Inggris", font=entry_font, bg="#e3ff00")
        self.inggris_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,highlightbackground="#00FFFF",highlightthickness=7)

        # Place entry widgets inside the container
        label_y = 0
        entry_y = 1
        for label, entry in zip([self.nama_label, self.biologi_label, self.fisika_label, self.inggris_label],
                                [self.nama_entry, self.biologi_entry, self.fisika_entry, self.inggris_entry]):
            label.grid(row=label_y, column=0, pady=5)
            entry.grid(row=entry_y, column=0, pady=5)
            label_y += 2
            entry_y += 2

        # Create Submit button with shadow
        button_font = ("Helvetica", 14)
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_nilai,
                                       font=button_font, bg="blue", fg="white", bd=0, padx=10, pady=3,  # Mengurangi nilai pady
                                       relief=tk.GROOVE, cursor="hand2")
        self.submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Start background color animation

    def submit_nilai(self):
        # Ambil nilai dari entry widgets
        nama_siswa = self.nama_entry.get()
        nilai_biologi = int(self.biologi_entry.get())
        nilai_fisika = int(self.fisika_entry.get())
        nilai_inggris = int(self.inggris_entry.get())

        # Tentukan prediksi_fakultas berdasarkan nilai tertinggi
        if nilai_biologi >= nilai_fisika and nilai_biologi >=nilai_inggris:
            prediksi_fakultas = "Kedokteran"
        elif nilai_fisika >= nilai_biologi and nilai_fisika >=nilai_inggris:
            prediksi_fakultas = "Teknik"
        elif nilai_inggris >= nilai_fisika and nilai_inggris >= nilai_biologi:
            prediksi_fakultas = "Bahasa"

        # Simpan data ke database
        conn = sqlite3.connect("NilaiSiswa.db")
        cursor = conn.cursor()
        
        """cursor.execute('''
            CREATE TABLE NilaiSiswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT,
                biologi INTEGER,
                fisika INTEGER,
                inggris INTEGER,
                prediksi_fakultas TEXT
            )
        ''')
        """
        cursor.execute('''
            INSERT INTO NilaiSiswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))

        conn.commit()
        conn.close()

        # Tampilkan popup hasil prediksi
        messagebox.showinfo("Hasil Prediksi", f"Prediksi Fakultas: {prediksi_fakultas}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NilaiSiswaApp(root)
    root.mainloop()
