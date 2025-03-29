from nltk import word_tokenize, sent_tokenize
import json

def fungsi_word(input_teks):
    '''Fungsi Untuk Tokenisasi Kata'''
    word = word_tokenize(input_teks)
    
    print("\n","="*10,"KATA","="*10,)
    for index,kata in enumerate(word, 1):
        print(f"{index}. {kata}")
        
    return word
    
def fungsi_sent(input_teks):
    '''Fungsi Untuk Tokenisasi Kalimat'''
    sent = sent_tokenize(input_teks)
    
    print("\n","="*10,"KALIMAT","="*10)
    for index, kalimat in enumerate(sent, 1):
        print(f"{index}. {kalimat}")
        
    return sent

while True:
    print("""
===============================================
|                TOKENIZER APP                |
===============================================
| Mentokenisasai teks menjadi beberapa bagian |
| Termasuk kata dan kalimat.                  |
| pilih mode tokenisasi yang ada dibawah ini! |
===============================================
| 0. Tokenizer (Tokenisasi Semua)             |
| 1. Word Tokenizer (Tokenisasi Kata)         |
| 2. Sentence Tokenizer (Tokenisasi Kalimat)  |
===============================================
""")
    input_teks = input("Masukan Teks: ")
    while True:
        input_menu = input("Masukan pilihan anda di dengan menulis nomor yang terdapat di atas: ")
    
        if input_menu == "1":
            word = fungsi_word(input_teks)
            tokenizer = {
                "Kata":word
            }
            break
        elif input_menu == "2":
            sent = fungsi_sent(input_teks)
            tokenizer = {
                "Kalimat":sent
            }
            break
        else:
            print("Masukan input dengan benar! contoh(1/2)")
    
    with open("tokenizer.json", "w") as file:
        json.dump(tokenizer, file, indent=4)
    
    while True:
        user_confirmation = input("\nApakah sudah selesai? y/n: ").lower()
        if user_confirmation == "y":
            break
        elif user_confirmation == "n":
            break
        else:
            print("Masukan input dengan benar!")
    
    if user_confirmation == "y":
        break
    else:
        continue

print("Program selesai!")