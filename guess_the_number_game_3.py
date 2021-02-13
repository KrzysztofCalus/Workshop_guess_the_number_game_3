from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def number():
    min = 0
    max = 1000
    guess = int((max - min) / 2 + min)
    html = f"""
            <html>
            <form action="/" method="POST">
            <label>{guess}</label>
            <label>
            <button type="submit" name="user_answer" value="You win">You win</button>
            <button type="submit" name="user_answer" value="To big">To big</button>
            <button type="submit" name="user_answer" value="To small">To small</button>
            </label>
            </form>
            </html>
            """
    if request.method == 'GET':
        return html
    else:
        user_answer = request.form["user_answer"]
        if user_answer == "You win":
            return "Hurra! I guess"
        if user_answer == "To big":
            max = guess
            return html
        if user_answer == "To small":
            min = guess
            return html


if __name__ == "__main__":
    app.run(debug=True)