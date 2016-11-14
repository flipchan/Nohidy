echo  'auto-scripting file that runs all kinds of scanner against target'


echo -n "Enter target ip or domain? "
read answer
$target = $answer
echo -n 'Enter wordlist for url bruteforce'
read answer
$wordlist = $answer

echo 'starting enumeration'
whois $target > whois.$target.log &
dig ANY $target > dig.$target.log
host $target > host.$target.log
fierce -dns $target > fierce.$target.log &
dirb $target $wordlist > dirb.$target.log &

echo 'starting vuln scanners'
golismero $target > golismero.$target.log &
nikto -h $target -C all > nikto.$target.log &





echo 'done'
