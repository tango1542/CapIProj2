def inputDisplay_database():
    import sqlite3

    sqlite_file = 'Project1DB'  # name of the sqlite database file

    col_value = input("Select the record number you wish to display")
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM Products WHERE ID =?',(col_value))
    for row in c:
        print ("ID=", row[0])
        print("Name=", row[1])
        print("Color=", row[2])
        print("PricePerLb=", row[3])
        print("InventoryLbs=", row[4])
        print("SpecialItem=", row[5], "\n")



    conn.commit()
    conn.close()