from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# localhost:5000/
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    # return f'GOT it <br /> {str(request.form)}'
    return f'Your name is {request.form["txt_name"]}'

app.run()