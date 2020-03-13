Disk overview:
Device     Boot     Start        End    Sectors   Size Id Type
/dev/sda1  *         2048    3905535    3903488   1.9G 83 Linux
/dev/sda2         3905536  179687423  175781888  83.8G 83 Linux
/dev/sda3       179687424  195311615   15624192   7.5G 82 Linux swap / Solaris
/dev/sda4       195311616 1953523711 1758212096 838.4G 83 Linux

I reserved a large partition sda4 for LVM.

> sudo fdisk /dev/sda4
command 't': change partition type
command '8e': type is Linux LVM

> w


sudo pvcreate /dev/sda4

sudo vgcreate vgx /dev/sda4

sudo lvcreate -n lvx -L 5g vgx

sudo mkfs.ext4 /dev/vgx/lvx

sudo mount /dev/vgx/lvx /mnt/lvx/

sudo lvextend -L +1g vgx/lvx

sudo resize2fs /dev/vgx/lvx

