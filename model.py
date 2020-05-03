import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def format_img(image_path):    
    test_datagen = ImageDataGenerator(    
        rescale=1./255
        )
        
    # load the image
    image = load_img(image_path)
    # convert to numpy array
    image = img_to_array(image)
    # expand dimension to one sample
    image = np.expand_dims(image, 0)
    # prepare iterator
    return test_datagen.flow(image, batch_size=1)

def predict(image):

    model = tf.keras.models.load_model('saved_model/catsNdogs_combined')

    # Check its architecture
    # model.summary()

    # # Evaluate the restored model
    # loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
    # print('Restored model, accuracy: {:5.2f}%'.format(100*acc))

    # print(new_model.predict(test_images).shape)

    # Returns list with probability Dog & Cat [0, 1]
    return model.predict(format_img(image))[0]