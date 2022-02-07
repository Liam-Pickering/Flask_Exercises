from flask import request

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'