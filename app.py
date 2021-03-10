from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hi'

@app.route('/pepelove.jpg')
def get_image_pepelove():
    requester = request.remote_addr
    print('IP: ' + request.headers['X-Forwarded-For'])
        
    return send_file('pepelove.jpg')

@app.route('/aligator.jpg')
def get_image_aligator():
    requester = request.remote_addr
    print('IP: ' + request.headers['X-Forwarded-For'])
        
    return send_file('aligator.jpg')

if __name__ == '__main__':
      app.run(threaded=True, port=80)
