# Library
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Function
def choose():
    '''Fungsi untuk memilih bahasa stopwords'''
    while True:
        input_menu = input("Masukan pilihan anda di dengan menulis nomor yang terdapat di atas: ")
        if input_menu == "1":
            stop_word_set = set(stopwords.words("english"))
            break
        elif input_menu == "2":
            stop_word_set = set(stopwords.words("indonesian"))
            break
        else:
            print("Masukan input dengan benar! contoh(1/2)")
            
    return stop_word_set

def add_stopwords():
    '''Fungsi, opsi untuk menambahkan stopwords costume'''
    while True:
        new_stopwords = input("Mau menambahkan kata stopword baru? y/n: ").lower()
        
        if new_stopwords == "y":
            break
        elif new_stopwords == "n":
            break
        else:
            print("Masukan input dengan benar!")
    
    if new_stopwords == "y":
        add_text = input("Masukan kata baru dalam stopword dan pisahkan dengan tanda , (koma): ")
        stop_word_set.update(add_text.split(","))
        
    return stop_word_set

def save_file():
    '''Fungsi, opsi untuk menyimpan file hasil stopwords'''
    while True:
        new_save = input("\nMau menyimpan hasil stopwords? y/n: ").lower()
        
        if new_save == "y":
            break
        elif new_save == "n":
            break
        else:
            print("Masukan input dengan benar!")
    
    if new_save == "y":    
        with open("stopword_app/words.txt", "w") as file:
            file.write(str(text_word))
            
def finish_code():
    '''fungsi untuk konfirmasi finish code'''
    while True:
        user_confirmation = input("\nApakah sudah selesai? y/n: ").lower()
        if user_confirmation == "y":
            break
        elif user_confirmation == "n":
            break
        else:
            print("Masukan input dengan benar!")
    return user_confirmation

## download stopwords dulu kalau mau codenya bekerja, *hanya perlu sekali aja cukup. Contoh codenya di bawah
# nltk.download("stopwords")

# Variable
text_word = []

## Code inti / code core
while True:
    # Main menu
    print("""
===============================================
|              STOPWORDS REMOVER              |
===============================================
| Menghilangkan kata umum dan kata penghubung.|
| Hanya akan mengambil kata-kata yang bermakna|
| dan spesifik.                               |
===============================================
| 1. English (Bahasa Inggris)                 |
| 2. Indonesian (Bahasa Indonesia)            |
===============================================
        """)
    
    # Fungsi memilih bahasa dan menambah stopwords baru
    stop_word_set = choose()
    add_word = add_stopwords()
    
    # Input text yang nanti akan di hapus stopwordsnya
    text = input("Masukan teks: ")
    text_word_tokenizer = word_tokenize(text.lower())
    
    # Menmbuat data stopwords yang nanti akan digunakan untuk menghilanagkan stopwords pada variabel text
    data_stopword = [] # Variabel list untuk menyimpan semua stopwords yang di hasilkan dari input text
    for item in text_word_tokenizer:
        if item in stop_word_set:
            data_stopword.append(item)
    
    # Hasil text dan stopwordsnya sudah dihilangkan
    result = set(text_word_tokenizer)-set(data_stopword)
    
    # Menampilkan kata spesifik atau non stopwords
    print("\n","="*10,"KATA-KATA SPESIFIK","="*10,"\n")
    for index,item in enumerate(result, 1):
        text_word.append(item)
        print(f"{index}. {item}")
    
    # Menampilkan jumlah kata sebelum dan sesudah stopwords dihilangkan
    print("","="*10,"JUMLAH KATA SEBELUM & SESUDAH","="*10,"\n")
    print(f"Sebelum : {len(text_word_tokenizer)}")
    print(f"Sesudah : {len(text_word)}")
    
    # Memanggil fungsi untuk menyimpan file
    save_file()
    
    # Closing code
    confirm = finish_code()
    
    if confirm == "y":
        break
    else:
        continue

print("==========Program selesai!==========")