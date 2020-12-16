import pyjokes

print(help(pyjokes))
joke = pyjokes.get_jokes('en', 'neutral')
print(joke)
