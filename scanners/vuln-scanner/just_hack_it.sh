echo  'auto-scripting file that runs all kinds of scanner against target'


echo -n "Enter target ip or domain? "
read answer
$target = $answer

echo 'starting enumeration'
whois $target
fierce -dns $target

echo 'starting vuln scanners'
golismero $target > golismero.log &
nikto -h $target -C all > nikto.log &
