# -*- coding: utf-8 -*-

from . import index_blu
from flask import request,render_template,redirect
from pymysql import *
import time

conn = connect(host='localhost', port=3306, database='ask', user='root', password='19971103', charset='utf8')
cs = conn.cursor()


@index_blu.route('/')
def table():
    count = cs.execute("select * from ask_table;")
    user11 = cs.fetchall()
    data = []
    for i in user11:

        ps = {
            'id':i[0],
            'name':i[1],
            'stare_time':i[2],
            'end_time':i[3],
            'type':i[4],
            'reason':i[5],

        }
        data.append(ps)
    print(data)
    return render_template('tables.html',data=data)

@index_blu.route('/get_user')
def get_user():
    name = request.args.get('user_name')
    stare_date = request.args.get('star_time')
    end_date = request.args.get('ster_time')
    reason = request.args.get('reason')
    create_time = time.time()
    type = '待审核'
    count = cs.execute("insert into ask_table(name,stare_time,end_time,reason,type,create_time) values('%s','%s','%s','%s','%s','%s')" % (name,stare_date,end_date,reason,type,create_time))
    conn.commit ()
    return redirect('http://127.0.0.1:5000')



@index_blu.route('/delete_user/<id>')
def delete_user(id):
    count = cs.execute("delete from ask_table where id={};".format(id))
    conn.commit()
    return redirect('http://127.0.0.1:5000')


@index_blu.route('/admin')
def admin_user():
    count = cs.execute("select * from ask_table;")
    user11 = cs.fetchall()
    data = []
    for i in user11:
        ps = {
            'id':i[0],
            'name':i[1],
            'stare_time':i[2],
            'end_time':i[3],
            'type':i[4],
            'reason':i[5],

        }
        data.append(ps)
    print(data)
    return render_template('admin_user.html',data=data)


@index_blu.route('/up_type/<id>')
def up_type(id):
    print(id)
    type = '通过'
    count = cs.execute("update ask_table set type='{}' where id={};".format(type,id))
    conn.commit()

    return redirect('http://127.0.0.1:5000/admin')


@index_blu.route('/no_up_type/<id>')
def no_up_type(id):
    print(id)
    type = '不通过'
    count = cs.execute("update ask_table set type='{}' where id={};".format(type,id))
    conn.commit()

    return redirect('http://127.0.0.1:5000/admin')