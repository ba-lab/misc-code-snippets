import tensorflow as tf
import datetime
import time

print('')
print('')
print('Checking CPU/GPU...')
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF!!")

time.sleep(1)

print('')
print('')
print('Listing devices..')
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
print('')
print('')

time.sleep(1)

# Clear any logs from previous runs
#!rm -rf ./tb-logs/ 

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
