#!/data/data/com.termux/files/usr/bin/bash
pkg install python requests git -y
git clone https://github.com/USERNAME/ANONYS-AUTO-EXPLOIT
cd ANONYS-AUTO-EXPLOIT
chmod +x main.sh
python -m pip install requests
./main.sh
