def build_profile(first, last, **userinfo):
    profile = {
        "first_name": first,
        "last_name": last,
    }
    for key, val in userinfo.items():
        profile[key] = val 
    return profile

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}