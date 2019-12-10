# -*- coding: utf-8 -*-

from flask_script import Manager
from info import create_app
from flask_cors import *


app = create_app('development')

# 添加扩展命令行
manager = Manager(app)


CORS(app, supports_credentials=True)


if __name__ == '__main__':
    manager.run()