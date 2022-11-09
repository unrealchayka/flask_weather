from flask import Flask, render_template, request, redirect
from openweather import weather

app = Flask(__name__)


@app.route('/index', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            w = weather(request.form['city'])
        except:
            return redirect('/index')
        return render_template('index.html', context=w)
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run(debug=True,)