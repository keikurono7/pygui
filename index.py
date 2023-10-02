from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        # Process the user's input here
        # You can store it in a database, perform calculations, etc.
        # For demonstration purposes, we'll just display the input.
        return f'You entered: {user_input}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
