sample ='My name is Asfand Yar, I am doing both CA & SE ! What are you doing?'

def split_on_separators(original, separators):
    seplist = list(separators)
    original = original.strip(separators)
    new = []
    for i in seplist:
        original = original.replace( i , '~')
    for check in original:
        if check == '~':
            new = original.split('~')
    print(new)
print(split_on_separators( sample, '.?!'))
