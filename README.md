<h1>Code Snippets</h1>

# Python

### A sample code
```python
#!/usr/bin/python
import sys
import os

if len(sys.argv) != 2:
        sys.stderr.write('Usage: ' + sys.argv[0] + ' <log-file-directory>\n')
        sys.exit(1)

file_path = sys.argv[1]

project_root  = "/home/" + "badri"

f = open(file_fragfold, 'r')
lines = f.readlines()
f.close()

for i in range(0,len(lines)):
	lines[i] = lines[i].strip()
	os.system(script + " " + file_in + " " + file_out)
	if (wt == 0):
		print(wt)
```
### Some hammers and screwdrivers
```
print(x.shape)
print(len(x))
print(x.ndim)
print(x.dtypes)
print(type(x))
```

### How to remotely access the Jupyter Notebook in prayog02?
#### In 1st Terminal start Jupyter service:
```bash
ssh user@prayog02.umsl.edu
pip install jupyter (if not installed)
jupyter notebook --no-browser --port=8892
OR
/home/user/.local/bin/jupyter-notebook --no-browser --port=8892
```
This will give a URL path; leave the terminal open.

#### In 2nd terminal Port forward (this is a local terminal; not server terminal)
* If you are using Windows follow [this](https://crl.ucsd.edu/handbook/vnc/index.php) instead
```
$ ssh -L 8892:127.0.0.1:8892 -N -f -l user prayog02.umsl.edu
```
Open the URL path in your local browser.

### How to allow GPU memory growth?
Add the following code at the beginning of your Python script or Notebook:  
```python
import keras.backend as K
gpu_options = tf.GPUOptions(allow_growth=True)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
K.tensorflow_backend.set_session(sess)
```  
### How to increase the display decimals (precision) of metrics in Keras?
* Change “1e-4” to “1e-9” in generic_utils.py (at two places) to increase the output precision
* Not sure if this impacts only the display but also the actual accuracy calculations.
```bash
vim /home/notebook/anaconda3/lib/python3.6/site-packages/keras/utils/generic_utils.py
EDIT: info += ' %.4f' % avg
```
### How to test GPU speed?
* Run [this code](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.1-introduction-to-convnets.ipynb)

### How to change plotsize in matplotlib?
```python
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = ((16,16))
plt.matshow(y, cmap='gray')
plt.show()
```
### How to confirm the dimensions of tensors?
```python
def abc(x, y):
   assert len(x.shape) == 2
   assert x.shape == y.shape
```

### How to find out which device GPU device tensorflow is using?
```python
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

### How to make remote folders accessible locally in Mac?
```bash
brew cask install osxfuse
brew install sshfs
sshfs badri@prayog02.umsl.edu:/data/PCP/ /Users/badriadhikari/prayog02.umsl.edu -ovolname=prayog02
```

# Linux
### How to connect to the prayog02 server?
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
pip install tensorflow-gpu==1.13.2 [If this does not work try - pip3 install tensorflow-gpu==1.13.2]
pip install keras
```
### How to backup (and push to background)?
* Open ssh terminal to remote server
* Begin scp transfer as usual.
* Background the scp process using `Ctrl+Z`, then the command `bg`
* Disown the backgrounded process using `disown`

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

### How to create a user in Ubuntu?
```bash
sudo useradd -m -d /home/badri badri
sudo passwd badri
sudo usermod -s /bin/bash $USERNAME
```

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

# Lewis Server
### Documentations
* [Main documentation](https://docs.rnet.missouri.edu)
* [Slurm tutorial](https://wiki.rc.hms.harvard.edu/display/O2/Using+Slurm+Basic)
* [Basic linux commands](http://docs.rnet.missouri.edu/Linux/basic-commands)

### What are the directories that I have access to?
`~, ~/data, ~/scratch, /group/prayog/, /storage/htc/prayog/`

### How to obtain a GPU terminal?
#### Option 1 (quick):
```
source /home/adhikarib/group-prayog/ba-lab/give-me-a-gpu-node.sh
source /home/adhikarib/group-prayog/ba-lab/keras.sh
```

#### Option 2 (detailed):
1. Connect
   ```
   ssh adhikarib@lewis.rnet.missouri.edu
   ```
2. Obtain any or specific GPU terminal (2 hour access):
   ```
   srun --mem 20G -p Gpu --gres gpu:1 --pty /bin/bash --login (for any GPU)
   srun --mem 20G -p Gpu --gres gpu:"Tesla V100-PCIE-32GB":1 --pty /bin/bash --login (for a specific GPU)
   ```
2. For two day access:
   ```
   srun --mem 20G -p gpu3 --account general-gpu --gres gpu:1 --pty /bin/bash --login
   ```
3. Activate Python environment:
   ```
   source /group/prayog/venvGPU/bin/activate (Python 2)
   module load cudnn/cudnn-7.1.4-cuda-9.0.176
   ```
#### Option 3 (Python3):
```bash
source /group/prayog/ba-lab/give-me-a-gpu-node.sh 
source /group/prayog/virt-env3.5/bin/activate
module load cudnn/cudnn-7.4.2-cuda-10.0.130
python3 /group/prayog/ba-lab/test-gpu.py
```

#### Test GPU speed
```
python --version
python /group/prayog/ba-lab/test-gpu.py
```
You should see GPU (not CPU) in the logs
   
### What are the GPUs available?
```
05 GB - lewis4-r730-gpu3-node426,gpu:Tesla K20Xm:1  
05 GB - lewis4-r730-gpu3-node428,gpu:Tesla K20Xm:1  
11 GB - lewis4-r730-gpu3-node429,gpu:Tesla K40m:1  
12 GB - lewis4-r730-gpu3-node430,gpu:Tesla K40m:1
05 GB - lewis4-r730-gpu3-node431,gpu:Tesla K20Xm:1
05 GB - lewis4-r730-gpu3-node432,gpu:Tesla K20Xm:1
05 GB - lewis4-r730-gpu3-node433,gpu:Tesla K20Xm:1
05 GB - lewis4-r730-gpu3-node434,gpu:Tesla K20Xm:1
05 GB - lewis4-r730-gpu3-node435,gpu:Tesla K20Xm:1
05 GB - lewis4-r730-gpu3-node476,gpu:Tesla K20Xm:1
12 GB - lewis4-r730-gpu3-node687,gpu:Tesla P100-PCIE-12GB:1
32 GB - Lewis4-r740xd-gpu4-node887,gpu:"Tesla V100-PCIE-32GB":?
32 GB - lewis4-r740xd-gpu4-node888,gpu:"Tesla V100-PCIE-32GB":? 
11 GB - lewis4-z10pg-gpu3-node598,gpu:GeForce GTX 1080 Ti:4
11 GB - lewis4-z10pg-gpu3-node599,gpu:GeForce GTX 1080 Ti:4
11 GB - lewis4-z10pg-gpu3-node601,gpu:GeForce GTX 1080 Ti:4
12 GB - lewis4-z10pg-gpu3-node600,gpu:GeForce GTX 1080 Ti:4
```
### How to run a non-GPU job in background?
#### Option 1:
```
sbatch --time 1-23:00 --partition Lewis --mem 20G "your script"
```
If it does not run after 5 minutes, you probably don't have two-day access!
#### Option 2:
```
sbatch /group/prayog/ba-lab/sbatch-Lewis.sh "python /group/prayog/ba-lab/test-gpu.py"
```
### How to check my jobs?
```
sacct
```
```
squeue -A adhikarib
```
```
squeue | grep 'GPU|gpu'
```

### How to know who is in my group?
```
getent group prayog-group
```

### How to lookup detailed partition information (number of nodes, etc.)
```
sinfo --long --partition=Lewis
sinfo --long --partition=Gpu
sinfo --long --partition=gpu3
```

### How to create a 'daddy' sbatch job?
```bash
#!/bin/bash
for pdb in `ls ./aln/*.aln`; 
   do
	id=$(basename $pdb)
	id=${id%.*}
	echo $id
	sbatch sbatch-Lewis.sh $id
   done
```

# Native R
Some references:
* http://research.stowers-institute.org/efg/R/Color/Chart/ColorChart.pdf
* http://rgraphics.limnology.wisc.edu/images/miscellaneous/pch.png
* http://research.stowers-institute.org/mcm/plotlayout.pdf

### A sample code
```R
setwd("~/Dropbox/manuscripts/conassess")
data <- read.table(“abc.txt”, skip = 1, header = T)
data$V7 <- abs(data$V1-data$V2)

for(i in 1:10) {
	print(usq[i])
}

all = read.table("jobs/14/feats/win-7_train.feat.txt", header = F)
cor(  all$V1, all$V598, method="pearson")
summary(all)
fileconn = file("results.txt")
writeLines(summary(all), fileconn)
close(fileconn)
```

### Computing correlation in R for two vectors a and b:
```R
coeff <- cor(a, b, method="spearman")
coeff <- cor(a, b, method="pearson")
```
### Replacing data values
```R
data$V7[data$V7 > 23] <- 200
```
### Subsetting data
```R
selection1 <- subset(alldata, EVAL == "TMSCORE")
chr1 <- data[which(data$V1 == 1),]
alldata <- subset(alldataoriginal, alldataoriginal$RMSD < 20.0)
```
### Combine data into a new table
```R
stage1 <- data.frame(tmscore = alldata$stage1_TM.score, stage = rep(c("stage1"), each = 150))
stage2 <- data.frame(tmscore = alldata$stage2_TM.score, stage = rep(c("stage2"), each = 150))
final  <- rbind(stage1, stage2)
```
### Set number of plots in one image, and adjust figure margins
```
par(mar=c(2,2,1,0.1))
```

### XY plot with selected columns
plot(data[, 'Dist'], data[, 'ENOE'])
lines(data[,'ENOE'],col='red',lty=3)

### Plot to file
```R
png(filename="C:/temp/name.png", height = 1600, width = 1600, res=300)
dev.off()
```

### XY plot with grouped data
```R
axis(1, at=1:5, labels=c("a","b","c","d","e"))
lines(trucks,col='red',lty=3) 
cars<-c(1,3,6,4,9) 
trucks <- c(2, 5, 4, 5, 12)
g_range <- range(0, cars, trucks) 
plot(cars, col="blue", type='l', ylim=g_range, xaxt='n')
axis(1, at=1:5, labels=c("a","b","c","d","e"))
lines(trucks,col='red',lty=3) 
```

### Quick box plot
```R
data <- read.table("/tmp/abc.txt", header=F)
hist(data$V1)
axis(1, seq(0, 600, by=100))
```

### Filled Density Plot
```R
d <- density(mtcars$mpg)
plot(d, main="Kernel Density of Miles Per Gallon")
polygon(d, col="red", border="blue")
```

### Tip: 
The actual values of variables are used only when the plots are actually printed. So, separate variables must be used for separate plots within same image!

# ggplot2

### A sample code
```R
require("ggplot2")
require("gridExtra")
alldata <- read.table(file="correlation.txt", header=T) 
png(filename = "correlation.png", width = 1000, height = 600, res=100)
plot1 <- ggplot(...) + …
plot2 <- ggplot(...) + ...
grid.arrange(plot1, plot2, ncol = 2)
dev.off()
```

### XY plot with grouped data
```R
ggplot(data = selection1, aes(selection1$ID, selection1$Correlation)) +
geom_point(aes(colour = factor(selection1$Measure))) +
geom_line(aes(colour = factor(selection1$Measure))) +
xlab("Selected Top Contacts") +
ylab("|Pearson correlation| with TM-score") +
```
### Replace the X-axis tick labels
```R
scale_x_discrete(labels = unique(selection1$TopxL)) + 
theme_bw() +
theme(legend.position = "top", legend.title=element_blank())
```

### Density plot
```R
pl1 <- ggplot(data, aes(x = data$TM_score, fill = data$method, linetype = data$method, colour = data$method)) +
geom_density(alpha = 0.2) +
xlab("TM-score") + ylab("Density of best models") +
scale_colour_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
scale_linetype_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
scale_fill_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
theme_bw() +
theme(legend.position = "top", legend.title=element_blank())
print(pl1)
```

### Bar diagrams
```
ggplot(alldata, aes(x = alldata$xL, y = alldata$contact_count, fill = alldata$stage)) +
	geom_bar(stat="identity", position=position_dodge(), colour = "black") +
	xlab("number of contacts (top-xL)") + ylab("number of best models (out of 150)") +
	theme_bw() +
	scale_x_continuous(breaks=c(0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2)) +
	theme(legend.position = "top", legend.title=element_blank())
```

### Box Plot
```R
pl1 <-	ggplot(feature.scores, aes(y = feature.scores$PrecisionL5, x = feature.scores$FeatureLabel, fill = feature.scores$FeatureLabel)) +
  geom_boxplot(aes(group = cut_width(feature.scores$FeatureLabel, 1)), alpha = 0.2, color = "darkgreen", outlier.size = 0) +
  xlab("Separation between two points") + ylab("Distance") +
  theme_bw() +
  theme(legend.position = "none", legend.title=element_blank()) +
  labs(title = "Chromosome3D")
```
