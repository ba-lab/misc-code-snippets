# Code Snippets

## Python

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

### How to making remote folders accessible locally in Mac?
```bash
brew cask install osxfuse
brew install sshfs
sshfs badri@prayog02.umsl.edu:/data/PCP/ /Users/badriadhikari/prayog02.umsl.edu -ovolname=prayog02
```

## Linux
### How to setup VNC viewer using Mac/Ubuntu to access?
#### Start VNC server in the server with a useraccount
$ vncserver -kill :1
$ vncserver -kill :2
$ vncserver -kill :3
$ vncserver -kill :4
$ sudo rm -rf /tmp/.X*
$ vncserver -geometry 1200x800
Alternately simply run the following script which has all the commands
$ ./restart-vnc-server.sh
In a local machine’s terminal port forward (the exact port number can increase/decrease based on port availability)
Connect to UMSL VPN
$ ssh -L 5901:127.0.0.1:5901 -N -f -l notebook prayog01.hcp.umsl.edu [password is notebook2733]
In the same local terminal, open the vnc viewer and supply password (notebook)
$ open vnc://localhost:5901 (for mac client) [same password]
$ vncviewer localhost:5901 (for Ubuntu client)

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

### Some frequently used linux commands
```bash
Update Bash prompt [update ~/.bashrc and ~/.bash_profile]
export PS1='$(whoami)@$(hostname):$(pwd)'
export HISTSIZE=100000

Check disk usage summary for each folder sorted by size
du -hs /home/bap54/* | sort -h

Recursive Grep
grep -r sspro4 /home/projects/

Find and delete
find ./project69/ -name dg_sa.log -exec rm -f {} \;

For loop syntax
for i in {1..23}; do nohup ./build_models_HD.pl test $i & done
export p=4; for i in {0..5}; do echo p$p$i; sort -k3 p$p$i/results.txt | tail -5 | head -4 ; done

Check Memory (RAM)
free -g

Tar and then Gzip
tar zcvf abc.tar.gz ./abc

Untar and then Gunzip
tar zxvf abc.tar.gz

Zip 
zip -r abc.zip ./abc

CPU architecture and Number of CPU
lscpu

Bulk Rename
rename ‘Tp’ ‘Ts’ Tp*

Column Count
head -1 win-7_train.feat.txt | tr '\t' '\n' | wc -l

Keep Column 1 to 596
cut -d' ' -f1-596 win-7_valid.feat.txt

DOS2UNIX Command alternative
sed -i 's/\r//' filename to convert dos2unix line endings

Fix the log file with backspace and other characters:
col -bp < train-2017-02-26.log > xx.log
```

## Server Access

