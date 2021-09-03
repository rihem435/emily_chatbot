from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
     name = request.form['name']
     password = request.form['password']
    response={'name':name}
    return jsonify({"user": response })
    

@app.route('/auth/signup', methods=[ "POST"])
def signup():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        response={'name':name,'email':email}

    return jsonify({"user": response })

@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html', **locals())

@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template('contact.html', **locals())

@app.route('/aboutus', methods=["GET"])
def aboutus():
    return render_template('aboutus.html', **locals())


@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)
    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True,use_reloader=True)
