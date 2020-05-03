import numpy as np
import tensorflow as tf


def predict(image_path):    
    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(    
        rescale=1./255
        )
        
    # load the image
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(128, 128))
    # convert to numpy array
    image = tf.keras.preprocessing.image.img_to_array(image)
    # expand dimension to one sample
    image = np.expand_dims(image, 0)
    # prepare iterator
    image = test_datagen.flow(image, batch_size=1)[0]

    # load model
    model = tf.keras.models.load_model('saved_model/catsNdogs_combined')
    # predict
    return model.predict(image, verbose=1)[0]
