from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/squared/<int:number>')
def squared(number):
    return str(number **2)

@app.route('/conc/<string:string1>/<int:int>')
def conc(string1, int):
    return string1 + str(int)

@app.route('/projects')
def projects():
    return 'This is where my projects will be listed'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)