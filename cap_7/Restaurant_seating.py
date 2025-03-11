reservation = input("How may people are in you in your dinner group: ")
reservation = int(reservation)

if reservation > 8:
    print("\nI'm sorry, you have to wait for a table")
else:
    print("\nOk, the table is ready!")