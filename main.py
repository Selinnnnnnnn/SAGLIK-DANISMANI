import math

print("=" * 45)
print(" KİŞİSEL SAĞLIK VE VKİ DANIŞMANI ".center(45, "*"))
print("=" * 45)

#1. GİRDİLERİN ALINMASI VE TEMİZLENMESİ
ad_soyad = input("Ad Soyad: ").strip().title()
cinsiyet = input("Cinsiyet (E/K): ").strip().upper()
yas = int(input("Yaş: "))
boy_cm = float(input("Boy (cm): "))
kilo_kg = float(input("Kilo (kg): "))

#2. HESAPLAMALAR VE MATEMATİKSEL İŞLEÇLER
boy_m = boy_cm / 100

# VKİ Formülü: Kilo / (Boy * Boy)  --> üs alma: boy_m ** 2
vki = kilo_kg / (boy_m ** 2)

# İdeal Kilo Aralığı (Standart VKİ aralığı 18.5 - 24.9 kabul edilir)
min_ideal_kilo = 18.5 * (boy_m ** 2)
max_ideal_kilo = 24.9 * (boy_m ** 2)

# Günlük Su İhtiyacı Hesabı (Kilo başına yaklaşık 0.035 Litre)
gunluk_su_litre = kilo_kg * 0.035

#3. KARAR YAPILARI (VKİ KATEGORİSİ VE RİSK ANALİZİ)
if vki < 18.5:
    kategori = "Zayıf"
    tavsiye = "Dengeli beslenme ile kilo almanız önerilir."
    fark_kilo = min_ideal_kilo - kilo_kg
    durum_mesaji = f"İdeal kilonun {fark_kilo:.1f} kg altındasınız."
elif 18.5 <= vki <= 24.9:
    kategori = "Normal (Sağlıklı)"
    tavsiye = "Tebrikler! Mevcut kilonuzu korumaya devam edin."
    durum_mesaji = "İdeal kilo aralığındasınız."
elif 25.0 <= vki <= 29.9:
    kategori = "Fazla Kilolu"
    tavsiye = "Düzenli yürüyüş ve hafif diyet önerilir."
    fark_kilo = kilo_kg - max_ideal_kilo
    durum_mesaji = f"İdeal kilonun {fark_kilo:.1f} kg üstündesiniz."
elif 30.0 <= vki <= 34.9:
    kategori = "1. Derece Obez"
    tavsiye = "Bir beslenme uzmanına danışmanız tavsiye edilir."
    fark_kilo = kilo_kg - max_ideal_kilo
    durum_mesaji = f"İdeal kilonun {fark_kilo:.1f} kg üstündesiniz."
else:
    kategori = "2./3. Derece İleri Obez"
    tavsiye = "Mutlaka tıbbi kontrol ve uzman desteği almalısınız."
    fark_kilo = kilo_kg - max_ideal_kilo
    durum_mesaji = f"İdeal kilonun {fark_kilo:.1f} kg üstündesiniz."

#4. HİZALANMIŞ SAĞLIK RAPORU (F-STRING BİÇİMLENDİRME)
print("\n" + "=" * 45)
print(" KİŞİSEL SAĞLIK KARNESİ ".center(45, "-"))
print("=" * 45)
print(f"Danışan          : {ad_soyad}")
print(f"Yaş / Cinsiyet   : {yas} yaş / {'Erkek' if cinsiyet == 'E' else 'Kadın'}")
print(f"Boy / Kilo       : {boy_cm:.0f} cm / {kilo_kg:.1f} kg")
print("-" * 45)
print(f"VKİ Değeri       : {vki:.2f} kg/m²")
print(f"Sağlık Kategorisi: {kategori}")
print(f"İdeal Kilo Aralığı: {min_ideal_kilo:.1f} kg - {max_ideal_kilo:.1f} kg")
print(f"Durum Analizi    : {durum_mesaji}")
print(f"Günlük Su Hedefi : {gunluk_su_litre:.2f} Litre ({math.ceil(gunluk_su_litre * 5)} bardak)")
print("-" * 45)
print(f"Öneri            : {tavsiye}")
print("=" * 45)
