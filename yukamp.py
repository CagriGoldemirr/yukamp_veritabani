# -*- coding: utf-8 -*-

class Dugum:
    def __init__(self, üye_numarası, ad, soyad, malzeme, tarih):
        self.üye_numarası = üye_numarası
        self.ad = ad
        self.soyad = soyad
        self.malzeme = malzeme
        self.tarih = tarih
        self.sol = None
        self.sag = None // BOS DEGER 


class ÜyeAgaci:
    def __init__(self):
        self.kök = None

    def üye_ekle(self, üye_numarası, ad, soyad, malzeme, tarih):
        if self.kök is None:
            self.kök = Dugum(üye_numarası, ad, soyad, malzeme, tarih)
        else:
            self._üye_ekle(self.kök, üye_numarası, ad, soyad, malzeme, tarih)

    def _üye_ekle(self, mevcut, üye_numarası, ad, soyad, malzeme, tarih):
        if üye_numarası < mevcut.üye_numarası:
            if mevcut.sol is None:
                mevcut.sol = Dugum(üye_numarası, ad, soyad, malzeme, tarih)
            else:
                self._üye_ekle(mevcut.sol, üye_numarası, ad, soyad, malzeme, tarih)
        elif üye_numarası > mevcut.üye_numarası:
            if mevcut.sag is None:
                mevcut.sag = Dugum(üye_numarası, ad, soyad, malzeme, tarih)
            else:
                self._üye_ekle(mevcut.sag, üye_numarası, ad, soyad, malzeme, tarih)

    def üye_bul(self, üye_numarası):
        return self._üye_bul(self.kök, üye_numarası)

    def _üye_bul(self, mevcut, üye_numarası):
        if mevcut is None:
            return None
        if üye_numarası == mevcut.üye_numarası:
            return mevcut
        elif üye_numarası < mevcut.üye_numarası:
            return self._üye_bul(mevcut.sol, üye_numarası)
        else:
            return self._üye_bul(mevcut.sag, üye_numarası)

    def tüm_üyeleri_göster(self, mevcut):
        if mevcut:
            self.tüm_üyeleri_göster(mevcut.sol)
            print(f"Üye Numarası: {mevcut.üye_numarası}, Ad: {mevcut.ad}, Soyad: {mevcut.soyad}, "
                  f"Malzeme: {mevcut.malzeme}, Tarih: {mevcut.tarih}")
            self.tüm_üyeleri_göster(mevcut.sag)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, etkinlik):
        self.stack.append(etkinlik)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack boş!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack boş!"

    def is_empty(self):
        return len(self.stack) == 0

    def göster(self):
        if self.is_empty():
            print("Stack boş!")
        else:

            for etkinlik in reversed(self.stack):
                print(etkinlik)


def kullanıcı_bilgilerini_al():
    üye_numarası = int(input("Üye numarasını giriniz: "))
    ad = input("Üyenin adını giriniz: ")
    soyad = input("Üyenin soyadını giriniz: ")
    return üye_numarası, ad, soyad


def malzeme_bilgilerini_al():
    malzeme = input("Üyeye verilecek malzeme: ")
    tarih = input("Malzemenin alındığı tarihi giriniz (GÜN/AY/YIL): ")
    return malzeme, tarih


def Main():
    print("YUKAMP MALZEME ARAYÜZÜNE HOŞGELDİNİZ")

    ağaç = ÜyeAgaci()
    etkinlik_stack = Stack()

    while True:
        print("\n--- Dağcılık Kulübü Veritabanı ---")
        print("1. Etkinliğe üye ekle")
        print("2. Bir üyenin bilgilerini görüntüle")
        print("3. Tüm üyeleri görüntüle")
        print("4. Çıkış")
        print("5. Etkinlik ekle (Stack)")
        print("6. Tüm etkinlikleri listele")

        seçim = input("Bir işlem seçin (1/2/3/4/5/6): ")

        if seçim == "1":
            üye_numarası, ad, soyad = kullanıcı_bilgilerini_al()
            malzeme, tarih = malzeme_bilgilerini_al()
            ağaç.üye_ekle(üye_numarası, ad, soyad, malzeme, tarih)
        elif seçim == "2":
            üye_numarası = int(input("Görüntülemek istediğiniz üye numarasını girin: "))
            üye = ağaç.üye_bul(üye_numarası)
            if üye:
                print(f"Üye Numarası: {üye.üye_numarası}, Ad: {üye.ad}, Soyad: {üye.soyad}, "
                      f"Malzeme: {üye.malzeme}, Tarih: {üye.tarih}")
            else:
                print("Üye bulunamadı.")
        elif seçim == "3":
            print("\nTüm Üyeler:")
            ağaç.tüm_üyeleri_göster(ağaç.kök)
        elif seçim == "4":
            print("Arayüzden çıkılıyor...")
            break
        elif seçim == "5":
            etkinlik = input("Eklemek istediğiniz etkinlik adını ve etkinliğin yapılma tarihini (GÜN/AY/YIL) giriniz: ")
            etkinlik_stack.push(etkinlik)
            print("Etkinlik eklendi.")
        elif seçim == "6":
            print("\nTüm Etkinlikler:")
            etkinlik_stack.göster()
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")


if __name__ == "__main__":
    Main()
