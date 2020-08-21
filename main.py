from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

app = Flask(__name__)

USERS = {
    'tom':{
        'name':'tom',
        'password':'123456',
        'gender':'男',
        'age':27
    },
    'lucy':{
        'name':'lucy',
        'password':'123456',
        'gender':'女',
        'age':27
    }
}

@app.route('/',methods=('POST','GET'))
def login():
    if request.method == 'POST':
        # 提取请求的参数
        name = request.form.get('name')
        password = request.form.get('password')

        # 验证用户名、密码
        user = USERS.get(name) # 这一步是干啥的？是从库里获取用户信息的呀
        #如果表单中输入的姓名在我们的数据库中，那么 user 就有值，如果 user 为空的，那么这个用户名就不在我们的数据库里被
        if not user:
            return '用户名不存在'
        if user['password'] != password:
            return '密码错误'

        # 这一步是比较关键的一步，记录用户的登录信息
        html = render_template('result.html')
        response = make_response(html)
        response.set_cookie('username',name)
        return response
    else:
        return render_template('login.html')

@app.route('/info')
def user_info():
    name = request.cookies.get('username')
    if not name :
        return '您还没有登录'
    else:
        user = USERS[name]
        return render_template('info.html',user=user)


if __name__ == '__main__':
    app.run(debug=True)