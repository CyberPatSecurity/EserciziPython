registered_ids = ["Paolo_77","PatrizioEGD", "FranchinoERcriminale", "Achille_Lauro"]

lower_registered_ids = [user_ids.lower() for user_ids in registered_ids]

new_registered_ids = ["paolo_77","PatrizioEGD", "andrea", "alessia"]

for new_user in new_registered_ids:
    if new_user.lower() in lower_registered_ids:
        print(f"{new_user} is already in use, try another one!")
    else:
        print(f"{new_user} is available!")

