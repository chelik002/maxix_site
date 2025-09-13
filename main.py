from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # передаём данные в шаблон
    return render_template("index.html", balance=1234, rate=15.60)

if __name__ == "__main__":
    # Render требует host=0.0.0.0 и порт, который он задаёт через переменную PORT
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
