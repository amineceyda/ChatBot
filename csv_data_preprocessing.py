import pandas as pd
from datetime import datetime, timedelta

def preprocess_data(csv_file_path):
    data = pd.read_csv(csv_file_path, encoding='utf-8')

    data.duplicated()
    #veri tipi dönüşümleri 
    data['UyeAktivasyonTarih'] = pd.to_datetime(data['UyeAktivasyonTarih'])
    data['IslemTarih'] = pd.to_datetime(data['IslemTarih'])
    data['SurumTarih'] = pd.to_datetime(data['SurumTarih'])
    data['IslemTutar'] = pd.to_numeric(data['IslemTutar'], errors='coerce')
    data['Tercih'] = data['Tercih'].astype(str)
    data['Versiyon'] = data['Versiyon'].astype(str)
    #Marka aynıysada yanlış girildiyse diye
    data['Marka'] = data['Marka'].str.strip()
    data['Marka'] = data['Marka'].str.lower()

    data['UyeAdres'] = data['UyeAdres'].str.replace(r'[^a-zA-Z0-9\s]', '')
    
    return data

csv_file_path = "hackathon_data.csv"
data = preprocess_data(csv_file_path)

##Veri Analizi 

# Veri setinin temel istatistiklerini görüntüleme
basic_stats = data.describe()
print(basic_stats)

# Belirli bir sütunun ortalama değerini almak
mean_value = data['IslemTutar'].mean()
print("Ortalama Değer:", mean_value)

#İşlem tipleri nelerdir
islem_tipleri = data['Tercih'].unique()

print("İşlem tipleri:")
for islem_tipi in islem_tipleri:
    print(islem_tipi)


#Üyelerin yüzde kaçı aktiftir?
aktif_uye_sayisi = len(data[data['UyeDurum'] == 'Aktif'])
toplam_uye_sayisi = len(data)
aktif_uye_yuzdesi = (aktif_uye_sayisi / toplam_uye_sayisi) * 100

print(f"Aktif Üyelerin Yüzdesi: {aktif_uye_yuzdesi:.2f}%")

#ilk işlem yapılan tarih ve son işlem yapılan tarih nedir?
data['IslemTarih'] = pd.to_datetime(data['IslemTarih'])

ilk_islem_tarihi = data['IslemTarih'].min()
son_islem_tarihi = data['IslemTarih'].max()

print(f"İlk İşlem Yapılan Tarih: {ilk_islem_tarihi}")
print(f"Son İşlem Yapılan Tarih: {son_islem_tarihi}")

#Toplam işlem sayısı nedir
toplam_islem_sayisi = data['IslemID'].nunique()

print(f"Toplam işlem sayısı: {toplam_islem_sayisi}")

#Son 10 günde kaç işlem gerçekleşti
data['IslemTarih'] = pd.to_datetime(data['IslemTarih'])
bugun = datetime.today()
on_gun_once = bugun - timedelta(days=10)
son_10_gun_islemleri = data[(data['IslemTarih'] >= on_gun_once) & (data['IslemTarih'] <= bugun)]
son_10_gun_islem_sayisi = len(son_10_gun_islemleri)

print(f"Son 10 günde gerçekleşen işlem sayısı: {son_10_gun_islem_sayisi}")


#Hangi işlem tipi en fazla gerçekleşmiştir?
islem_tipleri_sayisi = data['Tercih'].value_counts()
en_fazla_tekrarlanan_islem_tipi = islem_tipleri_sayisi.idxmax()
en_fazla_tekrar_sayisi = islem_tipleri_sayisi.max()

print(f"Hangi işlem tipi en fazla gerçekleşmiştir?")
print(f"'{en_fazla_tekrarlanan_islem_tipi}' işlem tipi {en_fazla_tekrar_sayisi} kez gerçekleştirilmiştir.")

#En yüksek işlem tutarı ne kadardır?
en_yuksek_islem_tutari = data['IslemTutar'].max()

print(f"En yüksek işlem tutarı ne kadardır?")
print(f"En yüksek işlem tutarı {en_yuksek_islem_tutari} TL'dir.")

#En düşük işlem tutarı ne kadardır?
en_dusuk_islem_tutari = data['IslemTutar'].min()

print(f"En düşük işlem tutarı ne kadardır?")
print(f"En düşük işlem tutarı {en_dusuk_islem_tutari} TL'dir.")

#Ortalama işlem tutarı nedir?
ortalama_islem_tutari = data['IslemTutar'].mean()

