current_users = ['MIERVOLINO','Mbruscella','Admin','Amauti','Lfancelli']
lower_current_users = [user.lower() for user in current_users]

new_users = ['Miervolino','Mlangella','Lfancelli','Emvalentino','Rmangialavori']

for user in new_users:
    if user.lower() in lower_current_users:
        print("This username is already in use, try another one!")
    else:
        print("The username is available!")