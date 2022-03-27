from telegram import Bot
from keys import *  
import discord
import re 
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

dc = discord.Client()
tg = Bot(token=TELEGRAM_TOKEN)

def Find(string): 
  
    
    
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)       
        return [x[0] for x in url] 

@dc.event
async def on_message(message): 
    if message.channel.id in DISCORD_CHANNELS:
        if message.attachments:
            attachers = ""
            for attachment in message.attachments:
                attachers += f"{attachment} "
            print(f'{message.content} ')
            url = "https://neoxscans.net/?s&post_type=wp-manga&m_orderby=latest"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}        
            req = Request(url,headers=headers)
            response = urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html,'html.parser')

            i=0
            for i in range(0,int (1)):
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]

                def manga_caplk(link): 
                    try:
                        linkk = itens.find_next('span', class_="font-meta chapter")
                        link = linkk.find_next(href=True)
                        return link['href']
                    except AttributeError:
                        link = "None"
                        return link
            
           

            mensagem_tirar = ["<@&553402160378019852>"," <@&952270033961242644>", "<@&870312799191072839>", "<@&952270033961242644>","<@&553402160378019852>","<@&867800588041453583>","<@&867800588041453583>","<@&553402160378019852>" ]
            for i in range(0,int (len(mensagem_tirar))):
                messagefi1 = re.sub(mensagem_tirar[i],'',message.content)

            messagefi1 = re.sub('<#826944584524234754>' ,'#tags',message.content)
            
            tg.sendMessage(TELEGRAM_CHAT_ID, messagefi1 + "\n"  + manga_caplk(all) )

            
            
               
 
            

        else:
            print(f"{message.content}")
            tg.sendMessage(TELEGRAM_CHAT_ID, message.content)

    


def main():
    print("Running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()
