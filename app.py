from flask import Flask

app = Flask(__name__)

@app.get('/')
def root():
    return {"hello":"world"}

if __name__ == '__main__':
    app.run(debug=True)
    # To run on Replit
    # app.run(host='0.0.0.0', port=8080)