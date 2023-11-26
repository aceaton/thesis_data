# wget https://www.wireshark.org/download/src/wireshark-4.2.0.tar.xz -O /tmp/wireshark-4.2.0.tar.xz
# tar -xvf /tmp/wireshark-4.2.0.tar.xz
# cd wireshark-4.2.0

# sudo add-apt-repository universe

# sudo apt update && sudo apt dist-upgrade
# # sudo apt install qt6-base-dev
# sudo apt install cmake libglib2.0-dev libgcrypt20-dev flex yacc bison byacc \
#   libpcap-dev qtbase5-dev libssh-dev libsystemd-dev qtmultimedia5-dev \
#   libqt5svg5-dev qttools5-dev
# # sudo apt-get install libc-ares-dev 
# # sudo apt-get install libqt6core5compat6-dev
# # sudo apt-get install qttools5-dev
# # sudo apt-get install qconf qmake6 qmake6-bin
# cmake .
# make
# sudo make install
# c


# SCRIPT TO SET UP ENVIRONMENT TO RUN WIRESHARK AND SELENIUM

# ON UBUNTU 22.4
# get wireshark and tshark
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt install wireshark

# get pip
sudo apt install python3-pip

# sudo apt update 
# sudo apt install -y unzip xvfb libxi6 libgconf-2-4 

# get chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

# get chromedriver
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chromedriver-linux64.zip
unzip chromedriver_linux64.zip 

# get selenium
pip3 install selenium
pip3 install pyshark
pip3 install matplotlib

sudo chmod +x /usr/bin/dumpcap

sudo apt --fix-broken install
sudo apt install tshark

# get the interface to connect to
ifconfig