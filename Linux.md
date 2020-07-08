# Linux
### How to connect to the prayog servers?
1. Connect to UMSL VPN 
1. `ssh: user@prayog02.umsl.edu`
1. Setup your environment (after first login):
   Add the following lines to your ~/.bashrc file
   ```bash
   export PATH=$PATH:/usr/local/cuda-10.0/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
   ```
1. Install the following  
```bash
pip3 install tensorflow-gpu [If this does not work try - pip3 install tensorflow-gpu==1.13.2]
pip3 install keras
pip install tensorflow-gpu [If this does not work try - pip3 install tensorflow-gpu==1.13.2]
pip install keras
```

---
### How to backup (and push to background)?
* Open ssh terminal to remote server
* Begin scp transfer as usual.
* Background the scp process using `Ctrl+Z`, then the command `bg`
* Disown the backgrounded process using `disown`

---
### How to setup VNC viewer using Mac/Ubuntu to access?
#### Start VNC server in the server with your account
Run the following commands or create a script with the following content:
```bash
vncserver -kill :1
vncserver -kill :2
vncserver -kill :3
vncserver -kill :4
rm -rf /tmp/.X*
vncserver -geometry 1600x1200
```
This will show a log file in the screen that will have the port where vnc server is running.
#### In 2nd terminal Port forward (this is a local terminal; not server terminal)
* If you are using Windows follow [this](https://crl.ucsd.edu/handbook/vnc/index.php) instead
```
$ ssh -L 8892:127.0.0.1:5901 -N -f -l user prayog02.umsl.edu
```
#### Connect to server
```
open vnc://localhost:5901 (for mac client)
$ vncviewer localhost:5901 (for Ubuntu client)
```

---
### How to create a user in Ubuntu?
```bash
sudo useradd -m -d /home/badri badri
sudo passwd badri
sudo usermod -s /bin/bash $USERNAME
```

---
### How to make vim interface more informative?
Change default VIM settings:
```bash
$ vim ~/.vimrc 
syntax on
filetype indent plugin on
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
:color desert
:set number
```

---
### How to add a new HDD/SDD?
```bash
df -h
ls /dev/
sudo fdisk /dev/sdd
sudo mkfs.ext4 /dev/sdd
sudo mkdir /mysdd
sudo mount /dev/sdc2 /mysdd
sudo vim /etc/fstab
```
```bash
#device        mountpoint             fstype    options  dump   fsck
/dev/sdb1    /home/yourname/mydata    ext4    defaults    0    1
```

---
### Some frequently used linux commands
```bash
Update Bash prompt [update ~/.bashrc and ~/.bash_profile]
export PS1='$(whoami)@$(hostname):$(pwd)'
export HISTSIZE=100000
```
Check disk usage summary for each folder sorted by size
```bash
du -hs /home/bap54/* | sort -h
```
Recursive Grep
```bash
grep -r sspro4 /home/projects/
```
Find and delete
```bash
find ./project69/ -name dg_sa.log -exec rm -f {} \;
```
Check Memory (RAM)
```bash
free -g
```
Tar and then Gzip
```bash
tar zcvf abc.tar.gz ./abc
```
Untar and then Gunzip
```bash
tar zxvf abc.tar.gz
```
Zip
```bash
zip -r abc.zip ./abc
```
CPU architecture and Number of CPU
```bash
lscpu
```
Bulk Rename
```bash
rename ‘Tp’ ‘Ts’ Tp*
```
Column Count
```bash
head -1 win-7_train.feat.txt | tr '\t' '\n' | wc -l
```
Keep Column 1 to 596
```bash
cut -d' ' -f1-596 win-7_valid.feat.txt
```
DOS2UNIX Command alternative
```bash
sed -i 's/\r//' filename to convert dos2unix line endings
```
Fix the log file with backspace and other characters:
```bash
col -bp < train-2017-02-26.log > xx.log
```

