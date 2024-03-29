from flask import Flask, render_template, request
import models
from flask_cors import CORS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        models.create_post(name, post)

    posts = models.get_posts()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)