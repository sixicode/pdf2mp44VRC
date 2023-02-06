from flask import Flask
import downloader as dl

app = Flask(__name__)

@app.route('/paper/<doi>', methods=['GET'])
    num=int(doi)


@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
