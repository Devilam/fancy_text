import re

class fancy(object):
    def bold(text):
        fancy_bold = { 
                    'a' : '\uD835\uDD86'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'b' : '\uD835\uDD87'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'c' : '\uD835\uDD88'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'd' : '\uD835\uDD89'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'e' : '\uD835\uDD8A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'f' : '\uD835\uDD8B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'g' : '\uD835\uDD8C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'h' : '\uD835\uDD8D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'i' : '\uD835\uDD8E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'j' : '\uD835\uDD8F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'k' : '\uD835\uDD90'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'l' : '\uD835\uDD91'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'm' : '\uD835\uDD92'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'n' : '\uD835\uDD93'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'o' : '\uD835\uDD94'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'p' : '\uD835\uDD95'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'q' : '\uD835\uDD96'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'r' : '\uD835\uDD97'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    's' : '\uD835\uDD98'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    't' : '\uD835\uDD99'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'u' : '\uD835\uDD9A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'v' : '\uD835\uDD9B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'w' : '\uD835\uDD9C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'x' : '\uD835\uDD9D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'y' : '\uD835\uDD9E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'z' : '\uD835\uDD9F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'A' : '\uD835\uDD6C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'B' : '\uD835\uDD6D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'C' : '\uD835\uDD6E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'D' : '\uD835\uDD6F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'E' : '\uD835\uDD70'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'F' : '\uD835\uDD71'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'G' : '\uD835\uDD72'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'H' : '\uD835\uDD73'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'I' : '\uD835\uDD74'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'J' : '\uD835\uDD75'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'K' : '\uD835\uDD76'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'L' : '\uD835\uDD77'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'M' : '\uD835\uDD78'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'N' : '\uD835\uDD79'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'O' : '\uD835\uDD7A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'P' : '\uD835\uDD7B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Q' : '\uD835\uDD7C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'R' : '\uD835\uDD7D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'S' : '\uD835\uDD7E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'T' : '\uD835\uDD7F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'U' : '\uD835\uDD80'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'V' : '\uD835\uDD81'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'W' : '\uD835\uDD82'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'X' : '\uD835\uDD83'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Y' : '\uD835\uDD84'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Z' : '\uD835\uDD85'.encode('utf-16', 'surrogatepass').decode('utf-16')
                    }
        pattern = re.compile(r'(' + '|'.join(fancy_bold.keys()) + r')')
        result = pattern.sub(lambda x: fancy_bold[x.group()], text)
        return(result)


    def light(text):
        fancy_light = { 
                    'a' :  '\uD835\uDD1E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'b' : '\uD835\uDD1F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'c' : '\uD835\uDD20'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'd' : '\uD835\uDD21'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'e' : '\uD835\uDD22'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'f' : '\uD835\uDD23'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'g' : '\uD835\uDD24'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'h' : '\uD835\uDD25'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'i' : '\uD835\uDD26'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'j' : '\uD835\uDD27'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'k' : '\uD835\uDD28'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'l' : '\uD835\uDD29'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'm' : '\uD835\uDD2A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'n' : '\uD835\uDD2B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'o' : '\uD835\uDD2C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'p' : '\uD835\uDD2D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'q' : '\uD835\uDD2E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'r' : '\uD835\uDD2F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    's' : '\uD835\uDD30'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    't' : '\uD835\uDD31'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'u' : '\uD835\uDD32'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'v' : '\uD835\uDD33'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'w' : '\uD835\uDD34'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'x' : '\uD835\uDD35'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'y' : '\uD835\uDD36'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'z' : '\uD835\uDD37'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'A' : '\uD835\uDD04'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'B' : '\uD835\uDD05'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'C' : '\u212D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'D' : '\uD835\uDD07'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'E' : '\uD835\uDD08'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'F' : '\uD835\uDD09'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'G' : '\uD835\uDD0A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'H' : '\u210C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'I' : '\u2111'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'J' : '\uD835\uDD0D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'K' : '\uD835\uDD0E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'L' : '\uD835\uDD0F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'M' : '\uD835\uDD10'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'N' : '\uD835\uDD11'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'O' : '\uD835\uDD12'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'P' : '\uD835\uDD13'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Q' : '\uD835\uDD14'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'R' : '\u211C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'S' : '\uD835\uDD16'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'T' : '\uD835\uDD17'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'U' : '\uD835\uDD18'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'V' : '\uD835\uDD19'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'W' : '\uD835\uDD1A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'X' : '\uD835\uDD1B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Y' : '\uD835\uDD1C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Z' : '\u2128'.encode('utf-16', 'surrogatepass').decode('utf-16'),
        }
        pattern = re.compile(r'(' + '|'.join(fancy_light.keys()) + r')')
        result = pattern.sub(lambda x: fancy_light[x.group()], text)
        return(result)

    def box(text):
        fancy_box = { 
                    'a' : '\uD83C\uDD70'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'b' : '\uD83C\uDD71'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'c' : '\uD83C\uDD72'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'd' : '\uD83C\uDD73'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'e' : '\uD83C\uDD74'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'f' : '\uD83C\uDD75'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'g' : '\uD83C\uDD76'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'h' : '\uD83C\uDD77'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'i' : '\uD83C\uDD78'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'j' : '\uD83C\uDD79'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'k' : '\uD83C\uDD7A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'l' : '\uD83C\uDD7B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'm' : '\uD83C\uDD7C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'n' : '\uD83C\uDD7D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'o' : '\uD83C\uDD7E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'p' : '\uD83C\uDD7F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'q' : '\uD83C\uDD80'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'r' : '\uD83C\uDD81'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    's' : '\uD83C\uDD82'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    't' : '\uD83C\uDD83'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'u' : '\uD83C\uDD84'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'v' : '\uD83C\uDD85'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'w' : '\uD83C\uDD86'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'x' : '\uD83C\uDD87'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'y' : '\uD83C\uDD88'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'z' : '\uD83C\uDD89'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'A' : '\uD83C\uDD70'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'B' : '\uD83C\uDD71'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'C' : '\uD83C\uDD72'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'D' : '\uD83C\uDD73'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'E' : '\uD83C\uDD74'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'F' : '\uD83C\uDD75'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'G' : '\uD83C\uDD76'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'H' : '\uD83C\uDD77'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'I' : '\uD83C\uDD78'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'J' : '\uD83C\uDD79'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'K' : '\uD83C\uDD7A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'L' : '\uD83C\uDD7B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'M' : '\uD83C\uDD7C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'N' : '\uD83C\uDD7D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'O' : '\uD83C\uDD7E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'P' : '\uD83C\uDD7F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Q' : '\uD83C\uDD80'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'R' : '\uD83C\uDD81'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'S' : '\uD83C\uDD82'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'T' : '\uD83C\uDD83'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'U' : '\uD83C\uDD84'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'V' : '\uD83C\uDD85'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'W' : '\uD83C\uDD86'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'X' : '\uD83C\uDD87'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Y' : '\uD83C\uDD88'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                    'Z' : '\uD83C\uDD89'.encode('utf-16', 'surrogatepass').decode('utf-16')
                }
        pattern = re.compile(r'(' + '|'.join(fancy_box.keys()) + r')')
        result = pattern.sub(lambda x: fancy_box[x.group()], text)
        return result

    def sorcerer(text):
        fancy_sorcerer = {
        'a' : '\u01DF',
        'b' : '\u026E',
        'c' : '\u0188',
        'd' : '\u0256',
        'e' : '\u025B',
        'f' : '\u0284',
        'g' : '\u0262',
        'h' : '\u0266',
        'i' : '\u0268',
        'j' : '\u029D',
        'k' : '\u04C4',
        'l' : '\u029F',
        'm' : '\u028D',
        'n' : '\u057C',
        'o' : '\u0585',
        'p' : '\u0584',
        'q' : '\u0566',
        'r' : '\u0280',
        's' : '\u0586',
        't' : '\u0236',
        'u' : '\u028A',
        'v' : '\u028B',
        'w' : '\u0561',
        'x' : '\u04FC',
        'y' : '\u028F',
        'z' : '\u0290',
        'A' : '\u01DF',
        'B' : '\u026E',
        'C' : '\u0188',
        'D' : '\u0256',
        'E' : '\u025B',
        'F' : '\u0284',
        'G' : '\u0262',
        'H' : '\u0266',
        'I' : '\u0268',
        'J' : '\u029D',
        'K' : '\u04C4',
        'L' : '\u029F',
        'M' : '\u028D',
        'N' : '\u057C',
        'O' : '\u0585',
        'P' : '\u0584',
        'Q' : '\u0566',
        'R' : '\u0280',
        'S' : '\u0586',
        'T' : '\u0236',
        'U' : '\u028A',
        'V' : '\u028B',
        'W' : '\u0561',
        'X' : '\u04FC',
        'Y' : '\u028F',
        'Z' : '\u0290'

    }
        pattern = re.compile(r'(' + '|'.join(fancy_sorcerer.keys()) + r')')
        result = pattern.sub(lambda x: fancy_sorcerer[x.group()], text)
        return(result)
        
