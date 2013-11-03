from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open("report", "r") as report:
        string = ""
        for line in report.readlines():
            string += line + "<br>"
        return string

if __name__ == '__main__':
    app.run()
