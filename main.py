from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():    
    return render_template('landing.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)