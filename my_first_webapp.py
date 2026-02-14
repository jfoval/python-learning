# My First Web Application!

from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return """
    <h1>My First Web App!</h1>
    <p>Welcome to my website built with Python!</p>
    <a href="/about">About Me</a> |
    <a href="/calculator">Calculator</a>
    """

# About page
@app.route('/about')
def about():
    return """
    <h1>About Me</h1>
    <p>I'm learning Python and web development!</p>
    <a href="/">Back to Home</a>
    """

# Interactive calculator
@app.route('/calculator')
def calculator():
    return """
    <h1>Calculator</h1>
    <form action="/calculate" method="get">
        <input type="number" name="num1" placeholder="First number" required>
        <select name="operation">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">×</option>
            <option value="/">÷</option>
        </select>
        <input type="number" name="num2" placeholder="Second number" required>
        <button type="submit">Calculate</button>
    </form>
    <br><a href="/">Back to Home</a>
    """

@app.route('/calculate')
def calculate():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    op = request.args.get('operation')

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"

    return f"""
    <h1>Result</h1>
    <p>{num1} {op} {num2} = {result}</p>
    <a href="/calculator">Calculate Again</a> |
    <a href="/">Home</a>
    """

if __name__ == '__main__':
    print("🚀 Starting web server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    app.run(host='0.0.0.0', debug=True)
