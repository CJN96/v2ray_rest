from flask import Flask, request, jsonify
import traffic_api

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/v2ray/api/traffic')
def get_traffic():
    email = request.args.get("email")
    if email:
        data = traffic_api.get_traffic(email)
        if len(data) == 2:
            return jsonify({'code': 0, 'msg': 'success', 'data': data})
        else:
            return jsonify({'code': -1, 'msg': 'query fail'})
    else:
        return jsonify({'code': -2, 'msg': 'require [email] parameter'})


if __name__ == '__main__':
    app.run(debug=False)
