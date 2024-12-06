listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

for kota in listKota:
  print(kota)

  ## 0 sampai 4
for i in range(5):
  print("Perulangan ke -", i)

### mencari bilangan ganjil
for bilangan_ganjil in range(1,100,2):
  print(bilangan_ganjil)


  tuplebuah ='mangga','jeruk','apel','pepaya'

  for buah in tuplebuah:
    print(buah)

    listKota = [
  'selindung','gabek','bukit intan','air itam'
]

for kota in listKota:
  print(kota)
else:
  print('semua kota telah ditampilkan')

  listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listKota):
  # kita ubah katanya ke lowercase agar 
  # menjadi case insensitive
  if kota.lower() == kotaYangDicari.lower():
    print('Kota yang anda cari berada pada indeks', i)
    break
else:
  print('Maaf, kota yang anda cari tidak ada')