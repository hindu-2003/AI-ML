from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   return "Hai"

@app.route("/hello")
def hello_world():
   return "Hello AI ML students"

if __name__ == '__main__':
   app.run()