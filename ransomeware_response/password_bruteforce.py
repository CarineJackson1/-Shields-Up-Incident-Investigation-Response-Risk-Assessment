import zipfile  

def try_password(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        return True  
    except:
        return False  

def main():
    print("Starting brute-force...")

    with zipfile.ZipFile('/Users/carinejackson/Downloads/EncryptedFilePack/enc.zip') as zf:
        with open('/Users/carinejackson/Downloads/EncryptedFilePack/rockyou.txt', 'r', errors='ignore') as pw_file:
            for line in pw_file:
                password = line.strip()  

                if try_password(zf, password):
                    print(f"[+] Password found: {password}")
                    return  
                else:
                    print(f"[-] Tried: {password}")

    print("[!] Password not found in the list.")

main()
