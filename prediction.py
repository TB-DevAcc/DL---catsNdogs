import tensorflow as tf

def predict(image):

    model = tf.keras.models.load_model('saved_model/catsNdogs')

    # Check its architecture
    # model.summary()

    # # Evaluate the restored model
    # loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
    # print('Restored model, accuracy: {:5.2f}%'.format(100*acc))

    # print(new_model.predict(test_images).shape)

    print(model.predict(img_gen))

predict()