cities = {
    'Roma' : {
        'country' : 'Italy', 
        'population' : '2.76 millions',
        'fact' : 'Is the house of Vatican',
        },
    'London' : {
        'country' : 'England',
        'population' : '8.86 millions',
        'fact' : 'It is know as pea soup fog',
        },
    'Paris' : {
        'country' : 'France',
        'population' : '2,1 millions',
        'fact' : 'Paris was originally a Roman City called “Lutetia.”',
         },
    }

for city, cities_info in cities.items():
    print(f"\n City : {city}")
    location = cities_info['country']
    about_city = cities_info['fact']
    people = cities_info['population']

    print(f"\t Country : {location}")    
    print(f"\t Population : {people} of person")
    print(f"\t A fact about : {about_city}")