import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = "https://neoxscans.net/?s&post_type=wp-manga&m_orderby=latest"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}        
req = Request(url,headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

def find_titulo(titulo):
        titulo = re.findall('A-Za-z *-'  ,titulo)
        return titulo

def manga_itens(itens):
    for i in range(0,int (1)):
        tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
        itens = tabsitens[i]
    return itens

def manga_caplk(link): 
        try:
            linkk = manga_itens(all).find_next('div', class_="post-title")
            link = linkk.find_next(href=True)
            return link['href']
        except AttributeError:
            link = "None"
            return link

def filtro(messagefilted):
                try:
                    if  re.findall('<@&'+ '[0-9]+' + '>',messagefilted):
                        messagefilted = re.sub('<@&'+ '[0-9]+' + '>','' , messagefilted)
                        return messagefilted
                except:
                    return messagefilted

                try:
                    if re.findall('<#'+ '[0-9]+' + '>',messagefilted):
                       messagefilted = re.sub('<#'+ '[0-9]+' + '>' ,'tags',messagefilted)
                       return messagefilted
                except:
                    return messagefilted
                try:
                    if re.search('[**A-Z]' or '[**]',messagefilted):
                        messagefilted = re.sub('[**]','', messagefilted)
                        return messagefilted
                except:
                    return messagefilted
                return messagefilted

def filtro2(filtro2):
    try:
        filtro2 = re.sub('[**]','', filtro(filtro2))
        return filtro2
    except:
        return filtro2

def capnumber(messagefilted1):
    try:
        if re.findall('Capítulo [0-9]+' or 'Capítulos [0-9]+' or 'Capitulos [0-9]+',messagefilted1):
            messagefilted1 = re.sub('Capítulo' or 'Capítulos'or 'Capitulos' ,'', messagefilted1)
            messagefilted1 = [int(temp)for temp in messagefilted1.split() if temp.isdigit()]
            return messagefilted1
        if re.findall('Capítulos [0-9]+' or 'Capitulos [0-9]+',messagefilted1):
            messagefilted1 = re.sub('Capítulos' ,'', messagefilted1)
            messagefilted1 = [int(temp)for temp in messagefilted1.split() if temp.isdigit()]
            return messagefilted1
        if re.findall('Capitulos [0-9]+',messagefilted1):
            messagefilted1 = re.sub('Capitulos' ,'', messagefilted1)
            messagefilted1 = [int(temp)for temp in messagefilted1.split() if temp.isdigit()]
            return messagefilted1
    except:
        return messagefilted1
            
def lin_new(param1,linkdefin1):
    linkdefin1 = []
    try:
        for i in range(0,int (len(capnumber(param1)))):
            linkdefini = (f'{manga_caplk(any)}'+"/cap-" + f'{capnumber(param1)[i]}' )
            linkdefin1.extend([linkdefini])
        return linkdefin1
    except:
        return linkdefin1
