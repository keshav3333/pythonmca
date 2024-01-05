class AnilInterrupt(Exception):
    pass

try:
    a=input('enter a string:- ')

    if a[0] in 'aeiouAEIOU':
        raise AnilInterrupt ('first char should not be a vowel')
    
except AnilInterrupt:
    print('error handled')
