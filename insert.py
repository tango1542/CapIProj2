
def insert_database():
    import sqlite3

    sqlite_file = 'Project1DB'  # name of the sqlite database file
    table_name = 'Products'  # name of the table to be created
    col1 = 'ID' # name of the column
    col2 = 'Name'  # name of the column


    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()


    c.execute("INSERT INTO Products ({c2}, Color, PricePerLb, InventoryLbs, SpecialItem)\
              VALUES ('bananas','yellow',18,13,1)".format(c1=col1,c2=col2))
    c.execute("INSERT INTO Products (Name, Color, PricePerLb, InventoryLbs, SpecialItem)\
                 VALUES ('apples','red',28.6,16,1)")
    c.execute("INSERT INTO Products (Name, Color, PricePerLb, InventoryLbs, SpecialItem)\
                 VALUES ('blueberries','blue',26.1,111,0)")
    c.execute("INSERT INTO Products (Name, Color, PricePerLb, InventoryLbs, SpecialItem)\
                 VALUES ('raspberries','red',18.6,9,1)")
    c.execute("INSERT INTO Products (Name, Color, PricePerLb, InventoryLbs, SpecialItem)\
                 VALUES ('mango','green',51.2,12,1)")
    c.execute("INSERT INTO Products (Name, Color, PricePerLb, InventoryLbs, SpecialItem)\
                 VALUES ('kiwis','brown',25.6,11,0)")



    conn.commit()
    conn.close()