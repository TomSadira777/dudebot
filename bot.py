from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/420", methods=["POST"])
def handle_420():
    user = request.form.get("user_name", "Dude")
    today = datetime.today()
    year = today.year if (today.month, today.day) < (4, 20) else today.year + 1
    next_420 = datetime(year, 4, 20)
    days_remaining = (next_420 - today).days

    message = f"Hey there, {user}... it's {days_remaining} days until the next 4/20. The Dude abides. 😎✌️"
    return jsonify(response_type="in_channel", text=message)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)