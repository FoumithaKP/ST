from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Result: Division by zero is not allowed"
        else:
            result = 'Invalid operation'

        print(f"Result: {result}")  # Debugging line

        return render_template('index.html', result=f"Result: {result}")

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")
if __name__ == '__main__':
    app.run(debug=True)
