######### ÖDEV 2 ###########

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

def ekleme(ogrenciListesi): 
    isim = input("Lütfen eklemek istediğiniz öğrencinin adı ve soyadını giriniz: ")
    if isim != []:
        ogrenciListesi.append(isim)
        b = input("İşlem başarılı. Devam etmek için lütfen bir tuşa basınız.")
    else:
        b = input("Lütfen geçerli bir isim giriniz. Ana menüye dönmek için lütfen bir tuşa basınız.")

def cikartma(ogrenciListesi):
    isim = input("Lütfen listeden çıkarmak istediğiniz öğrencinin adını ve soyadını giriniz: ")
    if ogrenciListesi.count(isim):
        ogrenciListesi.remove(isim)
        b = input("İşlem başarılı. Devam etmek için lütfen bir tuşa basınız.")
    else:
        b = input("İşlem yapılamadı. Lütfen listede olan bir öğrenci ismi giriniz. Ana sayfaya dönmek için lütfen bir tuşa basınız.")   

def topluEkleme(ogrenciListesi):
    sayi = input("Lütfen listeye eklemek istediğiniz öğrenci sayısını giriniz: ")
    p = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
    liste = []
    if p.count(sayi) > 0:
        sayi = int(sayi)
        for i in range(sayi):
            isim = input("Eklemek istediğiniz öğrencinin adı ve soyadını giriniz: ")
            if isim == "":
                b = input("Lütfen geçerli bir isim giriniz.")
            else:
                liste.append(isim)
                print("{}. öğtenci eklendi.".format(i+1))
        ogrenciListesi.extend(liste)
        b = input("İşlem başarılı. Ana menüye dönmek için bir tuşa basınız.")  
    else:
        b = input("Geçersiz sayı girdiniz. Ana menüye dönmek için bir tuşa basınız.")

def ekran(ogrenciListesi):
    if len(ogrenciListesi) > 0:
        for i in range(len(ogrenciListesi)):
            print("{} - {}".format(i+1,ogrenciListesi[i]))
        b = input("Ana menüye dönmek için lütfen bir tuşa basınız.")
    else:
        b = input("Öğrenci listesi boş. Ana menüye dönmek için bir tuşa basınız.")

def numaraOgrenme(ogrenciListesi):
    u = (input("Lütfen numarasını öğrenmek istediğiniz öğrenciyi giriniz: "))
    if ogrenciListesi.count(u) != 0:
        for i in range(len(ogrenciListesi)):
            if ogrenciListesi[i] == u:
                print("İlgili öğrencinin numarası: {}".format(i+1))
    else: 
        print("İsmini girdiğiniz öğrenci listede bulunmamaktadır.")
    b = input("Devam etmek için lütfen bir tuşa basınız.")

def topluCikartma(ogrenciListesi):
    a = len(ogrenciListesi)
    p = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
    sayi = (input("Lütfen listeden çıkarmak istediğiniz öğrenci sayısını giriniz: "))
    liste = []
    m = 0
    if p.count(sayi) > 0:
        sayi = int(sayi)
        for i in range(sayi):
            if len(ogrenciListesi) - i > 0:
                o = input("Çıkartmak istediğiniz öğrencinin adı ve soyadını giriniz: ")
                if  ogrenciListesi.count(o) > 0:
                    liste.append(o)
                    print("{}. öğrenci çıkartıldı.".format(i+1))
                else:
                    print("İlgili öğrencinin kaydı sistemde yoktur.")
            else:
                b = input("Listede öğrenci kalmadığı için daha fazla öğrenci ismi giremezsiniz. Devam etmek için bir tuşa basınız.")   
    else:
        print("Geçersiz sayı girdiniz.")
    for i in range(len(liste)):
        ogrenciListesi.remove(liste[i])
    b = input("Ana menüye dönmek için bir tuşa basınız.")  


ogrenciListesi = ["Ahmet Işık","Uğurcan Yanık", "Veli Ahmet Bayraktar", "Mahmut Çakar", "Yaren Çılbır", "Eda Aksoy", "Sibel Can", "Ömer Dağar", "Ayşe Irmak"]
input("Öğrenci Veritabanına Hoşgelidiniz. Lütfen devam etmek için bir tuşa basınız.")
a = " Listeye Öğtenci Eklemek İçin Lütfen '1' tuşuna basınız. \n Listeden belirli bir öğrenciyi çıkarmak için lütfen '2' tuşuna basınız. \n Listeye birden fazla öğrenci eklemek için lütfen '3' tuşuna basınız. \n Öğrenci listesini görmek için lütfen '4' tuşuna basınız. \n Belirli bir öğrencinin okul numarasını görmek için lütfen '5' tuşuna basınız. \n Listeden birden fazla öğrenciyi silmek için lütfen '6' tuşuna basınız. \n Programdan çıkmak için lütfen 'e' tuşuna basınız."
x = []
while True:
    if x == "e":
        print("İyi günler...")
        break
    print("******************************************************")
    print(a)
    x = input("")
    print("******************************************************")

    while True:
        if x == "1":
            ekleme(ogrenciListesi)
            break
        
        elif x == "2":
            cikartma(ogrenciListesi)
            break
        
        elif x == "3":
            topluEkleme(ogrenciListesi)
            break
        
        elif x == "4":
            ekran(ogrenciListesi)
            break

        elif x == "5":
            numaraOgrenme(ogrenciListesi)
            break

        elif x == "6":
            topluCikartma(ogrenciListesi)
            break
    
        elif x == "e":
            break
    
        else:
            print("Lütfen geçerli bir tuşa basınız.")
            break