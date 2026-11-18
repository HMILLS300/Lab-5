from flask import Flask, request

app = Flask(__name__)

class Calculations:
    def sum(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def quotient(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])

        calc = Calculations()

        result = f"""
        Sum: {calc.sum(a, b)}<br>
        Difference: {calc.difference(a, b)}<br>
        Product: {calc.product(a, b)}<br>
        Quotient: {calc.quotient(a, b)}
        """

    return f"""
    <h1>Calculator</h1>
    <form method="POST">
        <input name="a" type="number" step="any" placeholder="First number">
        <input name="b" type="number" step="any" placeholder="Second number">
        <button type="submit">Calculate</button>
    </form>
    <p>{result}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


