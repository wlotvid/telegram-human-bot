import time
from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi import FastAPI
import threading

MODEL_NAME = "zai-org/GLM-4.7"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

print("Rawan bot is online and running...")

# Background loop to keep the bot alive
def run_bot_loop():
    while True:
        time.sleep(60)

threading.Thread(target=run_bot_loop, daemon=True).start()

# Minimal FastAPI app to satisfy Railway
app = FastAPI()

@app.get("/")
def home():
    return {"status": "Rawan bot is online"}
