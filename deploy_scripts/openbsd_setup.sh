echo 'setting up openbsd'

pkg_add -v gnupg-2.1.15p2 gmake privoxy dante wget libevent git
ln -sf /usr/local/bin/gpg2 /usr/local/bin/gpg
echo 'installing ToR'
mkdir tor 
cd tor 
echo 'make sure u update to the latest tor installation check out the latest one from https://dist.torproject.org/'
wget https://dist.torproject.org/tor-0.3.0.9.tar.gz.asc
gpg --verify tor-0.3.0.9.tar.gz.asc
wget https://dist.torproject.org/tor-0.3.0.9.tar.gz
tar -zxvf tor-0.3.0.9.tar.gz
cd tor-0.3.0.9/
./configure 
make
make install
cd ../
git clone https://git.torproject.org/torsocks.git
echo 'Tor is installed'
echo 'check out https://www.torproject.org/download/download-unix.html.en'

echo 'tor is installed here is another cool thing https://trac.torproject.org/projects/tor/wiki/doc/OpenbsdChrootedTor'
