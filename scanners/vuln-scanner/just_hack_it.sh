echo  'auto-scripting file that runs all kinds of scanner against target'


echo -n "Enter target ip or domain? "
read answer
$target = $answer

echo 'starting'
golismero $target > golismero.log &
nikto -h $target -C all > nikto.log &
