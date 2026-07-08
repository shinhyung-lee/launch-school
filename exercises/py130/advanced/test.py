

def song_decoder(string):
    words = string.split("WUB")
    validWords = []
    # print(words)
    for word in words:
        if word != '':
            validWords.append(word)
    
    print(validWords)
    return ' '.join(validWords)
    
# The below tests should each print True.
print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB") == "WE ARE THE CHAMPIONS MY FRIEND")