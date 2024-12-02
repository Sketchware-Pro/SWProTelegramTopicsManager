import asyncio
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

# Get the bot token from environment variable
TOKEN = os.getenv('SWPRO_TELEGRAM_BOT_TOKEN')
CHAT_ID = '-1001427104411'

# Dictionary to hold topic IDs and allowed user IDs
allowed_users_by_topic = {
    f"{CHAT_ID}_278732": [ # Contributors Only
        651390997,   # @ilyassesalama
        776148634,   # @Mu_Sa101
        6455223969,  # @trindadedev
        6539284752,  # @elfilibusterismo_inc
        1608453750,  # @Bobur4ik05
        1013653102,  # @jkhon
        6841473609,  # @ishak_mes
        1752763139,  # @aikrqq
        1493547431,  # @PranavPurwar
        6148526102,  # @HasratAKhan
        1350857656,  # @nethicalps
    ],
}

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message

    if message and message.message_thread_id:
        topic_id = f"{message.chat.id}_{message.message_thread_id}"

        if topic_id in allowed_users_by_topic:
            if message.from_user.id not in allowed_users_by_topic[topic_id]:
                await message.delete()
    else:
        pass

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, check_message))
    app.run_polling(poll_interval=0.1, timeout=10)

if __name__ == '__main__':
    main()
