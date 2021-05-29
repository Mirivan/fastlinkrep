#!/usr/bin/bash
# shellcheck shell=bash
if [ $EUID -ne 0 ]; then
   echo "This script must be run as root"; exit 1
else
   echo "Prepairing..."
   cd ~
   if ping -c 1 github.com &> /dev/null; then
      echo "Server working stability!"
   else
      echo "Server doesn't work, exiting..."
      exit 1
   fi
   echo "Installing requirements..."
   apt update; apt install git make unzip wget libnl-3-dev libnl-genl-3-dev  libssl-dev python-is-python2 hostapd-mana hostapd-wpe -y
   wget http://ftp.br.debian.org/debian/pool/main/d/dnspython/python-dnspython_1.16.0-1_all.deb; dpkg -i python-dnspython_1.16.0-1_all.deb; rm python-dnspython_1.16.0-1_all.deb
   wget http://ftp.br.debian.org/debian/pool/main/s/scapy/python-scapy_2.4.0-2_all.deb; dpkg -i python-scapy_2.4.0-2_all.deb; rm python-scapy_2.4.0-2_all.deb
   wget http://ftp.br.debian.org/debian/pool/main/p/pcapy/python-pcapy_0.10.8-1+b1_arm64.deb; dpkg -i python-pcapy_0.10.8-1+b1_arm64.deb; rm python-pcapy_0.10.8-1+b1_arm64.deb
   clear
   echo "Downloading mana-shs..."
   wget https://github.com/Mirivan/fastlinkrep/raw/main/mana-toolkit-shs.zip
   clear
   echo "Installing mana-shs..."
   mv mana-toolkit-shs.zip /usr/bin/
   cd /usr/bin; unzip mana-toolkit-shs.zip
   chmod 755 dumpmifare.sh
   chmod 755 start-mana-bdf-kitkat
   chmod 755 start-mana-bdf-lollipop
   chmod 755 start-mana-full-kitkat
   chmod 755 start-mana-full-lollipop
   chmod 755 start-mana-simple-kitkat
   chmod 755 start-mana-simple-lollipop
   chmod 755 start-update.sh
   chmod 755 stop-mana-kitkat
   chmod 755 stop-mana-lollipop
   chmod 755 stop-wlan1.sh
   cd ~; clear
   echo "Prepairing for mana-toolkit..."
   git clone --depth 1 https://github.com/Mirivan/mana
   cd mana
   git clone --depth 1 https://github.com/sensepost/hostapd-mana
   git clone --depth 1 https://github.com/DanMcInerney/net-creds
   cd sslstrip-hsts
   git clone --depth 1  https://github.com/singe/dns2proxy
   git clone --depth 1 https://github.com/singe/sslstrip2
   cd ..
   clear; ./kali-install.sh
   echo "Successfully installed. Cleaning..."
   cd ~
   rm -rf mana
fi