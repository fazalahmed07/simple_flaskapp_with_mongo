from flask import Flask, request, render_template
from datetime import datetime
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:9000"

@app.route('/')
def home():
    day_of_the_week = datetime.today().strftime('%A')
    return render_template('index.html', day_of_the_week=day_of_the_week)


@app.route('/submit', methods=['POST'])
def submit():
    day_of_the_week = datetime.today().strftime('%A')
    form_data = dict(request.form)
    
    try:
        # Forward data to the backend
        response = requests.post(f"{BACKEND_URL}/submit", json=form_data)
        
        if response.status_code == 200:
            # Redirect/Render to a simple success state
            return "<h1>Data submitted successfully</h1>"
        else:
            # Grab the error message sent by the backend
            error_msg = response.json().get('error', 'Unknown backend error occurred.')
            return render_template('index.html', day_of_the_week=day_of_the_week, error=error_msg)
            
    except requests.exceptions.ConnectionError:
        error_msg = "Could not connect to the backend database service."
        return render_template('index.html', day_of_the_week=day_of_the_week, error=error_msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)