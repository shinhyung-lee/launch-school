def display_info(data, /, *, reverse=False, uppercase=False):
    if reverse and uppercase:
        return data[::-1].upper()
    if reverse:
        return data[::-1]
    if uppercase:
        return data.upper()
    return data


print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC