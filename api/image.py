# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

YOUTUBE_URL = "https://youtu.be/xvFZjo5PgG0?si=vhMrJfztYaBUdpNk"

HTML = """
<!doctype html>
<html lang="hu">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Megnyit 10 videót (kattints rá)</title>
  <style>
    html,body { height:100%; margin:0; display:flex; align-items:center; justify-content:center;
                background:#111; color:#fff; font-family:system-ui,Arial; }
    .card { background:#222; padding:24px; border-radius:8px; box-shadow:0 6px 20px rgba(0,0,0,0.6); text-align:center; }
    button { padding:10px 16px; font-size:16px; cursor:pointer; border-radius:6px; }
    p { font-size:13px; color:#bbb; margin-top:12px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Kattints ide a videók megnyitásához</h2>
    <button id="openBtn">Megnyit 10 videót</button>
    <p>Megjegyzés: a böngészők popup-blokkolója megakadályozhatja, hogy mind a 10 fül megnyíljon.</p>
  </div>

  <script>
    const url = "{{ url }}";
    document.getElementById('openBtn').addEventListener('click', () => {
      // Ez a kód csak kattintás után fut; a böngészők általában csak ekkor engednek window.open-ot
      for (let i = 0; i < 10; i++) {
        window.open(url, '_blank');
      }
    });
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, url=YOUTUBE_URL)

if __name__ == "__main__":
    app.run(debug=True)
