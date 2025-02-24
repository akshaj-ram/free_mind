from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/techniques')
def techniques():
    return render_template('techniques.html')

@app.route('/peer-pressure')
def peer_pressure():
    user_type = request.args.get('type', 'individual')
    return render_template('peer_pressure.html', user_type=user_type)

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)