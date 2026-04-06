import string
import random


def sifre_uret(uzunluk):
    havuz = string.ascii_lowercase + string.digits

    sifre = "".join(random.choices(havuz, k = uzunluk))
    return sifre


print("*********************************************")
print("*        ŞİFRE OLUŞTURMA PROGRAMINA           *")
print(("*                HOŞ GELDİNİZ                 *"))
print("*********************************************")

print("Bu program senin için kırılması zor değil imkansız olan, güvenli şifreler üretir.")

devam_etsin_mi = True

while devam_etsin_mi:
    karakter_sayisi = int(input("Şifreniz kaç karakter olsun? : "))

    yeni_sifre = sifre_uret(karakter_sayisi)

    print(f"İşte yeni şifren: {sifre_uret(karakter_sayisi)}")


    cevap = input("Yeni bir şifre oluşturmak ister misiniz ? (Evet / Hayır) : ")

    if cevap == "Evet" or cevap == "evet":
        print("Tamamdır, baştan şifre oluşturuluyor!")
    else:
        print("Programdan çıkılıyor, İyi günler dileriz...")

        devam_etsin_mi = False






