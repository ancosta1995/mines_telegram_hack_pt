from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters
#import json
from core import sendVideo, response

TOKEN_BOT = '7795577887:AAEiKujadZF94J9d3PzIm6gIE_KpqkoE3Nk'
PATH_VIDEO = 'assets/videos/'

async def start_no_register(update, context) -> None:
    text = f"✍🏼 INSIRA O ID DA SUA CONTA DA CASA DE APOSTA NO CHAT:\n\n👇 Se você não possui uma conta, clique no botão para criar uma:\n\n⭐️ USE CÓDIGO PROMOCIONAL PRIVADO PARA OBTER BÔNUS DE 500% E RODADAS GRATUITAS: MNS24GPT"
    video_path = PATH_VIDEO + 'register.mp4'
    button = ['📎REGISTRO', 'https://bonus-betando.com/registro']
    await sendVideo(text, video_path, update, button)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start_no_register(update, context)

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = f"💣 Minas\n\n📝 Descrição:\nUm jogo em que você deve adivinhar as estrelas que não possuem minas. Para cada célula aberta você ganha dinheiro.\n\n🤖 Existe um hack bot disponível para este jogo, que mostra estrelas sem minas."
    await response(update, text, True)

# Configuração do bot
def main():
    app = ApplicationBuilder().token(TOKEN_BOT).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex(r"^\d{9}$"), get_id))
    #app.add_handler(CallbackQueryHandler(start_bot, pattern="start_bot"))

    print("Bot está rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()