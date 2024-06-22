from flask import Flask, request, jsonify
import os
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 上传文件的     路由
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'})

    global file
    file = request.files['file']
    print(file)
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'})

    upload_folder = 'data'  # 保存文件的目录
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # 调用另一个 Python 脚本，并传递文件名作为命令行参数
    script_path = 'Ifasr_new.py'  # 替换为你要运行的脚本的路径
    subprocess.Popen(['python', script_path, file_path])

    return jsonify({'success': True, 'message': 'File uploaded successfully'})


if __name__ == '__main__':
    app.run(debug=True)
