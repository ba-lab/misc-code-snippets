# Lewis Server
### Documentations
* [Main documentation](https://docs.rnet.missouri.edu)
* [Slurm tutorial](https://wiki.rc.hms.harvard.edu/display/O2/Using+Slurm+Basic)
* [Basic linux commands](http://docs.rnet.missouri.edu/Linux/basic-commands)

---
### What are the directories that I have access to (and their space limits)?
`~, ~/data, ~/scratch, /group/prayog/, /storage/htc/prayog/`

```
~/ - 5GB
~/data/ - 100GB
/group/prayog/ - 100GB or 250GB
/storage/htc/prayog - 10TB
~/scratch/ - Unlimited
```

```
lfs quota -hg prayog-group /storage/hpc
```

---
### How to obtain a GPU terminal?
#### Option 1 (quick):
```
source /group/prayog/ba-lab/ba-lab/give-me-a-gpu-node.sh
source /group/prayog/ba-lab/keras.sh
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
   
---
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

---
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

---
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

---
### How to know who is in my group?
```
getent group prayog-group
```

---
### How to lookup detailed partition information (number of nodes, etc.)
```
sinfo --long --partition=Lewis
sinfo --long --partition=Gpu
sinfo --long --partition=gpu3
```

---
### How to create a 'daddy' sbatch job?
```bash
#!/bin/bash
for pdb in `ls ./aln/*.aln`; 
   do
	id=$(basename $pdb)
	id=${id%.*}
	echo $id
	sbatch /group/prayog/ba-lab/sbatch-Lewis.sh $id
   done
```
