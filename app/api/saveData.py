# app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()['data']

    # 将数据写入文件
    with open('data.txt', 'w') as f:
        f.write(data)

    return jsonify({'message': 'Data saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)