<h1>GPU Code Snippets</h1>

---
### How to increase my `history` size?
Add the following code to `~/.bashrc`
```bash
HISTSIZE=10000
HISTFILESIZE=20000
```

---
### How to allow GPU memory growth?
Add the following code at the beginning of your Python script or Notebook:   

Option 0:
```python
config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
```

Option 1:
```python
import keras.backend as K
gpu_options = tf.GPUOptions(allow_growth=True)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
K.tensorflow_backend.set_session(sess)
```

Option 2:
```
for gpu in tf.config.experimental.list_physical_devices('GPU'):
	tf.config.experimental.set_memory_growth(gpu, True)
```
---
### How to use a specific GPU (in prayog10 server)?
```python
CUDA_VISIBLE_DEVICES=0 python3 train.py
```

---
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

---
### How to remotely access the Tensorboard in prayog02?
#### Install Tensorboard:
```bash
pip3 list
pip3 uninstall tensorboard
pip3 uninstall tensorflow
pip3 uninstall tensorflow-gpu
pip3 install tf-nightly-gpu-2.0-preview
```
#### In 1st Terminal start tensorboard service:
```bash
ssh user@prayog02.umsl.edu
cd project-directory (this is where your logs will be written)
rm -r tb-logs
tensorboard --logdir ./tb-logs/
```
This will give a URL path (along with a port number, say 6007); leave the terminal open.

#### In 2nd terminal Port forward (this is a local terminal; not server terminal)
* If you are using Windows follow [this](https://crl.ucsd.edu/handbook/vnc/index.php) instead
```
$ ssh -L 6007:127.0.0.1:6007 -N -f -l user prayog02.umsl.edu
```
Open the URL path in your local browser `http://localhost:6007/`

#### Test with the following Python code:
```python
import tensorflow as tf
import datetime

# Clear any logs from previous runs
!rm -rf ./tb-logs/ 

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])

model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

log_dir="./tb-logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x=x_train, 
          y=y_train, 
          epochs=3, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])
```

---

How to rsync?
```bash
rsync -av --progress source/ destination/ --exclude dir2
```
---
### How to increase the display decimals (precision) of metrics in Keras?
* Change “1e-4” to “1e-9” in generic_utils.py (at two places) to increase the output precision
* Not sure if this impacts only the display but also the actual accuracy calculations.
```bash
vim /home/notebook/anaconda3/lib/python3.6/site-packages/keras/utils/generic_utils.py
EDIT: info += ' %.4f' % avg
```

---
### How to test GPU speed?
* Run [this code](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.1-introduction-to-convnets.ipynb)

---
### How to find out which device GPU device tensorflow is using?
```python
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

---
### How to make remote folders accessible locally in Mac?
```bash
brew cask install osxfuse
brew install sshfs
sshfs badri@prayog02.umsl.edu:/data/PCP/ /Users/badriadhikari/prayog02.umsl.edu -ovolname=prayog02
```
