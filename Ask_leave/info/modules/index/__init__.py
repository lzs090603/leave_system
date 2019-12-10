# -*- coding: utf-8 -*-
from flask import Blueprint
import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
#创建蓝图
index_blu = Blueprint("index", __name__)

from . import views