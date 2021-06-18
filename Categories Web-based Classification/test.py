import tensorflow as tf
import cv2
from tensorflow.keras import models

model = models.load_model('best_model.hdf5')
img = cv2.imread('anchor/7.jpg')
img = cv2.resize(img, (127, 127))
pred = model.predict(tf.expand_dims(img, axis=0))
print(pred.shape)
