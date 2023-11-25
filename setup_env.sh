wget https://www.wireshark.org/download/src/wireshark-4.2.0.tar.xz -O /tmp/wireshark-4.2.0.tar.xz
tar -xvf /tmp/wireshark-4.2.0.tar.xz
cd wireshark-4.2.0

sudo add-apt-repository universe

sudo apt update && sudo apt dist-upgrade
# sudo apt install qt6-base-dev
sudo apt install cmake libglib2.0-dev libgcrypt20-dev flex yacc bison byacc \
  libpcap-dev qtbase5-dev libssh-dev libsystemd-dev qtmultimedia5-dev \
  libqt5svg5-dev qttools5-dev
# sudo apt-get install libc-ares-dev 
# sudo apt-get install libqt6core5compat6-dev
# sudo apt-get install qttools5-dev
# sudo apt-get install qconf qmake6 qmake6-bin
cmake .
make
sudo make install
c