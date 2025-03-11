def make_album(artist_name, album_name):
    """return a dictionary with pair Artist:Album"""
    artist = f"{artist_name} and {album_name}"
    return artist

#while per rendere il programma interattivo con la funzione input
while True:
    print("\nPlease tell me you favourite band and his album:")
    print("(enter 'Q' at any time to quit)")

    b_name = input("Name of band you like: ")
    if b_name == 'q':
        break
    a_name = input("Name of his album you like: ")
    if b_name == 'q':
        break

    call_var = make_album(b_name, a_name)
    print(f"\nYou favourite band and album are {call_var}")