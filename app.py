from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>HELLO WORLD</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"{post_id}"
     
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5001' )