import requests
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def web():
    try:
        url = "https://netflix.com"
        response = requests.get(url)
        print('data:', response)
        if response.status_code == 200:
            return render_template('new_page.html')
        else:
            return "Failed to retrieve data from Netflix",response.status_code
    except:
        return response.status_code
if __name__ == '__main__':
    app.run()
