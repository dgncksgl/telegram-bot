from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from .weather_api_client import get_weather_infos

TOKEN: Final = '7207800798:AAEul7eB_wXj8acGR19sH2MPjXMEQU7Q4AI'


def init_telegram_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, weather_status_reply))
    app.run_polling()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Merhaba, Hoşgeldiniz')
    await update.message.reply_text('Lütfen hava durumunu öğrenmek istediğiniz il adını yazınız.')


async def weather_status_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_weather_infos(update.message.text)

    if data is not None:
        await update.message.reply_text(f"{update.message.text} ili için hava bilgileri şu şekildedir")
        await update.message.reply_text(f"mevcut sıcaklık {data['main']['temp']}°C")
        await update.message.reply_text(f"hissedilen sıcaklık {data['main']['feels_like']}°C")
        await update.message.reply_text(f"maksimum sıcaklık {data['main']['temp_max']}°C")
        await update.message.reply_text(f"minimum sıcaklık {data['main']['temp_min']}°C")
        await update.message.reply_text(f"Hava {data['weather'][0]['description']}")
    else:
        await update.message.reply_text(f"Üzgünüz, uygun veri bulunamadı.")
