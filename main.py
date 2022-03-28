from telegram import Bot
from keys import *  
import discord
import re 
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



dc = discord.Client()
tg = Bot(token=TELEGRAM_TOKEN)




@dc.event
async def on_message(message): 
    url = "https://neoxscans.net/?s&post_type=wp-manga&m_orderby=latest"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}        
    req = Request(url,headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    def manga_caplk(link): 
                    try:
                        linkk = itens.find_next('span', class_="font-meta chapter")
                        link = linkk.find_next(href=True)
                        return link['href']
                    except AttributeError:
                        link = "None"
                        return link
    if message.channel.id in DISCORD_CHANNELS:
        if message.attachments:
            attachers = ""
            for attachment in message.attachments:
                attachers += f"{attachment} "
            print(f'{message.content}')
            for i in range(0,int (1)):
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]

                
            messageb = re.sub('<@&'+ '[0-9]+' + '>','', f'{message.content}')
            messagef2 = re.sub('<#826944584524234754>' ,'#tags',messageb)
            messagef2 = re.sub('[**]','',messagef2)
            print(messagef2)
            try:
                tg.sendMessage(TELEGRAM_CHAT_ID, messagef2 + "\n"  + manga_caplk(all) )
                print("Enviado 1")
            except:
                print("Não enviado 1")
        else:
            for i in range(0,int (1)):
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]

                
            messageb = re.sub('<@&'+ '[0-9]+' + '>','', f'{message.content}')
            messagef2 = re.sub('<#826944584524234754>' ,'#tags',messageb)
            messagef2 = re.sub('[**]','',messagef2)
            print(messagef2)
            try:
                tg.sendMessage(TELEGRAM_CHAT_ID, messagef2 + "\n"  + manga_caplk(all) )
                print("Enviado 2")
            except:
                print("Não enviado 2")
        
    


def main():
    print("Running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()
