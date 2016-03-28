#Freia Lobo - fll220@nyu.edu - Homework #9 Problem #4
coded = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

cypher = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s',
'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 
's':'f', 't': 'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 
'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 
'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P': 'C', 
'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def decode(message,key):
    decoded = ''
    for char in message:
        if char.isalpha():

            decoded+=key.get(char)
        else:
            decoded+=char
    return decoded

answer = decode(coded, cypher)
print(answer)
