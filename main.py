from flask import Flask, send_file
import paper_viewer

app = Flask(__name__)

@app.route('/paper/<doi1>/<doi2>/<page>')
def paper(doi1, doi2, page):
    try:
        doi=f'{doi1}/{doi2}'
        pv=paper_viewer.paper_viewer(doi)
        pv.download_pdf()
        pv.pdf2image()
        pv.image2mp4()
        return send_file(f'./result_{pv.file_name}/{pv.file_name}{page}.mp4', mimetype='video/mp4', f'{pv.file_name}{page}.mp4', as_attachment=True)
    except:
        return 'something went wrong'


@app.route('/')
def home():
    return 'There is nothing here...'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
