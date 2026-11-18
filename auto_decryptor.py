import hashlib
import base64
import argparse
import os
import sys

# Terminal renkleri
YESIL = '\033[92m'
SARI = '\033[93m'
KIRMIZI = '\033[91m'
MAVI = '\033[94m'
SIFIRLA = '\033[0m'

def banner():
    print(f"""{MAVI}
    =================================================
       ULTIMATE AUTO-DECRYPTOR & HASH CRACKER v3.0
    =================================================
    {SIFIRLA}""")

def encoding_kontrol(metin):
    try:
        if len(metin) % 2 == 0:
            cozulen_hex = bytes.fromhex(metin).decode('utf-8')
            if cozulen_hex.isprintable():
                print(f"{YESIL}[+] Format Bulundu (HEX): {cozulen_hex}{SIFIRLA}")
                return True
    except Exception:
        pass

    try:
        if len(metin) % 4 == 0:
            cozulen_b64 = base64.b64decode(metin).decode('utf-8')
            if cozulen_b64.isprintable():
                print(f"{YESIL}[+] Format Bulundu (Base64): {cozulen_b64}{SIFIRLA}")
                return True
    except Exception:
        pass

    return False

def hash_turu_belirle(hash_metni):
    uzunluk = len(hash_metni)
    turler = {
        32: ["md5", "ntlk" if False else "ntlm"],
        40: ["sha1"],
        56: ["sha224"],
        64: ["sha256"],
        96: ["sha384"],
        128: ["sha512"]
    }
    return turler.get(uzunluk, [])

def hash_kir(hedef_hash, wordlist_yolu, algoritmalar):
    if not os.path.exists(wordlist_yolu):
        print(f"{KIRMIZI}[-] Hata: '{wordlist_yolu}' dosyası bulunamadı!{SIFIRLA}")
        return

    print(f"{SARI}[*] Olası Algoritmalar taranıyor: {', '.join(algoritmalar).upper()}{SIFIRLA}")
    print(f"{SARI}[*] Wordlist taranıyor, lütfen bekleyin...{SIFIRLA}")

    hedef_hash = hedef_hash.lower()

    with open(wordlist_yolu, 'r', encoding='utf-8', errors='ignore') as dosya:
        for satir in dosya:
            kelime = satir.strip()
            if not kelime:
                continue

            for algo in algoritmalar:
                try:
                    if algo == "ntlm":
                        uretilen_hash = hashlib.new('md4', kelime.encode('utf-16le')).hexdigest()
                    else:
                        hash_objesi = hashlib.new(algo)
                        hash_objesi.update(kelime.encode('utf-8'))
                        uretilen_hash = hash_objesi.hexdigest()

                    if uretilen_hash == hedef_hash:
                        print(f"\n{YESIL}[+] BAŞARILI! Şifre Çözüldü!{SIFIRLA}")
                        print(f"{YESIL}[+] Algoritma : {algo.upper()}{SIFIRLA}")
                        print(f"{YESIL}[+] Şifre     : {kelime}{SIFIRLA}")
                        return
                except Exception:
                    continue

    print(f"\n{KIRMIZI}[-] Maalesef verilen wordlist içinde eşleşen bir şifre bulunamadı.{SIFIRLA}")

def main():
    banner()
    
    # Eğer komut satırından parametre verilmediyse interaktif moda geç
    if len(sys.argv) == 1:
        print(f"{SARI}[*] İnteraktif Mod Aktif{SIFIRLA}")
        hedef = input(f"{MAVI}[?] Çözülecek Hash veya Metni Girin: {SIFIRLA}").strip()
        
        # Wordlist'i sor, boş bırakırsa varsayılan rockyou'yu seç
        secilen_wordlist = input(f"{MAVI}[?] Wordlist Yolu [Enter basarsan varsayılan rockyou]: {SIFIRLA}").strip()
        if not secilen_wordlist:
            wordlist = "/usr/share/wordlists/rockyou.txt"
        else:
            wordlist = secilen_wordlist
    else:
        # Eski usul parametreli kullanım (istersen hala kullanabilirsin)
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", help="Çözülecek metin")
        parser.add_argument("-w", "--wordlist", default="/usr/share/wordlists/rockyou.txt", help="Wordlist yolu")
        args = parser.parse_args()
        hedef = args.target
        wordlist = args.wordlist

    if not hedef:
        print(f"{KIRMIZI}[-] Hedef boş bırakılamaz!{SIFIRLA}")
        return

    print(f"\n[*] Hedef Analiz Ediliyor: {hedef}\n")

    if encoding_kontrol(hedef):
        return

    olasi_algoritmalar = hash_turu_belirle(hedef)
    if not olasi_algoritmalar:
        print(f"{KIRMIZI}[-] Desteklenmeyen veya geçersiz hash uzunluğu ({len(hedef)} karakter).{SIFIRLA}")
        return

    hash_kir(hedef, wordlist, olasi_algoritmalar)

if __name__ == "__main__":
    main()
