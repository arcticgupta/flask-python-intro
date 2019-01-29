from flask import Flask, render_template, url_for, request, redirect
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/page2')
def about():
    return render_template('page2.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'sweta ki dick':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('login.html', error=error)
@app.route('/success')
def success():
    return render_template('success.html')

if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)