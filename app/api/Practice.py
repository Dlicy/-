from flask import Flask, request, jsonify
from flask_cors import CORS
from backflask import app

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/Practice/Practice.vue', methods=['POST'])
def process_text():
    try:
        # 获取前端发送过来的 JSON 数据
        request_data = request.get_json()

        # 提取文本信息
        input_text = request_data['text']

        # 在这里可以对 input_text 进行处理，比如调用机器学习模型、数据库查询等

        # 假设处理后得到一个响应消息
        response_message = f"You sent: {input_text}. Server processed it."

        # 返回响应给前端
        return jsonify({'message': response_message})

    except Exception as e:
        print(f"Error processing text: {e}")
        return jsonify({'message': 'Error processing text'}), 500

if __name__ == '__main__':
    app.run(port=5000)
