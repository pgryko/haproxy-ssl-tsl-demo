from flask import request, Flask

app = Flask(__name__)


@app.route('/')
def index():
    headers = "This displays what is send to the server via the headers: \n \n </br></br>"
    for item in request.headers:
        headers += str(item) + "\n </br>"
    return(headers)
    # return "Hello World!"


if __name__ == '__main__':
    app.run()
