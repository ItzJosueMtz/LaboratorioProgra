touch temp.txt
ifconfig >> temp.txt
hostname >> temp.txt
curl ifconfig.me >> temp.txt
nmap 192.168.1.* >> temp.txt
echo "1er nmap"
nmap -sP 192.168.1.0/25 >> temp.txt
echo "2do nmap"
nmap 192.168.1.255 >> temp.txt
echo "3er nmap"
nmap --script http-headers scanme.nmap.org >> temp.txt
echo "4to nmap"
touch PracticaNmap.txt
base64 temp.txt > PracticaNmap.txt
rm temp.txt
echo "Finalizado"
