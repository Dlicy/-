import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 获取当前文件的绝对路径
base_dir = os.path.abspath(os.path.dirname(__file__))

# 构建数据库文件的完整路径
db_path = os.path.join(base_dir, '..', '..', 'sql.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)

# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# 获取用户信息
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username
        })
    else:
        return jsonify({'error': 'User not found'}), 404

# 更新用户密码
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_password(user_id):
    user = User.query.get(user_id)
    if user:
        new_password = request.json.get('password')
        if new_password:
            user.password = new_password
            db.session.commit()
            return jsonify({'message': 'Password updated successfully'})
        else:
            return jsonify({'error': 'Password is required'}), 400
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)