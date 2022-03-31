import re
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m")

def filtro(messagefilted):
            try:    
                regex = r"""([<@&|<#]+[0-9]+|[>])|[<#].[0-9]+[>]|[<@!]+[0-9]+[>]|([:|<|]+[a-z|a-z_]+[:]+[0-9]+)|([<|@!]+[0-9]+)|(POSTADO!!!)|(<https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"""
                rege1 = r"""([<@&]+[0-9]+|[>])"""
                rege2 = r"""([<#]+[0-9]+|[>])"""
                rege3 = r"""([:|<|]+[a-z|a-z_]+[:]+[0-9]+)|([<|@!]+[0-9]+)"""
                rege4 = r"""[<@!]+[0-9]+[>]"""
                rege5 = r"""(POSTADO!!!)"""
                rege6 = r'''(<https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'''
                subst = "tag"
                subst1 = ""
                subst2 = "#POSTADO"
                subst3 = r'''(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s^\>]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s^\>]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s^\>]{2,}|www\.[a-zA-Z0-9]+\.[^\s^\>]{2,})'''
                if re.finditer(regex, messagefilted, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE):   
                    messagefilted = re.sub(rege1, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege2, subst, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege3, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)                    
                    messagefilted = re.sub(rege4, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege5, subst2, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege6, subst3, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    return messagefilted
            except:
                return messagefilted 


