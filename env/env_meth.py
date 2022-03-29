import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = "https://neoxscans.net"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}        
req = Request(url,headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

# def find_titulo(titulo):
#         titulo = re.findall('A-Za-z *-'  ,titulo)
#         return titulo

def manga_itens(itens):
        tabsitens1 = soup.find('div', class_="row row-eq-height")
        tabsitens2 = tabsitens1.find('div', class_="col-6 col-md-2 badge-pos-2")
        tabsitens3 = tabsitens2.find('div', class_="item-thumb c-image-hover")
        itens = tabsitens3
        return itens

def manga_caplk(link): 
        try:
            linkk = manga_itens(all).find('a')
            link = linkk['href']
            return link
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
        if re.findall('Capítulo [0-9]',messagefilted1):
            messagefilted1 = re.sub('Capítulo' ,'', messagefilted1)
            messagefilted1 = [int(temp)for temp in messagefilted1.split() if temp.isdigit()]
            return messagefilted1
        if re.findall('Capítulos [0-9]',messagefilted1):
            messagefilted1 = re.sub('Capítulos' ,'', messagefilted1)
            messagefilted1 = [int(temp)for temp in messagefilted1.split() if temp.isdigit()]
            return messagefilted1
        if re.findall('Capitulos [0-9]',messagefilted1):
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
