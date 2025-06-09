# Türkçe Yazım Kontrol Kütüphanesi

Türkçe metinlerde yazım hatalarını tespit eden ve düzelten basit ama güçlü bir Python kütüphanesi.

## Özellikler

- Türkçeye özel yazım denetimi  
- Otomatik kelime önerileri  
- Büyük harf ve noktalama kuralları kontrolü  
- Kolay entegrasyon  
- CLI desteği  
- Web API olarak kullanılabilir  

## Kurulum

```bash
pip install turkyazim

## kullanım
from turkyazim import TurkceYazim

denetleyici = TurkceYazim()
sonuc = denetleyici.duzelt("Bu metin cok guzel degıl.")
print(sonuc)

CLI ile kullanım
turkyazim "Bu metin cok guzel degıl." --duzelt
