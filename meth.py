import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from time import sleep



def manga_itens(itens):
        url = "https://neoxscans.net/manga?m_orderby=latest"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}        
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')
        seconds = 5
        sleep(seconds)
        itens = soup.find('div', class_="page-content-listing item-default").find('div', class_="page-listing-item").find('div', class_="row row-eq-height").find('div', class_="col-12 col-md-6 badge-pos-2").find('div', class_="page-item-detail manga").find('h3', class_="h5").find('a')
        return itens

def manga_caplk(link): 
        try:
            link = manga_itens(all)['href']
            return link
        except AttributeError:
            link = "None"
            return link

def filtro(messagefilted):
            try:    
                # rege = r"""[<#|<@&[0-9]+[>]"""
                regex = r"""[<@&]+[0-9]+[>]|[<#].[0-9]+[>]"""
                rege1 = r"""[<@&]+[0-9]+[>]"""
                rege2 = r"""[<#].[0-9]+[>]"""
                subst = "tag"
                subst1 = ""
                if re.finditer(regex, messagefilted, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE):   
                    messagefilted = re.sub(rege1, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege2, subst, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    return messagefilted
            except:
                return messagefilted 
def filtro2(filtro2):
    try:
        filtro2 = re.sub('[**]+','', filtro(filtro2))
        return filtro2
    except:
        return filtro2

def capnumber(messagefilted1):
    regex = r'''
	((Capítulo|Capítulos|Capitulo).([0-9]+.*\|)|-.*[0-9]\|)
	'''
    try:
        if re.finditer(regex ,messagefilted1, re.IGNORECASE | re.MULTILINE | re.VERBOSE | re.DOTALL | re.UNICODE):
            messagefil = re.finditer(regex ,messagefilted1, re.IGNORECASE | re.MULTILINE | re.VERBOSE | re.DOTALL | re.UNICODE)
            for matchNum, match in enumerate(messagefil, start=1):
                messagefilted4 = ("{match}".format( match = match.group()))
                messagefilted2 = [(temp)for temp in messagefilted4.split() if temp.isdigit()]
            try:
                messagefilted1 = messagefilted2
                return messagefilted1
            except:
                pass
    except:
        return messagefilted1


def lin_new(param,linkdefin1):
    linkdefin1 = []
    try:
        for i in range(0,int (len(capnumber(param)))):
            linkdefini = (f'{manga_caplk(any)}'+"/cap-" + f'{capnumber(param)[i]}' )
            linkdefin1.extend([linkdefini])
        return linkdefin1
    except:
        return linkdefin1
