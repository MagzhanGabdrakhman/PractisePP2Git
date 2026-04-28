import psycopg2
from config import DATABASE

try:
    conn = psycopg2.connect(**DATABASE)
    print("✅ Connected successfully")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
