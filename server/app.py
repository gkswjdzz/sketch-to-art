import os

import requests
# Flask utils
from flask import Flask, redirect, url_for, request, render_template, Response, send_file, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__,
            static_folder=os.path.abspath("/usr/src/app/dist/static"),
            template_folder=os.path.abspath("/usr/src/app/dist"))
CORS(app)


@app.route('/')
def main(): 
    return render_template('index.html')

@app.route('/health')
def health_check():
    return "ok"

def reverse_proxy(domain='http://localhost:5001/'):
    # XXX: THANKS TO https://stackoverflow.com/a/36601467
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, domain),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


@app.route('/pix-translate-data', methods=['GET', 'POST'])
def to_pix2pix():
    return reverse_proxy('http://localhost:5001/')

@app.route('/stylize-with-data', methods=['GET', 'POST'])
@app.route('/get-gallery-list', methods=['GET'])
@app.route('/get-gallery-image/<filename>', methods=['GET'])
@app.route('/submit-to-gallery', methods=['GET', 'POST'])
def to_stylize(*args, **kwargs):
    return reverse_proxy('http://localhost:5002/')


if __name__ == '__main__':

    # Serve the app with gevent
    print('Start serving at port 8080...')
    app.run(debug=False, port=8080, host='0.0.0.0')
