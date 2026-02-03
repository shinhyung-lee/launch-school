def build_profile(first, last, **kwargs):
    profile = {
        "first_name": first,
        "last_name": last,
    }
    for key, val in kwargs.items():
        profile[key] = val 
    return profile

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}