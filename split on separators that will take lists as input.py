sample =['My name is Asfand Yar. I am doing both CA & SE ! What are you doing?']

def split_on_separators(original, separators):
    seplist = list(separators)
    original = original.strip(separators)
    original = ('').join(original)
    new = []
    for i in seplist:
        original = original.replace( i , '~')
    for check in original:
        if check == '~':
            targetlist = original.split('~')
    print(targetlist)
split_on_separators(sample, "!?.")
