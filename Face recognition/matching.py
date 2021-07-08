import json
import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from keras_vggface.utils import preprocess_input

model = models.load_model('models/embedding')


# file json để lưu ground truth embedding vector của từng khuôn mặt - list of vectors
with open('embedding_database.json', 'r') as openfile:

    # Reading from json file
    json_object = json.load(openfile)

face_embeddings = list(map(np.array, json_object))

# nhãn tên tương ứng
labels = [
    "Dang Nguyen Anh Tuan",
    "Dinh Xuan Vu",
    "Do Manh Quan",
    "Nguyen Anh Tuan",
    "Nguyen Duy Phuc",
    "Ngo Hong Quang",
    "Nguyen Thanh Vinh",
]


def face_matching(img):
    img = preprocess_input(img, version=2)
    img_embedding = model.predict(tf.expand_dims(img, axis=0))

    dis_vec = [np.linalg.norm(face_embedding - img_embedding)
               for face_embedding in face_embeddings]
    idx = np.argmin(dis_vec)

    return labels[idx]
