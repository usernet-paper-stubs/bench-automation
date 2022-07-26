# vm1 to RDMA-09
# vm4 to RDMA-10

ssh RDMA-08 "./usernet-module/virsh-migrate.sh usernet-vm1 RDMA-07"

# start netserver
ssh usernet-vm1 "
sudo killall netserver
netserver -p 8864
"

sleep 1

# start netperf
ssh usernet-vm2 "netperf -H 172.16.1.101 -p 8864 -D 1 -l 100 -P 0 > netperf.result.txt" &

# sleep 50
sleep 50

# migration
ssh RDMA-07 -t 'bash -l -c "./usernet-module/virsh-migrate.sh usernet-vm1 RDMA-08"'

# attach
# ssh RDMA-10 "
# ./usernet-module/attach-ivshmem-doorbell.sh usernet-vm1
# ./usernet-module/attach-ivshmem-doorbell.sh usernet-vm4
# "

# modprobe & insmod
# ssh usernet-vm1 "sudo ./usernet-module/load-amd-driver.sh"
# ssh usernet-vm4 "sudo ./usernet-module/load-amd-driver.sh"

# sleep 50
sleep 50

# recovery
# ssh usernet-vm1 "sudo ./usernet-module/unload-amd-driver.sh"
# ssh usernet-vm4 "sudo ./usernet-module/unload-amd-driver.sh"
# ssh RDMA-10 "
# ./usernet-module/detach-ivshmem-doorbell.sh usernet-vm1
# ./usernet-module/detach-ivshmem-doorbell.sh usernet-vm4
# "
