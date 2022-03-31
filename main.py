from telegram import Bot
from keys import *
import discord
from meth import *


dc = discord.Client()
tg = Bot(token=TELEGRAM_TOKEN)




@dc.event
async def on_message(message): 
    if message.channel.id in DISCORD_CHANNELS:
        if message.attachments:
            attachers = ""
            for attachment in message.attachments:
                attachers += f"{attachment}"
            
            try:
                   tg.send_photo(TELEGRAM_CHAT_ID,  f"{attachment}" , caption=filtro(message.content), parse_mode='Markdown',  )
                   print("Enviado F-M: " + filtro(message.content) + "\n " + f"{attachment}" )
            except:
                   print("Não enviado 'If'")

        else:                      
            try:
                tg.sendMessage(TELEGRAM_CHAT_ID,  filtro(message.content), parse_mode='Markdown',disable_web_page_preview=True)
                print("Enviado M: " + filtro(message.content))
            except:
                   print("Não enviado 'else'")
        

def main():
    print("Running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()