echo "part of the nohidy Framework"
echo"let the hunt begin"
cd
grep -r psloglist.exe
echo"lookin for openssh rootkit"
cd
cat /usr/include/log.h
shred /usr/include/log.h && rm -rf /usr/include/log.h
echo "lookin for case files"
cd && grep -r CASE && grep -r case
echo "going after jinx"
cd
grep -r jynx
cd /omgxochi && grep -r omgxochi
grep -r XxJynx
cd /XxJynx
grep -r ld.so.preload
echo "going after Azazel"
cd
cat /var/log/wtmp
grep -r azazel
grep -r crypthook
cat /etc/ld.so.preload
cat /var/run/utmp
echo "fetching a pub c azazel scanner"
wget http://pastebin.com/raw.php?i=hAV156Vt
mv raw.php?i=hAV156Vt azazel.c
gcc azazel.c -o azazelcompiled.c
./azazelcompiled.c
echo"havein a look at known ssh host"
cd
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}"  .ssh/known_hosts
echo"lookin for reverse tcp script"
cd
echo"bash"
grep -r "bash -i >&"
grep -r "exec /bin/bash"
grep -r "exec 5<>/dev/tcp/"
echo"perl"
grep -r "use Socket;$i="
grep -r "IO::Socket::INET"
echo"python"
grep -r "socket.AF_INET,socket.SOCK_STREAM"
grep -r "shell=True"
grep -r "subprocess.Popen(data,"
echo"php" 
grep -r "$sock=fsockopen"
echo"ruby"
grep -r "=TCPSocket"
echo"netcat"
grep -r "nc -r /bin/sh"
grep -r "/bin/sh -i 2>&1"
grep -r "nc -l -p"
grep -r "nc -lv"
grep -r "nc -c /bin/sh"
echo"java"
grep -r "Runtime.getRuntime"
grep -r "r.exec("
echo"xterm"
grep -r "xterm -display"
grep -r "Xnest :"
grep -r "xhost"
echo"commented out n stuff"
grep -r "targetip"
grep -r "attackerip"
grep -r "enter your ip here"
grep -r "port_bind"
echo "c"
grep -r "#include<sys/socket.h>"
grep -r "remote = connect(soc, (struct sockaddr*)"
grep -r "soc=socket"
grep -r "srv_addr.sin_port ="
echo "going after assembly reverse tcp script"
grep -r "push  byte 0x1"
grep -r "push  byte 0x2"
grep -r "mov   ecx,esp"
grep -r "inc   bl"
grep -r "mov   al,102"
grep -r "mov   bl,3  ; set bl to"
grep -r "push  byte  0x10"
grep -r "0x650A0A0A"
grep -r "mfspr 3,8"
grep -r "push word cx"
grep -r "inc ebx"
echo"goin against shellcode"
grep -r "\x66\x51\xb0\x3f\xcd\x80\x49\x79\xf9\x89\xe1\x6a\x10\x51\x53\x89\xe1\xb0"
grep -r "0x7CC63278, 0x2F867FFF, 0x41BC005C, 0x7C6802A6"
grep -r "\x31\xc0\x31\xdb\x31\xd2\xb0\x01\x89\xc6\xfe\xc0\x89\xc7\xb2"
grep -r "\x06\xb0\x29\x0f\x05\x93\x48\x31\xc0\x50\x68\x02\x01\x11\x5c"
grep -r "\xc6\xb0\x66\x31\xdb\xb3\x02\x68"
grep -r "\x31\xc0\x31\xdb\x31\xc9\x31\xd2"