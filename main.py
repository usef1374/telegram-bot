from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8038971157:AAFL-xQ38j0enmqpSMtJMeqJWvPyqHlGZ9A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("œò„Â ?", callback_data='button1')],
        [InlineKeyboardButton("œò„Â ?", callback_data='button2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("»Â —»«  ŒÊ‘ ¬„œ?œ! ê“?‰Âù«? —« «‰ Œ«» ò‰?œ:", reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'button1':
        await query.edit_message_text(text="‘„« œò„Â ? —« “œ?œ!")
    elif query.data == 'button2':
        await query.edit_message_text(text="‘„« œò„Â ? —« “œ?œ!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("—»«  «Ã—« ‘œ!")
    app.run_polling()