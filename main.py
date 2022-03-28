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
            linkk = itens.find_next('div', class_="post-title")
            link = linkk.find_next(href=True)
            return link['href']
        except AttributeError:
            link = "None"
            return link

    def filtro(messagefilted):
                if re.findall('<@&'+ '[0-9]+' + '>',messagefilted):
                    messagefilted = re.sub('<@&'+ '[0-9]+' + '>','' , messagefilted)
                    return messagefilted
                if re.findall('<#'+ '[0-9]+' + '>',messagefilted):
                    messagefilted = re.sub('<#'+ '[0-9]+' + '>' ,'tags',messagefilted)
                    return messagefilted
                if re.findall('[**]',messagefilted):
                    messagefilted = re.sub('*','', messagefilted)
                    return messagefilted
                else:
                    return messagefilted 

    def capnumber(messagefilted1):
        if re.findall('Capítulo [0-9]',messagefilted1):
            messagefilted1 = re.sub('Capítulo','', messagefilted1)
            messagefilted1 = [int(temp)for temp in messagefilted1.split() if temp.isdigit()]
            return messagefilted1

    if message.channel.id in DISCORD_CHANNELS:
        if message.attachments:
            attachers = ""
            for attachment in message.attachments:
                attachers += f"{attachment} "
            print(f'{message.content}')
            for i in range(0,int (1)):
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]
            linkdefin1 = []
            for i in range(0,int (len(capnumber(message.content)))):
                linkdefini = (f'{manga_caplk(any)}'+"/cap-" + f'{capnumber(message.content)[i]}' )
                linkdefin1.extend([linkdefini])
            
            lin_new = [str(a) for a in linkdefin1]
            try:
                  tg.sendMessage(TELEGRAM_CHAT_ID, filtro(message.content) + "\n" + "\n". join(lin_new)  )
                  print("Enviado If: " + filtro(message.content) + "\n" + "\n". join(lin_new) )
            except:
                  print("Não enviado if")

        else:
            for i in range(0,int (1)):
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]
            linkdefin1 = []
            try:
                for i in range(0,int (len(capnumber(message.content)))):
                    linkdefini = (f'{manga_caplk(any)}'+"/cap-" + f'{capnumber(message.content)[i]}' )
                    linkdefin1.extend([linkdefini])
            except:
                pass
            lin_new = [str(a) for a in linkdefin1]
            try:
                  tg.sendMessage(TELEGRAM_CHAT_ID, filtro(message.content) + "\n" + "\n". join(lin_new)  )
                  print("Enviado Else: " + filtro(message.content) + "\n" + "\n". join(lin_new) )
            except:
                  print("Não enviado else")

def main():
    print("Running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()