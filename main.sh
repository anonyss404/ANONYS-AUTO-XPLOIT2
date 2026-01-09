#!/data/data/com.termux/files/usr/bin/bash

# --- CONFIG SERVER ---
DB_URL="https://raw.githubusercontent.com/anonyss404/ANONYS-V2/main/server/database_key.txt"

clear
echo -e "\033[1;36m======================================\033[0m"
echo -e "\033[1;33m      ANONYS AUTO-EXPLOIT V1          \033[0m"
echo -e "\033[1;36m======================================\033[0m"
echo -n -e "\033[1;32mENTER SERIAL KEY: \033[0m"
read INPUT_KEY
USER_KEY=$(echo $INPUT_KEY | tr -d ' ')

echo -e "\033[1;34m[*] Verifikasi Lisensi...\033[0m"
GET_DATA=$(curl -sL "$DB_URL" | grep "^$USER_KEY|")

if [[ -n "$GET_DATA" ]]; then
    echo -e "\033[1;32m[✓] ACCESS GRANTED!\033[0m"
    sleep 1
    clear
    echo -e "\033[1;33m--- ADMIN FINDER & AUTO EXPLOIT ---\033[0m"
    echo -n -e "\033[1;32mMasukkan URL Target: \033[0m"
    read TARGET
    
    # Jalankan Mesin Python
    python engine.py $TARGET
else
    echo -e "\033[1;31m[✘] KEY TIDAK VALID!\033[0m"
fi
