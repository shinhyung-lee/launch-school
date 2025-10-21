

def extract_region(locale: str) -> str:
    underscore_index = locale.find('_')
    period_index = locale.find('.')
    region = locale[underscore_index + 1:period_index]
    return region


if __name__ == "__main__":
    assert extract_region('en_US.UTF-8') == 'US'
    assert extract_region('en_GB.UTF-8') == 'GB'
    assert extract_region('ko_KR.UTF-16') == 'KR'

    print(extract_region('en_US.UTF-8'))    # US
    print(extract_region('en_GB.UTF-8'))    # GB
    print(extract_region('ko_KR.UTF-16'))   # KR
