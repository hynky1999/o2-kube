from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/showtime', methods=['GET'])
def get_show_time():
    api_name = os.environ.get('API_DNS', 'api-service')
    response = requests.get('http://{}/api/time'.format(api_name))
    return jsonify({'showtime': response.json()['time']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
