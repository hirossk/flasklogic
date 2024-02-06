from flask import Flask,render_template,session,redirect

app = Flask(__name__, static_folder="./static/")
app.secret_key = 'user'

def login_check():
    if (session.get('logoned') == True):
        return True
    else:
        return False

@app.route('/')
def login():
    return render_template('transition/01login.html')

@app.route('/confirm',methods=["POST"])
def confirm():
    session['logoned'] = True
    return render_template('transition/01toppage.html')

@app.route('/link1')
def link1():
    if(login_check() == True):
        return render_template('transition/01link1.html')
    else:
        return redirect("/")

@app.route('/link2')
def link2():
    if(login_check() == True):
        return render_template('transition/01link2.html')
    else:
        return redirect("/")

if __name__=='__main__':
    app.run(host="0.0.0.0",port=80,debug=False)