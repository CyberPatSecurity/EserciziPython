def build_profile(first, last, **user_info):
    """Build a dictionari containing everything we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Patrizio', 'Egidi', location = 'Roma', field ='Computer science', hobby = 'programming language')

print(user_profile)