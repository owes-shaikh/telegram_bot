### Importing Required Modules:

```python
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
```

- The script imports necessary modules from the `python-telegram-bot` library, such as `Updater`, `Update`, `CallbackContext`, `CommandHandler`, `MessageHandler`, and `Filters`.

### Initializing the Updater:

```python
updater = Updater("your_own_API_Token got from BotFather", use_context=True)
```

- Creates an instance of the `Updater` class with the Telegram Bot API token obtained from BotFather. The `use_context=True` parameter enables the use of the `CallbackContext` in handlers.

### Command Handler Functions:

```python
def start(update: Update, context: CallbackContext):
    # ... (Welcome message)
    
def help(update: Update, context: CallbackContext):
    # ... (List of available commands)
    
def gmail_url(update: Update, context: CallbackContext):
    # ... (Placeholder for Gmail URL)
    
def youtube_url(update: Update, context: CallbackContext):
    # ... (Sample YouTube link)
    
def linkedIn_url(update: Update, context: CallbackContext):
    # ... (Sample LinkedIn profile link)
    
def geeks_url(update: Update, context: CallbackContext):
    # ... (Sample GeeksforGeeks link)
```

- Defines functions that handle different commands. For example, `/start` displays a welcome message, `/help` lists available commands, and others respond with predefined messages or links.

### Unknown Handlers:

```python
def unknown(update: Update, context: CallbackContext):
    # ... (Handles unknown commands)
    
def unknown_text(update: Update, context: CallbackContext):
    # ... (Handles unknown text messages)
```

- Handles cases where the user inputs an unknown command or text. Provides a response to inform the user.

### Adding Handlers:

```python
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
```

- Associates each command handler function with the corresponding command or message type. For example, `/start` is associated with the `start` function, and unknown text or commands are handled by the `unknown` and `unknown_text` functions.

### Starting the Bot:

```python
updater.start_polling()
```

- Initiates the bot to start listening for updates from Telegram.

### Explanation Summary:

The script sets up a basic Telegram bot with predefined command handlers to respond to specific commands and messages. It uses the `python-telegram-bot` library to facilitate interaction with the Telegram Bot API. Users can interact with the bot by sending commands such as `/start`, `/help`, `/youtube`, `/linkedin`, `/gmail`, and `/geeks`. The script also handles unknown commands and text messages to provide informative responses.
