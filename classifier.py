import numpy as np
import pandas as pd
from tensorflow.python.keras.backend import set_session, get_session
from skimage.transform import resize
import matplotlib.pyplot as plt
from keras import backend as K
from keras.models import load_model
import tensorflow as tf

session = get_session()
init = tf.global_variables_initializer()
session.run(init)

CROP_SIZE = (256,256)
IMG_SHAPE = (70,70)


#def root_mean_squared_error(y_true, y_pred):
 #   return K.sqrt(K.mean(K.square(y_pred - y_true))) 

#dependencies = {
#    'root_mean_squared_error': root_mean_squared_error
#}
#model = load_model('./static/model/model.h5.back', custom_objects=dependencies)
model = load_model('./static/model/model.h5')
graph = tf.get_default_graph()
def predict_galaxy(path):
    global graph
    global session
    with graph.as_default():
        set_session(session)
        image = plt.imread(path)
        image = resize(image, IMG_SHAPE)
        #image = image/255
        result = model.predict(np.array([image]))
        cls = np.argmax(result, axis=1)
        print(cls[0])
        return class_finder(cls[0])
def class_finder(result):
    label_ = {0:'Disk',1:'Spiral',2:'Disk',3:'Completely round',4:'Completely round',5:'in-between round',6:'in-between round',7:'Cigar Shaped',
              8:'Cigar Shaped',9:'Disk',10:'Edge On',11:'Rounded Bulge',12:'Disk',13:'Cigar Shaped',14:'Boxy Bulge',15:'Disk', 16:'Disk', 17:'Edge-on',
              18:'No Bulge',19:'spiral',20:'Face-on', 21:'Tight Spiral',22:'Disk', 23:'Face-on',24:'Medium Spiral',25:'Disk',26:'Face on',
              27:'loose spiral'}
    label__ = {
    6: "Completely Round",
    5: "In between",
    4: "Cigar Shaped",
    3: "On Edge",
    2: "Has Signs of Spiral",
    1: "Spiral Barred",
    0: "Spiral",
}
    return label__[result]
    
