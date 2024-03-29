#!/usr/bin/python3
from flask import Flask, send_file


app = Flask(__name__)
@app.route('/footer')
def footer():
    #首页
    return send_file('templates/footer.html')
@app.route('/gbook')
def gbook():
    #首页
    return send_file('templates/gbook.html')
@app.route('/header')  
def header():
    #首页
    return send_file('templates/header.html')@app.route('/header')  
@app.route('/list_bak')
def list_bak():
    #首页
    return send_file('templates/list_bak.html')
    
@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

@app.route('/<username>/info')
def info(username):
    #个人信息
    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):
    #修改个人信息
    return send_file('templates/change_info.html')

@app.route('/<username>/topic/release')
def topic_release(username):
    #发表博客
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):
    #个人博客列表
    return send_file('templates/list.html')

@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):
    #博客内容详情
    return send_file('templates/detail.html')


if __name__ == '__main__':
    app.run(debug=True)
    a = 1