# Lewis Server
* [Documentation](https://docs.rnet.missouri.edu)

How to Connect to Lewis GPU?
ssh adhikarib@lewis.rnet.missouri.edu
srun --mem 20G -p Gpu --gres gpu:1 --pty /bin/bash --login
srun --mem 20G -p Gpu --gres gpu:"Tesla V100-PCIE-32GB":1 --pty /bin/bash --login
source ~/tensorflow_from_source/tensorflow_virtual_env/bin/activate
module load cuda/cuda-8.0
module load cudnn/cudnn-6.0-cuda-8.0

Two day GPU access test:
srun --mem 20G -p gpu3 --account general-gpu --gres gpu:1 --pty /bin/bash --login

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

Run a job in background
$ sbatch --time 1-23:00 --partition Lewis --mem 20G /storage/htc/prayog/contact.pl /storage/htc/prayog/NP_001341437.1.fasta
- the default time limit for Lewis partition is two days so --time may not be needed
  		$ sinfo --long --partition=Lewis
- the default partition is not Lewis so the job is terminated earlier

Lewis Related
Slurm Tutorial
https://wiki.rc.hms.harvard.edu/display/O2/Using+Slurm+Basic 
Space Limitation Informations
~, ~/data, ~/scratch, /group/prayog/, /storage/htc/prayog, 
Basic Linux commands
http://docs.rnet.missouri.edu/Linux/basic-commands 
Find who is in the group?
$ getent group prayog-group

How to setup GPU access for a new user?
Install
$ virtualenv ~/aug-30 (Reference: http://docs.rnet.missouri.edu/Software/python_virtualenv)
$ source ~/aug-30/bin/activate
$ pip install --upgrade pip
$ pip install tensorflow-gpu==1.9.0 (Reference: http://docs.rnet.missouri.edu/Software/tensorflow)
$ pip install keras
$ deactivate
Test
$ srun --mem 20G -p Gpu --gres gpu:1 --pty /bin/bash --login
$ source ~/aug-30/bin/activate
$ module load cuda/cuda-9.0.176
$ module load cudnn/cudnn-7.1.4-cuda-9.0.176
$ python /group/prayog/test-gpu.py

from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils import to_categorical
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.summary()
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
model.compile(optimizer='rmsprop',
          	loss='categorical_crossentropy',
          	metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch_size=64)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("")
print(test_acc)

To use only a part of the GPU memory (never has to use, but just in case)
import tensorflow as tf
pu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)

Find out which device Tensorflow is currently using:
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


Python and Deep Learning
----------
>>> train_images.shape
(60000, 28, 28)
>>> len

>>> train_labels


>>> train_lables.ndim

>>> print(train_lables.dtype)

>>> import matplotlib.pyplot as plt
>>> plt.imshow(digit, cmap = plt.cm.binary)
>>> plt.show()

def abc(x, y):
   assert len(x.shape) == 2
   assert x.shape == y.shape

train_data, train_labels
y, y_pred 







----------------------------------------------------------------------------------------------------------------
Native R
----------------------------------------------------------------------------------------------------------------

http://research.stowers-institute.org/efg/R/Color/Chart/ColorChart.pdf
http://rgraphics.limnology.wisc.edu/images/miscellaneous/pch.png
http://research.stowers-institute.org/mcm/plotlayout.pdf

setwd("~/Dropbox/manuscripts/conassess")
data <- read.table(“abc.txt”, skip = 1, header = T)
data$V7 <- abs(data$V1-data$V2)
# Computing correlation in R for two vectors a and b:
coeff <- cor(a, b, method="spearman")
coeff <- cor(a, b, method="pearson")
# Replacing data values
data$V7[data$V7 > 23] <- 200
# subsetting data
selection1 <- subset(alldata, EVAL == "TMSCORE")
chr1 <- data[which(data$V1 == 1),]
alldata <- subset(alldataoriginal, alldataoriginal$RMSD < 20.0)
# Combine data into a new table
stage1 <- data.frame(tmscore = alldata$stage1_TM.score, stage = rep(c("stage1"), each = 150))
stage2 <- data.frame(tmscore = alldata$stage2_TM.score, stage = rep(c("stage2"), each = 150))
final  <- rbind(stage1, stage2)
# Figure margins
par(mar=c(2,2,1,0.1))
# Number of plots in one image
par(mfrow=c(2,2))

# XY plot with selected columns
plot(data[, 'Dist'], data[, 'ENOE'])
lines(data[,'ENOE'],col='red',lty=3)

png(filename="C:/temp/name.png", height = 1600, width = 1600, res=300)
dev.off()

# XY plot with grouped data
axis(1, at=1:5, labels=c("a","b","c","d","e"))
lines(trucks,col='red',lty=3) 
cars<-c(1,3,6,4,9) 
trucks <- c(2, 5, 4, 5, 12)
g_range <- range(0, cars, trucks) 
plot(cars, col="blue", type='l', ylim=g_range, xaxt='n')
axis(1, at=1:5, labels=c("a","b","c","d","e"))
lines(trucks,col='red',lty=3) 

# Quick box plot
data <- read.table("/tmp/abc.txt", header=F)
hist(data$V1)
axis(1, seq(0, 600, by=100))
R
# Filled Density Plot
d <- density(mtcars$mpg)
plot(d, main="Kernel Density of Miles Per Gallon")
polygon(d, col="red", border="blue")

Tips: 
“The actual values of variables are used only when the plots are actually printed. So, separate variables must be used for separate plots within same image!”

for(i in 1:10) {
	print(usq[i])
}

all = read.table("jobs/14/feats/win-7_train.feat.txt", header = F)
cor(  all$V1, all$V598, method="pearson")
summary(all)
fileconn = file("results.txt")
writeLines(summary(all), fileconn)
close(fileconn)
----------------------------------------------------------------------------------------------------------------
ggplot2
----------------------------------------------------------------------------------------------------------------
# An example
require("ggplot2")
require("gridExtra")
alldata <- read.table(file="correlation.txt", header=T) 
png(filename = "correlation.png", width = 1000, height = 600, res=100)
plot1 <- ggplot(...) + …
plot2 <- ggplot(...) + ...
grid.arrange(plot1, plot2, ncol = 2)
dev.off()

# XY plot with grouped data
ggplot(data = selection1, aes(selection1$ID, selection1$Correlation)) +
geom_point(aes(colour = factor(selection1$Measure))) +
geom_line(aes(colour = factor(selection1$Measure))) +
xlab("Selected Top Contacts") +
ylab("|Pearson correlation| with TM-score") +
# Replace the X-axis tick labels with these
scale_x_discrete(labels = unique(selection1$TopxL)) + 
theme_bw() +
theme(legend.position = "top", legend.title=element_blank())


	
# Density plot
pl1 <- ggplot(data, aes(x = data$TM_score, fill = data$method, linetype = data$method, colour = data$method)) +
geom_density(alpha = 0.2) +
xlab("TM-score") + ylab("Density of best models") +
scale_colour_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
scale_linetype_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
scale_fill_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
theme_bw() +
theme(legend.position = "top", legend.title=element_blank())
print(pl1)

# Bar diagrams
ggplot(alldata, aes(x = alldata$xL, y = alldata$contact_count, fill = alldata$stage)) +
	geom_bar(stat="identity", position=position_dodge(), colour = "black") +
	xlab("number of contacts (top-xL)") + ylab("number of best models (out of 150)") +
	theme_bw() +
	scale_x_continuous(breaks=c(0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2)) +
	theme(legend.position = "top", legend.title=element_blank())


# Box Plot
pl1 <-	ggplot(feature.scores, aes(y = feature.scores$PrecisionL5, x = feature.scores$FeatureLabel, fill = feature.scores$FeatureLabel)) +
  geom_boxplot(aes(group = cut_width(feature.scores$FeatureLabel, 1)), alpha = 0.2, color = "darkgreen", outlier.size = 0) +
  xlab("Separation between two points") + ylab("Distance") +
  theme_bw() +
  theme(legend.position = "none", legend.title=element_blank()) +
  labs(title = "Chromosome3D")





