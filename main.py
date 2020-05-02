from flask import Flask, render_template

import model


app = Flask(__name__, static_url_path='/static')

predictions = model.predict('saved_model/test1/1.jpg')

@app.route('/')
def index():
    return render_template('sign-up.html', data=predictions)

@app.route('/login')
def login():
    return render_template('log-in.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 