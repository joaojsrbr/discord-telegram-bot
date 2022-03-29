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
                attachers += f"{attachment} "
            print(f'{message.content}')
                             
            link_ne = [str(a) for a in lin_new(message.content,all)]
        
            #print("Enviado 'If': " + filtro2(message.content) + "\n" + "\n". join(link_ne))
            
            try:
                   tg.sendMessage(TELEGRAM_CHAT_ID, filtro2(message.content) + "\n" + "\n". join(link_ne) )
                   print("Enviado If: " + filtro2(message.content) + "\n" + "\n". join(link_ne) )
            except:
                   print("Não enviado 'If'")

        else:
                       
            link_ne = [str(a) for a in lin_new(message.content,all)]
        
            #print("Enviado 'Else': " + filtro2(message.content) + "\n" + "\n". join(link_ne))
                        
            try:
                   tg.sendMessage(TELEGRAM_CHAT_ID, filtro2(message.content) + "\n" + "\n". join(link_ne) )
                   print("Enviado Else: " + filtro2(message.content) + "\n" + "\n". join(link_ne) )
            except:
                   print("Não enviado 'else'")

def main():
    print("Running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()