from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    version = '1.5'
    return f"Hello world ver {version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)