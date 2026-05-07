from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

# allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB connection (edit values if needed)
conn = psycopg2.connect(
    host="localhost",
    database="your_db",
    user="postgres",
    password="1234",
    port="5432"
)

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/add")
def add(name: str, feedback: str):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO feedback (name, feedback) VALUES (%s, %s)",
        (name, feedback)
    )
    conn.commit()
    return {"message": "added"}

@app.get("/feedback")
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback;")
    data = cur.fetchall()
    return {"data": data}