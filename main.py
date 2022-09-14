from flask import Flask

app = Flask(__name__)

@app.route("/<int:number>")
def hello_world(number):
    return f"<p>Hello {number}, World!</p>"


if __name__ == '__main__':
   app.run()