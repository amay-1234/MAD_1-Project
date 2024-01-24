from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/Register')
def register():
    return render_template('Register.html')




if __name__ == '__main__':
    app.run(debug=True, port=5000)