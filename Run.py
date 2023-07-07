import datetime
import platform
import marshal
import zlib
import base64
import binascii
import os
from cryptography.fernet import Fernet

# Logo
logo = '''
╔═╗┬ ┬   ╦  ╦┌─┐┬─┐┬┌─┐┌┐ ┬  ┌─┐
╠═╝└┬┘───╚╗╔╝├─┤├┬┘│├─┤├┴┐│  ├┤ 
╩   ┴     ╚╝ ┴ ┴┴└─┴┴ ┴└─┘┴─┘└─┘
'''

# Pilihan untuk membaca tutorial
read_tutorial = input("Apakah Anda ingin membaca tutorial untuk menggunakan script ini? (y/t): ")

if read_tutorial.lower() == "y":
    # Menampilkan langkah-langkah/tutorial penggunaan skrip Python
    print("===== Tutorial =====")
    print("Langkah-langkah penggunaan script Python:")
    print("[1]. Jalankan script Python ini.")
    print("[2]. Ikuti instruksi yang ditampilkan pada layar.")
    print("[3]. Masukkan path file input.")
    print("[4]. Masukkan path file output.")
    print("[5]. Tunggu hingga proses encrypt selesai.")
    print("[6]. File output yang terenkripsi akan tersimpan di path yang telah Anda tentukan.")
    print("====================")

# Meminta input file path
print(logo)
input_file = input("Masukkan path file input: ")

# Meminta output file 
output_file = input("Masukkan path file output: ")

# Jumlah iterasi enkripsi
num_iterations = 44

# Fungsi untuk mengenkripsi file
def encrypt_file():
    current_time = datetime.datetime.now()
    encrypted_code = f'# You Cant Bypass My Codes Security\n' \
                     f'# Time : {current_time}\n' \
                     f'# Platform : {platform.platform()}\n' \
                     f'# Obfuscate By Ferly Afriliyan >_<\n\n'    \
                     f'#\n\n'   \
                     f'# __File__       = "Py3-Variable ; Encryptions File Python3"\n'   \
                     f'# __instagram__  = "www.instagram.com/afriliyanferlly_shishigami"\n\n'   \
                     f'#\n\n'   \
                     f'# __website__    = "https://ferlyafriliyan.vercel.app/"\n'  \
                     f'# __github__     = "https://github.com/ferlyafriliyan/Py3-Variable"\n\n\n'   \
                     f'# Dont Change My Code >_<\n\n'   \

    encrypted_code += f'Ferly_XV4 = [\n'
    for _ in range(3500):
        encrypted_code += f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n'
    encrypted_code += f']\n\n'

    encrypted_code += f'License_XV4 = [\n'
    for _ in range(444):
        encrypted_code += f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n'
    encrypted_code += f']\n\n'

    # Baca kode dari file input
    with open(input_file, 'r', encoding='utf-8') as file:
        code = file.read()

    # Enkripsi kode sebanyak iterasi yang ditentukan
    for _ in range(num_iterations):
        # Enkripsi kode menggunakan marshal, zlib, dan base64
        encrypted_data = base64.b64encode(zlib.compress(marshal.dumps(code.encode()))).decode()

        # Generate kunci acak untuk enkripsi Fernet
        key = Fernet.generate_key()
        fernet = Fernet(key)

        # Enkripsi kunci menggunakan marshal, zlib, dan base64
        encrypted_key = base64.b64encode(zlib.compress(marshal.dumps(key))).decode()

        # Enkripsi data menggunakan Fernet
        encrypted_data = fernet.encrypt(encrypted_data.encode()).decode()

        # Tulis kode terenkripsi ke file output
        with open(output_file, 'w') as file:
            file.write(encrypted_code)
            file.write(f'import marshal\n')
            file.write(f'import zlib\n')
            file.write(f'import base64\n')
            file.write(f'import binascii\n')
            file.write(f'encrypted_key = "{encrypted_key}"\n')
            file.write(f'decrypted_key = marshal.loads(zlib.decompress(base64.b64decode(encrypted_key)))\n')
            file.write(f'encrypted_data = "{encrypted_data}"\n')
            file.write(f'decrypted_data = Fernet(decrypted_key).decrypt(encrypted_data.encode()).decode()\n')
            file.write(f'exec(marshal.loads(zlib.decompress(base64.b64decode(decrypted_data))))\n\n')
            file.write(f'Afriliyan_XV4 = [\n')
            for _ in range(3500):
                file.write(f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
            file.write(f']\n\n')

# Panggil fungsi untuk mengenkripsi file
encrypt_file()
