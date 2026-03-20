from flask import Flask, request, render_template_string
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

HTML = """
<h2>Vote your favorite!</h2>
<form method="POST">
  <button name="vote" value="A">Vote A</button>
  <button name="vote" value="B">Vote B</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        vote = request.form["vote"]
        r.rpush("votes", vote)
        return "Vote submitted!"
    return render_template_string(HTML)

app.run(host="0.0.0.0", port=80)