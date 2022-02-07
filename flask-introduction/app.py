from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "So how is this running\nI honestly have no clue\nBut it works oooooooooooooo"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)