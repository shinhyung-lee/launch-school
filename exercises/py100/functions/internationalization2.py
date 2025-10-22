

# use extract_language, extract_region, and greet functions
def extract_language(locale: str) -> str:
    return locale.split('_', 1)[0]

def greet(lang):
    match lang:
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'Hi!'

def extract_region(locale: str) -> str:
    underscore_index = locale.find('_')
    period_index = locale.find('.')
    region = locale[underscore_index + 1:period_index]
    return region

def local_greet(locale: str) -> str:
    # if language is english, put them in their own match-case
    # if language is not english, use greet function. 
    language = extract_language(locale)
    if language == 'en':
        region = extract_region(locale)
        match region:
            case 'US':
                return 'Hey!'
            case 'GB':
                return 'Hello!'
            case 'AU':
                return 'Howdy!'
            case 'CA':
                return 'How\'s she goin?'
            case _:
                return 'Hi!'
    else:
        return greet(language)

if __name__ == "__main__":
    print(local_greet('en_US.UTF-8'))       # Hey!
    print(local_greet('en_GB.UTF-8'))       # Hello!
    print(local_greet('en_AU.UTF-8'))       # Howdy!

    print(local_greet('fr_FR.UTF-8'))       # Salut!
    print(local_greet('fr_CA.UTF-8'))       # Salut!
    print(local_greet('fr_MA.UTF-8'))       # Salut!












