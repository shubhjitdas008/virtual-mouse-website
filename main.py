from flask import Flask , render_template ,  jsonify ,url_for
import subprocess


app =  Flask(__name__ , static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/log_in')
def log_in():
    return render_template('log_in.html')
    
@app.route('/log_in/sign_in')
def sign_in():
    return render_template('sign_in.html')  

@app.route('/run_pdf')
def run_pdf():
    result = subprocess.run(['python', 'pdf.py'], capture_output=True, text=True)
    return result.stdout
     


@app.route('/gesture')
def gesture():
    result = subprocess.run(['python', 'button.py'], capture_output=True, text=True)
    return result.stdout

app.run(host='0.0.0.0' , debug=True)