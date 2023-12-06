sample = "Hooray! Finally, we're done."

def split_on_separators(original, separators):
    original = ('').join(original)
    seplist = list(separators)
    original = original.strip('\n')
    original = original.strip(separators)
    
    for i in seplist:
        original = original.replace( i , '~')
    for check in original:
        if check == '~':
            targetlist = original.split('~')
    return (targetlist)
print(split_on_separators(sample, "!,"))
