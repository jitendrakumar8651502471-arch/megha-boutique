import razorpay
from flask import Flask, render_template

app = Flask(__name__)

# यहाँ अपनी असली KEY_ID और KEY_SECRET डालें
razorpay_client = razorpay.Client(auth=("Megha", "5019"))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)