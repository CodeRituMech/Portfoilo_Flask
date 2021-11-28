from flask import Flask,render_template,request
import smtplib,os
app = Flask(__name__)
def send_mail(msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email','password')
    server.sendmail('your_emial','Sender_email',msg)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/works')
def works():
    return render_template("works.html")
@app.route('/work')
def work():
    return render_template("work.html")


@app.route('/dash')
def login():
    return render_template('login.html')
@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        email=request.form['email']
        user_msg=request.form['msg']
        sub=request.form['subject']
        msg=f'MESSAGE FROM--{email}\n\n{sub}\n\n{user_msg}'
        send_mail(msg)
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)