print("Ortalama işlem tutarı nedir?")
print(f"Ortalama işlem tutarı: {ortalama_islem_tutari:.2f} TL")

#Hangi şehirde en çok işlem yapılmıştır?
sehir_islem_sayilari = data['Sehir'].value_counts()

# En fazla işlem yapılan şehri belirleyin
en_fazla_islem_yapilan_sehir = sehir_islem_sayilari.idxmax()
en_fazla_islem_sayisi = sehir_islem_sayilari.max()

print("Hangi şehirde en çok işlem yapılmıştır?")
print(f"{en_fazla_islem_yapilan_sehir} şehrinde en fazla işlem yapılmıştır. ({en_fazla_islem_sayisi} işlem)")

#Hangi kullanıcı tipi en fazla işlem yapmıştır? saçma bir soru oldu neyse
kullanici_tipi_islem_sayilari = data['UyeDurum'].value_counts()
en_fazla_islem_yapan_kullanici_tipi = kullanici_tipi_islem_sayilari.idxmax()
en_fazla_islem_sayisi = kullanici_tipi_islem_sayilari.max()

print("Hangi kullanıcı tipi en fazla işlem yapmıştır?")
print(f"{en_fazla_islem_yapan_kullanici_tipi} kullanıcı tipi en fazla işlem yapmıştır. ({en_fazla_islem_sayisi} işlem)")

#Son 10 günde hangi marka en fazla işlem yapmıştır?
bugun = datetime.today()
baslangic_tarihi = bugun - timedelta(days=10)
son_10_gun_islemleri = data[data['IslemTarih'] >= baslangic_tarihi]
en_fazla_islem_yapan_marka = son_10_gun_islemleri['Marka'].value_counts().idxmax() if son_10_gun_islemleri['Marka'].any() else "Belirli Değer"
en_fazla_islem_sayisi = son_10_gun_islemleri['Marka'].value_counts().max()

print(f"Son 10 günde en fazla işlem yapan marka: {en_fazla_islem_yapan_marka}, Toplam işlem sayısı: {en_fazla_islem_sayisi}")

#Hangi saat diliminde en çok işlem gerçekleşmiştir?
data['IslemSaat'] = data['IslemTarih'].dt.hour
saat_dilimi_islemleri = data['IslemSaat'].value_counts()
en_fazla_islem_yapilan_saat = saat_dilimi_islemleri.idxmax()
en_fazla_islem_sayisi = saat_dilimi_islemleri.max()

print(f"En fazla işlem {en_fazla_islem_yapilan_saat}. saat diliminde gerçekleşmiştir. Toplam işlem sayısı: {en_fazla_islem_sayisi}")

#En fazla işlem yapan ilk 5 işyeri hangileridir?
en_fazla_islem_yapan_isyerleri = data['Marka'].value_counts()
ilk_5_isyeri = en_fazla_islem_yapan_isyerleri.head(5)

print("En fazla işlem yapan ilk 5 işyeri:")
print(ilk_5_isyeri)

#Son 5 günde hangi işlem tipi ile ne kadar işlem yapılmıştır?
end_date = datetime.today()
start_date = end_date - timedelta(days=5)
son_10_gun_islemleri = data[(data['IslemTarih'] >= start_date) & (data['IslemTarih'] <= end_date)]
gruplu_islemler = son_10_gun_islemleri.groupby('Tercih')
islemler_ve_tutarlar = gruplu_islemler.agg({'IslemID': 'count', 'IslemTutar': 'sum'})

print("Son 5 günde hangi işlem tipi ile ne kadar işlem yapılmıştır:")
print(islemler_ve_tutarlar)


#Belirli bir işlem türünün ortalama tutarı nedir?
ilgilenilen_islem_turu = "CeptePos"  # Değiştirmeniz gereken işlem türünü burada belirtin

filtrelenmis_veri = data[data['Tercih'] == ilgilenilen_islem_turu]

ortalama_tutar = filtrelenmis_veri['IslemTutar'].mean()

print(f"{ilgilenilen_islem_turu} işlem türünün ortalama tutarı: {ortalama_tutar:.2f}")

#Hangi kullanıcı en fazla işlem tutarı gerçekleştirmiştir?
kullanici_bazinda_islem_tutarlari = data.groupby('id')['IslemTutar'].sum()

en_yuksek_tutarli_kullanici = kullanici_bazinda_islem_tutarlari.idxmax()

print(f"En fazla işlem tutarına sahip kullanıcı ID'si: {en_yuksek_tutarli_kullanici}")
