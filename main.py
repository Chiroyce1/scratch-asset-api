from flask import Flask, request

app = Flask(__name__)

@app.after_request
def CORS(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.get('/')
def root():
    return {"hello":"world"}

@app.post('/<hash>.<extension>')
def handle_upload(hash, extension):
    print(request.get_data())
    with open(f'./assets/{hash}.{extension}', 'w') as file:
        file.write(request.get_data())
    return {"hash": hash, "extension": extension}

if __name__ == '__main__':
    # To run locally on `http://localhost:5000`
    # app.run(debug=True)
    
    # To run on Replit
    app.run(host='0.0.0.0', port=8080)
    