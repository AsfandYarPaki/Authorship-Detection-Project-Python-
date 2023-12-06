text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n','James Gosling\n']

def clean_up_convenient(s):
    string = ''.join(s)
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    temp=string.split()
    readytext=[]
    w=0
    for w in temp:
        readytext= readytext+ [w.lower().strip(punctuation)]
    return readytext


def type_token_ratio(string):
    temp=clean_up_convenient(string)
    dictionary=dict.fromkeys(temp)
    for key in dictionary:
        dictionary[key] = temp.count(key)
    TTR = len(list(dictionary.keys())) / len(temp)
    print (TTR)
