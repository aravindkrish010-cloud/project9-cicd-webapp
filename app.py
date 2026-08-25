from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from my CI/CD pipeline! This app was automatically deployed by GitHub Actions."

if __name__ == '__main__':
    app.run()
