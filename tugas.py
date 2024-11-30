data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A', 
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
         }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Menampilkan seluruh data
print("Seluruh data panen (nama lokasi dan hasil panen):")
for lokasi, data in data_panen.items():
    nama = data['nama_lokasi']
    hasil = data['hasil_panen']
    print(f"{nama} : Padi= {hasil['padi']}, Jagung= {hasil['jagung']}, Kedelai= {hasil['kedelai']}")

# 2. Menampilkan jumlah hasil panen jagung dari lokasi2
print("\nJumlah hasil panen jagung dari lokasi2:")
print(data_panen['lokasi2']['hasil_panen']['jagung'])

# 3. Menampilkan nama lokasi dari lokasi3
print("\nNama lokasi dari lokasi3:")
print(data_panen['lokasi3']['nama_lokasi'])

# 4 dan 5. Menampilkan jumlah hasil panen padi dan kedelai per lokasi
print("\nJumlah hasil panen per lokasi:")
for lokasi, data in data_panen.items():
    nama = data['nama_lokasi']
    padi = data['hasil_panen']['padi']
    kedelai = data['hasil_panen']['kedelai']
    print(f"{nama}: Padi = {padi}, Kedelai = {kedelai}")