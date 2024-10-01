from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask! This is running on Cloud Run."

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
