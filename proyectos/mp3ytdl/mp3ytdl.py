import youtube_dl
import os
import logging
import re
import threading
from os import remove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from idtoken import token

#token = "1134841999:AAGYVikHzXPdgk3tKqxoBLwZofy82a-g4Mk"

# Url where the project is hosted mp3ytdl.py
path = "www.leoleiva.ar/proyectos"

# If deletefile is true, delete the file, if you don't want it to be deleted, put False
deletefile = True


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class MyLogger(object): #youtube_dl log
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d): #converting message
    if d['status'] == 'finished':
	    print('Descarga completada, convirtiendo mp3...')

#        if numdescarga is not None:
#            numdescarga += 1
#        else:
#            numdescarga = 0
#            numdescarga += 1

def downloader(url): # download file config
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info = ydl.extract_info(url, download=False)

    global titulo
    titulo = info['title']
    global numid
    numid = info['id']
    global link
    link = titulo + "-" + numid + ".mp3"


def getMusic(update, context): #main function
    test = update.message.text
    pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
    
    rtest = re.findall(pattern, test, re.MULTILINE | re.IGNORECASE)
    
    if rtest:
        url = "https://www.youtube.com/watch?v=" + str(rtest[0])
    else:
        url = ""
        
    checkYtube = "https://www.youtube.com" # check youtube url
    if (url.startswith(checkYtube)): # check youtube url
        update.message.reply_text('Espere hasta que se extraiga el audio...')
        if "&" in url: 
            url = url.split("&")[0] 
        if not os.path.exists("singleMusic"):  #confirm the folder isn't exist 
            os.makedirs("singleMusic") # build a folder to put .mp3 file
        os.chdir("singleMusic") # change dir (cd)
        downloader(url)
        os.chdir("../") # change dir (cd) pwd: {/}
        descargar = "Listo: puedes abrirlo en el navegador haciendo <a href='" + path + "/mp3ytdl/singleMusic/" + link + "'>Click aqui</a>"
        update.message.reply_text(descargar, parse_mode='HTML',)
        incrementa_elemento(numero)
        print(numero[0])
        
        
        if deletefile == True:
            update.message.reply_text('El archivo durara solo 30 minutos en nuestro servidor, luego se borrara')
        
            # File delete function
            def borrado(link, titulo):
                remove("singleMusic/" + link)
                update.message.reply_text('Se borro el archivo ' + titulo)

            # duration in seconds
            t = threading.Timer(1800.0, borrado, (link,titulo,))
            t.start()
            
            

    else:
        update.message.reply_text('Por favor ingrese un link de youtube para descargar el mp3. Presione /help para pedir ayuda')

    
    
        
def incrementa_elemento(n):
    n[0]+=1

# Programa principal
numero = [0]   # No necesita ser global
        
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola para obtener ayuda presione /help y le explicaremos como descargar un mp3 de YouTube')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Para descargar un MP3 de Youtube simplemente pegue la direccion del video, por ejemplo: https://www.youtube.com/watch?v=kg1BljLu9YY')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def numdescargas(update, context):
    update.message.reply_text('Numero de descargas: ' + str(numero[0]))


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("numdescargas", numdescargas))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, getMusic))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


    


if __name__ == '__main__':
	main()