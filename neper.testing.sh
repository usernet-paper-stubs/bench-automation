
for i in {1..10}
do
  ssh usernet-vm1 ./neper/tcp_stream > $i.txt &
  sleep 1
  ssh usernet-vm4 ./neper/tcp_stream -c -H 172.16.1.101 -l 5 > /dev/null
  echo $i
done