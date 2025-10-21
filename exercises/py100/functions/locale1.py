
# first finding the position of '_' in the original locale string
# then using slicing to extract the language
def extract_language(locale: str) -> str:
    return locale.split('_', 1)[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

def extract_language2(locale: str) -> str:
    # before, partition, after 
    lang, _, _ = locale.partition('_')
    return lang

if __name__ == "__main__":
    assert extract_language('en_US.UTF-8') == 'en'
    assert extract_language('ko_KR.UTF-16') == 'ko'

    assert extract_language2('en_US.UTF-8') == 'en'
    assert extract_language2('ko_KR.UTF-16') == 'ko'
    