# 获取了用户输入的文件信息，然后调用到判题机判题后返回内容
from flask import Flask, request
import subprocess
import os
import re


app = Flask(__name__)

@app.route('/On-upload', methods=['POST'])
def execute_command():
    # 获取前端发送的文件
    uploaded_file = request.files['file']

    # 将文件保存到服务器

    file_path = os.path.join('uploads', uploaded_file)
    # 返回上两级目录
    parent_dir = os.path.abspath(os.path.join(file_path, os.pardir, os.pardir))
    # 访问上两级目录中的 'competitive-programming-tester-cli'
    another_folder_path = os.path.join(parent_dir, 'competitive-programming-tester-cli')

    uploaded_file.save(another_folder_path)

    # 执行命令行操作
    try:
        output = subprocess.check_output(['cp-tester run loan_repayment_silver_jan2020 --file', file_path], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Error executing command: {e}', 500

def parse_test_results(output):
    """解析测试结果输出,返回一个列表的字典。"""
    results = []
    for line in output.strip().split('\n'):
        match = re.match(r'(Test Case \d+): (\d+ milliseconds)\n(PASSED)', line)
        if match:
            result = {
                'name': match.group(1),
                'time': match.group(2),
                'status': match.group(3)
            }
            results.append(result)
    return results

test_results = parse_test_results(execute_command())
print(test_results)

if __name__ == '__main__':
    app.run(debug=True)