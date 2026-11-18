# 🚀 Ultimate Auto-Decryptor & Hash Cracker

Bu araç; girilen şifreli metinlerin veya hash'lerin formatını (Base64, Hex, MD5, NTLM, SHA-1, SHA-256 vb.) otomatik olarak tespit eden ve uygun yöntemle çözen CLI tabanlı profesyonel bir Python aracıdır.

---

## 📌 Özellikler

* **Otomatik Format Tespiti:** Hex ve Base64 gibi kodlanmış metinleri wordlist'e ihtiyaç duymadan anında çözer.
* **Akıllı Hash Analizi:** Girilen hash'in karakter uzunluğuna ve yapısına bakarak olası algoritmaları otomatik belirler.
* **İnteraktif Mod:** Karmaşık parametre komutlarıyla uğraşmadan, doğrudan terminal üzerinden soru-cevap şeklinde hızlı kullanım sağlar.
* **Genişletilebilir Wordlist Desteği:** Kali Linux'un dahili `rockyou.txt` dosyasıyla tam uyumlu çalışır.

---

## ⚙️ Kurulum (Installation)

Projeyi Kali Linux sisteminize klonlamak ve çalıştırmak için şu adımları izleyin:

```bash
git clone [https://github.com/freudsec/auto-decryptor.git](https://github.com/freudsec/auto-decryptor.git)
cd auto-decryptor
🛠️ Kullanım (Usage)
Aracı başlatmak için terminalde proje klasörünün içindeyken şu komutu çalıştırın:
python3 auto_decryptor.py
Örnek Çalışma Akışı:
[*] İnteraktif Mod Aktif
[?] Çözülecek Hash veya Metni Girin: 21232f297a57a5a743894a0e4a801fc3
[?] Wordlist Yolu [Enter basarsan varsayılan rockyou]: 

[*] Hedef Analiz Ediliyor...
[+] Algoritma Tespit Edildi: MD5
[+] Şifre Başarıyla Çözüldü: admin
⚠️Yasal Uyarı (Disclaimer)
Bu araç yalnızca eğitim amaçları, siber güvenlik laboratuvarları ve yetkili sızma testleri için geliştirilmiştir. Sahibi olmadığınız veya açık izniniz bulunmayan sistemler üzerinde test yapmak yasal sorumluluk doğurur.
