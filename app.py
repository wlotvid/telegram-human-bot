import os
import time
import threading
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# --- Read BOT_TOKEN from environment ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# --- Load model (optional, for AI replies later) ---
MODEL_NAME = "zai-org/GLM-4.7"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

print("Rawan bot model loaded!")

# --- Telegram bot setup ---
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm Rawan 🌸")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "Rawan" in text:  # Only respond if her name is mentioned
        await update.message.reply_text("Hey, you called me? 😳")

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# --- Run Telegram bot in a background thread ---
def run_telegram():
    telegram_app.run_polling()

threading.Thread(target=run_telegram, daemon=True).start()

# --- FastAPI app for Railway ---
api_app = FastAPI()

@api_app.get("/")
def home():
    return {"status": "Rawan bot is online"}
