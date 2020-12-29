''' 
Wiki Parser - The program searches Wikipedia and fetches a random article for the user to read. 

Then it asks the user if he wants to read that article or not. If the answer is yes, the material
is shown; otherwise, another random report is presented.

'''


import wikipedia

# Step 1: Create function to fetch random article from wikipedia (How do we recommend the page? By Title)

def wiki_gen():
    result = wikipedia.random(pages=1)
    return result
  
article = wiki_gen()
print(article)
print("")


# Step 2: Ask user to read article or not

print('Would you like to read "{}" (Type "yes" to read or "no" to recommend another)?'.format(article))
another_article = input()


# Step 3: If yes, show selected article, if no move to next article

if (another_article == 'Yes'.lower()):
    print('Thank you for reading')

if(another_article == 'no'.lower()):
    print('Searching for another article...')
    print("")
    article = wiki_gen()
    print(article)
    
    # Generator Loop
    while (another_article == 'no'.lower()):
        print('Would you like to read "{}" (Type "yes" to read or "no" to recommend another)?'.format(article))
        another_article = input()
        print('Searching for another article...')
        print("")
        article = wiki_gen()
        print(article)
    
else:
    print('End program')
    