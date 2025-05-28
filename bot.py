{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
from datetime import datetime\
\
app = Flask(__name__)\
\
@app.route("/420", methods=["POST"])\
def handle_420():\
    user = request.form.get("user_name", "Dude")\
    today = datetime.today()\
    year = today.year if (today.month, today.day) < (4, 20) else today.year + 1\
    next_420 = datetime(year, 4, 20)\
    days_remaining = (next_420 - today).days\
\
    message = f"Hey there, \{user\}... it's \{days_remaining\} days until the next 4/20. The Dude abides. \uc0\u55356 \u57151 \u9996 \u65039 "\
    return jsonify(response_type="in_channel", text=message)\
\
if __name__ == "__main__":\
    app.run(debug=True)}