matn = input("Biror matn kiriting: ").lower()

toza_matn = matn.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
sozlar = toza_matn.split()

if sozlar:
    eng_kop = max(set(sozlar), key=sozlar.count)
    print(f"Jami so‘zlar soni: {len(sozlar)}")
    print(f"Eng ko‘p uchragan so‘z: '{eng_kop}' ({sozlar.count(eng_kop)} marta)")
else:
    print("Hech qanday so‘z topilmadi.")
