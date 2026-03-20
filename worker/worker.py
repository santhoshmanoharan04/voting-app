import redis
import psycopg2
import os
import time

redis_host = os.getenv("REDIS_HOST", "redis")
db_host = os.getenv("DB_HOST", "db")

r = redis.Redis(host=redis_host, port=6379)

# Wait for DB to be ready
time.sleep(5)

conn = psycopg2.connect(
    host=db_host,
    database="votes",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    vote VARCHAR(10)
)
""")
conn.commit()

print("Worker started...")

while True:
    vote = r.blpop("votes")[1].decode("utf-8")

    cur.execute("INSERT INTO votes (vote) VALUES (%s)", (vote,))
    conn.commit()

    print("Stored vote:", vote)