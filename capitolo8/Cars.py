def build_car(manufacture, model, **car_info):
    """Build a dictionari containing everything we know about cars production"""
    car_info['manufacture'] = manufacture
    car_info['model'] = model
    return car_info

car_profile = build_car('subaru', 'outback', color = 'blue', tow_package = True) 
print(car_profile)