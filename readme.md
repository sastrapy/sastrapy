# Sastrapy
Sastrapy adalah pengolah teks sederhana untuk Bahasa Indonesia. Sastrapy berisi beberapa metode seperti slang converter, tokenize, stopword remover, dan kami berharap di masa depan Sastrapy memiliki fungsi stemming.

## Tujuan pembuatan
Tujuan pembuatan dari library Sastrapy adalah berangkat dari kebutuhan dalam text processing dalam Bahasa Indonesia yang semakin hari bahasa yang digunakan di tengah masyarakat semakin beragam. Munculnya istilah baru, singkatan baru, dan gaya penulisan baru membuat sebuah library text processing harus beradaptasi. Di sini Sastrapy berusaha untuk memberikan kemudahan dalam adaptasi tersebut.

## Instalasi
Untuk memasang Sastrapy, silahkan gunakan perintah di bawah ini
```
pip install Sastrapy
```
atau lebih lengkapnya seperti di bawah ini
```
python3 -m pip install Sastrapy
```

## Pengunaan
Ada tiga fitur di versi terakhir dari Sastrapy, ketiga fitur tersebut adalah sebagai berikut
#### Tokenize
Fitur ini untuk membuat token dari string atau kata yang dimasukan. Penggunaannya seperti di bawah ini
```py
from Sastrapy.WordTokenize.Tokenize import tokenize

result = tokenize('Aku sangat merindukan dirimu')
print(result) # ['Aku', 'sangat', 'merindukan', 'dirimu']
```
#### Stopword remover
Fitur ini untuk membersihkan kalimat dari kata yang tidak berelasi atau yang disebut dengan stopword. Penggunaannya seperti di bawah ini
```py
from Sastrapy.Corpus.StopwordRemover import StopwordRemoverMachine

machine = StopwordRemoverMachine()
result = machine.removeStopword('Aku sangat merindukan dirimu')
print(result) # merindukan

# Jika data yang dimasukan adalah dalam bentuk list,
# hasil yang diberikan juga dalam bentuk list
result = machine.removeStopword(['Aku', 'sangat', 'merindukan', 'dirimu'])
print(result) # ['merindukan']

# Kamu juga bisa mengubah kamus stopword
# dengan kamus kamu sendiri (dalam format txt)
# Tulis kode di bawah sebelum melakukan removeStopword()
machine.importDictionary('path/to/stopword_dictionary.txt')

# Atau kamu ingin mereset kamus kembali seperti semula. 
# Maka akan menggunakan kamus default
machine.resetDictionary()
```

#### Slang converter
Fitur ini digunakan untuk merubah kata slang atau singkatan ke dalam bentuk yang ditentukan. Penggunaannya seperti di bawah ini
```py
from Sastrapy.Corpus.SlangConverter import SlangConverterMachine

machine = SlangConverterMachine()
result = machine.convertSlang('Aku mmg sngt rindu km')
print(result) # saya memang sangat rindu kamu

# Jika data yang dimasukan adalah dalam bentuk list,
# hasil yang diberikan juga dalam bentuk list
result = machine.convertSlang(['Aku', 'mmg', 'sngt', 'rindu', 'km'])
print(result) # ['saya', 'memang', 'sangat', 'rindu', 'kamu']

# Kamu juga bisa mengubah kamus slang
# dengan kamus kamu sendiri (dalam format txt)
# Tulis kode di bawah sebelum melakukan convertSlang()
machine.importDictionary('path/to/slang_dictionary.txt')

# Atau kamu ingin mereset kamus kembali seperti semula. 
# Maka akan menggunakan kamus default
machine.resetDictionary()
```
## Pengembangan
Pengembangan akan terus dilakukan untuk beradaptasi dengan bahasa yang ada
