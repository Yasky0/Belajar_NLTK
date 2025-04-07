from nltk.stem import PorterStemmer, WordNetLemmatizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd

def choose():
    '''Fungsi untuk memilih bahasa stopwords'''
    while True:
        input_menu = input("Masukan pilihan anda di dengan menulis nomor yang terdapat di atas: ")
        if input_menu == "1":
            verbs = input("Masukan contoh english verbs untuk distemming. pisahkan dengan tanda , (koma): ").split(',')
            print(verbs)

            for item in verbs:
                porter.append(stemmer.stem(item))
                lemmi.append(lemmitizer.lemmatize(item, pos="v"))
            data = {
                "words": verbs,
                "porter": porter,
                "lemmitize": lemmi,
            }

            df = pd.DataFrame(data)
            break
        
        elif input_menu == "2":
            kata_kerja = input("Masukan contoh kata bahasa indonesia untuk distemming. pisahkan dengan tanda , (koma): ").split(',')
            for item in kata_kerja:
                sastra.append(sastrawi.stem(item))
            data = {
                "kata kerja": kata_kerja,
                "sastrawi": sastra
            }

            df = pd.DataFrame(data)
            break

        else:
            print("Masukan input dengan benar! contoh(1/2)")
            
    return df

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

porter = []
lemmi = []
sastra = []

stemmer = PorterStemmer()
lemmitizer = WordNetLemmatizer()
factory = StemmerFactory()
sastrawi = factory.create_stemmer()

## English verbs
# verbs = [
#     "running", "jumps", "played", "playing", "eats", "eating",
#     "driven", "driving", "walked", "walking", "flies", "flying",
#     "studied", "studying", "writes", "writing", "sings", "singing",
#     "danced", "dancing", "typed", "typing", "creates", "creating",
#     "coded", "coding", "reads", "reading", "solved", "solving",
#     "watched", "watching", "moved", "moving", "believed", "believing",
#     "hoped", "hoping", "loved", "loving", "worked", "working"
# ]

## Kata kerja bahasa Indonesia
# kata_kerja = [
# "menyanyikan", "berlari", "melompat", "memasak", "meminum", "menulis", "membaca",
#     "mengetik", "mengejar", "memukul", "menggambar", "mengangkat", "mencuci",
#     "mendorong", "mencari", "memancing", "mewarnai", "memanjat", "mengisi", "menggosok",
#     "mengupas", "menggiling", "menyapu", "menjahit", "menyalin", "mengolesi",
#     "membajak", "menyebarkan", "menyiapkan", "mewujudkan", "menyampaikan", "memecahkan",
#     "menyentuh", "menggenggam", "menyelesaikan", "memindahkan", "menghidupkan",
#     "mematikan", "mengembalikan", "memperbaiki", "mempelajari", "mengembangkan", "mengajarkan"
# ]

while True:
    # Main menu
    print("""
===============================================
|                  STEMMING                   |
===============================================
| Mengubah kata ke bentuk dasarnya (stem)     |
| dengan cara memotong akhiran atau imbuhan,  |
| tanpa memperhatikan apakah hasilnya adalah  |
| kata yang valid secara bahasa.              |
===============================================
| 1. English (Bahasa Inggris)                 |
| 2. Indonesian (Bahasa Indonesia)            |
===============================================
        """)
    
    hasil = choose()
    print(hasil)
    
    confirm = finish_code()
    
    if confirm == "y":
        break
    else:
        continue

print("==========Program selesai!==========")