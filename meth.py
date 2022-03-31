import re


def filtro(messagefilted):
            try:    
                regex = r"""[<@&]+[0-9]+[>]|[<#].[0-9]+[>]|[<@!]+[0-9]+[>]|[<:a-z_0-9A-Z:|<@!0-9]+[>]|(POSTADO!!!)"""
                rege1 = r"""[<@&]+[0-9]+[>]"""
                rege2 = r"""[<#].[0-9]+[>]"""
                rege3 = r"""[<:a-z_0-9A-Z:|<@!0-9]+[>]"""
                rege4 = r"""[<@!]+[0-9]+[>]"""
                rege5 = r"""(POSTADO!!!)"""
                subst = "tag"
                subst1 = ""
                subst2 = "#POSTADO"
                if re.finditer(regex, messagefilted, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE):   
                    messagefilted = re.sub(rege1, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege2, subst, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege3, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)                    
                    messagefilted = re.sub(rege4, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege5, subst2, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    return messagefilted
            except:
                return messagefilted 


