# Import necessary modules from the python-telegram-bot library
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# Initialize the Updater with your Telegram Bot API token obtained from BotFather
updater = Updater("your_own_API_Token got from BotFather", use_context=True)

# Command handler function for the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot. Please write /help to see the available commands."
    )

# Command handler function for the /help command
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands:-
    /youtube - To get the YouTube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get the Gmail URL
    /geeks - To get the GeeksforGeeks URL
    """)

# Command handler function for the /gmail command
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your Gmail link here (I am not giving mine for security reasons)"
    )

# Command handler function for the /youtube command
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("YouTube Link => https://www.youtube.com/")

# Command handler function for the /linkedin command
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/"
    )

# Handler for unknown commands
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text
    )

# Handler for unknown text messages
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry, I can't recognize you. You said '%s'" % update.message.text
    )

# Add handlers for different commands and messages
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# Start polling to receive updates from Telegram
updater.start_polling()
