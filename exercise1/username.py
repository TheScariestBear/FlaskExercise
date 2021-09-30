from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    lower = False
    upper = False
    if username[-1].isdigit():
        number = True
    else:
        number = False
    for i in username:
        if i.islower():
            lower = True
            break
    for i in username:
        if i.isupper():
            upper = True
            break
    if number and lower and upper:
        return render_template('reportpass.html')
    else:
        return render_template('reportfail.html',number=number,upper=upper,lower=lower)

if __name__ == '__main__':
    app.run(debug=True)
