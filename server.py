from flask import Flask
from api import api 

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')  # 所有路由将以 /api 开头

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
