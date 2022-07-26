ssh RDMA-09 -t 'bash -l -c "./usernet-module/virsh-migrate.sh usernet-vm4 RDMA-10"'

# start netserver
ssh usernet-vm3 "
sudo killall netserver
netserver -p 8864
"

sleep 1

# start netperf
ssh usernet-vm4 "netperf -H 172.16.1.103 -p 8864 -D 1 -l 100 -P 0 > netperf.result.txt &"

# sleep 50
sleep 50

# migration
ssh RDMA-10 -t 'bash -l -c "./usernet-module/virsh-migrate.sh usernet-vm4 RDMA-09"'

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
