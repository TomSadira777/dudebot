from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "DudeBot is alive, man!"


@app.route("/420", methods=["POST"])
def handle_dudebot():
    user = request.form.get("user_name", "Dude")
    text = request.form.get("text", "").strip().lower()

    if "420" in text:
        return respond_420(user)
    elif "green wednesday" in text:
        return jsonify(response_type="in_channel", text="Green Wednesday’s the day before Thanksgiving, man. Big sales, big vibes.")
    elif "flower" in text:
        return jsonify(response_type="in_channel", text="Flower is the smokable part of the cannabis plant, man. It’s the OG format. 🌿")
    elif "thc" in text:
        return jsonify(response_type="in_channel", text="THC is the psychoactive compound in cannabis, man. It’s what gets you feelin’ like you’re floatin’ over the rug.")
    elif "cbd" in text:
        return jsonify(response_type="in_channel", text="CBD is like THC’s mellow cousin, man. No high, just chill. Great for relaxation and inflammation.")
    elif "edibles" in text:
        return jsonify(response_type="in_channel", text="Edibles are cannabis-infused food or drinks. Start low and go slow, man. Trust me.")
    elif "thc drinks" in text or "drinks" in text:
        return jsonify(response_type="in_channel", text="THC drinks are like a little vacation in a can, man. Discreet, tasty, and uplifting.")
    elif "shatter" in text:
        return jsonify(response_type="in_channel", text="Shatter is a potent cannabis concentrate. It’s brittle, glassy, and packs a wallop.")
    elif "vape" in text:
        return jsonify(response_type="in_channel", text="Vapes heat up oil or flower to release vapor, not smoke. It’s like... hot yoga for your weed.")
    elif "tincture" in text:
        return jsonify(response_type="in_channel", text="Tinctures are liquid cannabis extracts you drop under your tongue. Fast-acting, low-key, very zen.")
    elif "indica" in text:
        return jsonify(response_type="in_channel", text="Indica strains are relaxing, body-heavy, and couch-lock-y. Like sinking into your favorite bean bag.")
    elif "sativa" in text:
        return jsonify(response_type="in_channel", text="Sativas are more energizing and uplifting. Great for daytime chillin’, creative flow, or philosophical bowling.")
    elif "hybrid" in text:
        return jsonify(response_type="in_channel", text="Hybrids mix indica and sativa traits, man. Best of both worlds. Like rug and sunglasses.")
    elif "concentrate" in text:
        return jsonify(response_type="in_channel", text="Concentrates are potent extracts of cannabis, man. A little dab’ll do ya.")
    elif "the rug" in text or "rug" in text:
        return jsonify(response_type="in_channel", text="That rug really tied the room together, did it not?")
    else:
        return respond_default(user)


def respond_420(user):
    today = datetime.today()
    year = today.year if (today.month, today.day) < (4, 20) else today.year + 1
    next_420 = datetime(year, 4, 20)
    days_remaining = (next_420 - today).days
    message = f"Hey there, {user}... it's {days_remaining} days until the next 4/20. The Dude abides. 😎✌️"
    return jsonify(response_type="in_channel", text=message)


def respond_default(user):
    return jsonify(response_type="in_channel", text=f"Sorry, {user}, I’m not sure what you mean... but I’m here, I’m chill, and I’ll always abide. Try askin’ me about 4/20, THC, flower, or shatter. 🕶️")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)