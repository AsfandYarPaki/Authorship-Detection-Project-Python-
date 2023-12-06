sample ='My name is Asfand Yar, I am doing both CA & SE ! What are you doing?'

text = ['The time has come, the Walrus said\n',
        'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']


def split_on_separators(original, separators):
    original = ('').join(original)
    original = original.strip('\n')
    
    for i in separators:
        original = original.strip(i)

    print( original )
    
split_on_separators(text, '?!.')
