from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    print('Someone accessed')
    return 'Hi'

@app.route('/get_image')
def get_image():
    requester = request.remote_addr
    current_datetime = datetime.now()
    
    with open('logs.txt', 'a') as f:
        f.write(f'{current_datetime} - {requester}\n')
        
    return send_file('img.jpg')

if __name__ == '__main__':
      app.run(threaded=True, port=80)
