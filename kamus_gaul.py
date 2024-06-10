# Kamu-kata-gaul
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": " menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah",
            }
word = input('masukkan kata gaul: ')
if word.upper() in meme_dict.keys():
    print(meme_dict[word.upper()])
else:
    print('error!')
