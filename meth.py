import re


def filtro(messagefilted):
            try:    
                regex = r"""[<@&]+[0-9]+[>]|[<#].[0-9]+[>]|[<@!]+[0-9]+[>]|[<:a-z_=-A-Z:]+[0-9]+[>]"""
                rege1 = r"""[<@&]+[0-9]+[>]"""
                rege2 = r"""[<#].[0-9]+[>]"""
                rege3 = r"""[<:a-z_=-A-Z:]+[0-9]+[>]"""
                rege4 = r"""[<@!]+[0-9]+[>]"""
                subst = "tag"
                subst1 = ""
                if re.finditer(regex, messagefilted, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE):   
                    messagefilted = re.sub(rege1, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege2, subst, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege3, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    messagefilted = re.sub(rege4, subst1, messagefilted, 0, re.MULTILINE | re.IGNORECASE | re.VERBOSE | re.DOTALL | re.UNICODE)
                    return messagefilted
            except:
                return messagefilted 


