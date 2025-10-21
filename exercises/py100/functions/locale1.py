
# first finding the position of '_' in the original locale string
# then using slicing to extract the language
def extract_language(str: str) -> str:
    underscore_index = str.find('_')
    lang = str[0:underscore_index]
    return lang 

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

# extracting substring from 0(inclusive) to 2(exclusive) using slicing
def extract_language2(str: str) -> str:
    return str[0:2]

print(extract_language2('en_US.UTF-8'))      # en
print(extract_language2('en_GB.UTF-8'))      # en
print(extract_language2('ko_KR.UTF-16'))     # ko

if __name__ == "__main__":
    assert extract_language('en_US.UTF-8') == 'en'
    assert extract_language('ko_KR.UTF-16') == 'ko'
    