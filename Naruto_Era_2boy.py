import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Welcome to Hugh West Gaming Bot!\n\n"
        "Your ultimate gaming community starts here.\n\n"
        "Commands:\n"
        "/games - View supported games\n"
        "/quiz - Gaming quiz\n"
        "/profile - Player profile\n"
        "/rank - Player rankings\n"
        "/help - Show commands"
    )


async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 SUPPORTED GAMES\n\n"
        "🔥 Free Fire\n"
        "🎯 Blood Strike\n"
        "🔫 PUBG Mobile\n"
        "⚽ eFootball\n"
        "More games coming soon!"
    )


async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 GAMING QUIZ\n\n"
        "Which company developed Free Fire?\n\n"
        "A) Garena\n"
        "B) Tencent\n"
        "C) Konami\n\n"
        "Reply A, B, or C!"
    )


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👤 PLAYER PROFILE\n\n"
        f"Name: {user.first_name}\n"
        f"Telegram ID: {user.id}\n"
        f"Username: @{user.username or 'Not set'}"
    )


async def rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 PLAYER RANKINGS\n\n"
        "The leaderboard is coming soon!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/games - List games\n"
        "/quiz - Gaming quiz\n"
        "/profile - View your profile\n"
        "/rank - View rankings\n"
        "/help - Show help"
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("games", games))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("rank", rank))
    app.add_handler(CommandHandler("help", help_command))

    print("Hugh West Gaming Bot is running!")
    app.run_polling()


if __name__ == "__main__":
    main()
