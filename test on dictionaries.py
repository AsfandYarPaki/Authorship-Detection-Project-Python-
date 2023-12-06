temp= ['james', 'fennimore', 'cooper', 'peter', 'paul', 'and', 'mary', 'james',
       'gosling']
def type_token_ratio(string):
    dictionary=dict.fromkeys(temp)
    for key in dictionary:
        dictionary[key]= temp.count(key)
    return dictionary
        
print(type_token_ratio(temp))
