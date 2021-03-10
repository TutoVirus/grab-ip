from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def main():
    print('Someone accessed')
    return 'Hi'

@app.route('/get_image')
def get_image():
    requester = request.remote_addr
    print('IP: ' + request.headers['X-Forwarded-For'])
        
    return send_file('img.jpg')

if __name__ == '__main__':
      app.run(threaded=True, port=80)
