from flask import Flask, render_template, request, send_from_directory

import model


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('sign-up.html')

@app.route('/login')
def login():
    return render_template('log-in.html')

@app.route('/demo', methods=['POST', 'GET'])
def demo():
    if request.method == 'GET':
        return render_template('demo.html')
    else:
        file = request.files["image"]
        upload_image_path = 'static/uploads/' + file.filename
        print('Predicting on image at', upload_image_path)
        file.save(upload_image_path)

        dog_prob, cat_prob = model.predict(upload_image_path)

        if cat_prob > dog_prob:
            cat_cols = int(cat_prob*12)
            dog_cols = int(dog_prob*12)+1
            result = 'Cat'
        else:
            cat_cols = int(cat_prob*12)+1
            dog_cols = int(dog_prob*12)
            result = 'Dog'

    return render_template(
        'classify.html', 
        image_file_name=file.filename, 
        cat_prob=round(cat_prob, 2), 
        dog_prob=round(dog_prob, 2),
        cat_cols=cat_cols,
        dog_cols=dog_cols,
        result=result
        )

@app.route('/classify/<filename>')
def send_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 