# from flask import Flask, request, jsonify
# import os
# import subprocess
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
#
# @app.route('/api/saveData/', methods=['POST','GET'])
# def save_data():
#     data = request.get_data()
#     with open('data.txt', 'wb') as f:
#         f.write(data)
#     return '数据已保存到文件中'
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
#
# from werkzeug.utils import secure_filename
#
# from app.backflask import app
#
# UPLOAD_FOLDER = '/'  # 设置上传文件的存放路径
# ALLOWED_EXTENSIONS = {'txt','cpp'}  # 允许的文件类型
#
# # 配置上传文件的最大大小（单位为字节）
# app.config['MAX_CONTENT_LENGTH'] = 256 * 1024 * 1024  # 限制为16MB
#
# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# @app.route('/api/saveData', methods=['POST'])
# def save_data():
#     print("Request URL:", request.url)
#     print("Request method:", request.method)
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(UPLOAD_FOLDER, filename))
#         return jsonify({'message': 'File saved successfully'}), 200
#     else:
#         return jsonify({'error': 'Invalid file type'}), 400
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from werkzeug.utils import secure_filename

from app.backflask import app

CORS(app)

UPLOAD_FOLDER = '/'  # 设置上传文件的存放路径
ALLOWED_EXTENSIONS = {'txt', 'cpp'}  # 允许的文件类型

# 配置上传文件的最大大小（单位为字节）
app.config['MAX_CONTENT_LENGTH'] = 256 * 1024 * 1024  # 限制为16MB

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/saveData', methods=['POST'])
def save_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'message': 'File saved successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
