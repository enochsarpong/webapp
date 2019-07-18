from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/foo')
def foo():
    return render_template('foo.html')

@app.route('/bar')
def bar():
    return render_template ('bar.html!')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
