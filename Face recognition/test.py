
# tạo ra file json - list of ground truth embedding vectors
# thử nghiệm trên backend trước khi deploy

import cv2
from keras_vggface.vggface import VGGFace
from tensorflow.python.keras.utils import generic_utils
from tensorflow.keras.models import load_model
from keras_vggface.utils import preprocess_input
import tensorflow as tf
from imutils import paths
import json
import numpy as np
from scipy.spatial.distance import cosine
from face_extraction import extract_face
import time


# model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
# model.save('pretrained_model')

model = load_model('models/embedding')

"""1"""
# print(model.summary())

"""2"""
# img_paths = sorted(paths.list_images('anchor'))

# feature_vectors = []

# for img_path in img_paths:
#     img = extract_face(img_path)

#     img = preprocess_input(img, version=2)
#     feature_vector = model.predict(tf.expand_dims(img, axis=0))
#     feature_vectors.append(feature_vector.tolist())

# json_object = json.dumps(feature_vectors)
# with open('embedding_database.json', 'w') as outfile:
#     outfile.write(json_object)

# print('success')


""""3"""
with open('embedding_database.json', 'r') as openfile:

    # Reading from json file
    json_object = json.load(openfile)

face_embeddings = list(map(np.array, json_object))


labels = [
    "Dang Nguyen Anh Tuan",
    "Dinh Xuan Vu",
    "Do Manh Quan",
    "Nguyen Anh Tuan",
    "Nguyen Duy Phuc",
    "Ngo Hong Quang",
    "Nguyen Thanh Vinh",
]

t1 = time.time()


def test(imgPath):
    img = extract_face(imgPath)
    img = preprocess_input(img, version=2)
    img_embedding = model.predict(tf.expand_dims(img, axis=0))

    dis_vec = [np.linalg.norm(face_embedding - img_embedding)
               for face_embedding in face_embeddings]
    idx = np.argmin(dis_vec)

    return labels[idx], dis_vec


t2 = time.time()

imgPath = 'test/5.jpg'

face, dis_vec = test(imgPath)
img = cv2.imread(imgPath)
cv2.putText(img, face, (100, 100), cv2.FONT_HERSHEY_SIMPLEX,
            4, (250, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('result', img)
cv2.waitKey()

print(f'[INFO] time: {t2 - t1}')
print(f'[INFO] distance vector: {dis_vec}')
