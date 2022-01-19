#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import requests
from clave import idtoken
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard = [[InlineKeyboardButton("Dolar", callback_data="dolar"),
                 InlineKeyboardButton("Dolar Blue", callback_data="dolarblue")],

                [InlineKeyboardButton("Euro", callback_data="euro"),
                InlineKeyboardButton("Euro Blue", callback_data="euroblue")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Que cotizacion deseas:', reply_markup=reply_markup, parse_mode='HTML',)


def button(update, context):
    query = update.callback_query

    r = requests.get('http://api.bluelytics.com.ar/v2/latest').json()

    #Rescatando datos del dolar oficial
    oficompra = float(r["oficial"]['value_buy'])
    coficompra = '%.2f' %oficompra
    ofiventa = float(r["oficial"]['value_sell'])
    cofiventa = '%.2f' %ofiventa
    soli = float(ofiventa + (ofiventa*0.65))
    csoli = '%.2f' %soli
    
    #rescatando datos del dolar blue
    bluecompra = float(r["blue"]['value_buy'])
    cbluecompra = '%.2f' %bluecompra
    blueventa = float(r["blue"]['value_sell'])
    cblueventa= '%.2f' %blueventa
    
    #Rescatando datos del euro
    eoficompra = float(r["oficial_euro"]['value_buy'])
    ceoficompra = '%.2f' %eoficompra
    eofiventa = float(r["oficial_euro"]['value_sell'])
    ceofiventa = '%.2f' %eofiventa
    esoli = float(eofiventa + (eofiventa*0.65))
    cesoli = '%.2f' %esoli
    
    #Rescatando datos del euro blue
    ebluecompra = float(r["blue_euro"]['value_buy'])
    cebluecompra = '%.2f' %ebluecompra
    eblueventa = float(r["blue_euro"]['value_sell'])
    ceblueventa = '%.2f' %eblueventa
    timeupdate = str(r["last_update"])


    dolar = "U$S Oficial Compra      | "  + str(coficompra) + "\n\n"
    dolar += "U$S Oficial Venta         | " + str(cofiventa) + "\n\n"
    dolar += "U$S Oficial C/Imp. incluido | " + str(csoli) + "\n\n"

    dolarblue = "U$S Blue Compra      | "  + str(cbluecompra) + "\n\n"
    dolarblue += "U$S Blue Venta         | " + str(cblueventa) + "\n\n"

    euro = "Euro Oficial Compra      | "  + str(ceoficompra) + "\n\n"
    euro += "Euro Oficial Venta         | " + str(ceofiventa) + "\n\n"
    euro += "Euro Oficial C/Imp. Pais | " + str(cesoli) + "\n\n"
    
    euroblue = "Euro Blue Compra      | "  + str(cebluecompra) + "\n\n"
    euroblue += "Euro Blue Venta         | " + str(ceblueventa) + "\n\n"

    actualizacion = "Ultima Actualizacion: " + timeupdate[:10] + " | Hora: " + timeupdate[11:19]
    
    if query.data == "dolar":
        query.edit_message_text(text=dolar + actualizacion + "\n\n Click en /start para elegir otra cotizacion")
    elif query.data == "dolarblue":
        query.edit_message_text(text=dolarblue + actualizacion + "\n\n Click en /start para elegir otra cotizacion")
    elif query.data == "euro":
        query.edit_message_text(text=euro + actualizacion + "\n\n Click en /start para elegir otra cotizacion")
    elif query.data == "euroblue":
        query.edit_message_text(text=euroblue + actualizacion + "\n\n Click en /start para elegir otra cotizacion")


def help(update, context):
    update.message.reply_text("Use /start para obtener las opciones de cotizacion")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(idtoken, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
