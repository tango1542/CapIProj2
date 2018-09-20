def create_database():
    import sqlite3

    sqlite_file = 'Project1DB'    # name of the sqlite database file
    table_name1 = 'Products'  # name of the table to be created
    new_field = 'ID' # name of the column
    new_field2 = 'Name'  # name of the column
    new_field3 = 'Color'  # name of the column
    new_field4 = 'PricePerLb'  # name of the column
    new_field5 = 'InventoryLbs'  # name of the column
    new_field6 = 'SpecialItem'  # name of the column
    field_type = 'INTEGER PRIMARY KEY'  # column data type
    field_type2 = 'TEXT NOT NULL'  # column data type
    field_type3 = 'TEXT NOT NULL'  # column data type
    field_type4 = 'REAL NOT NULL'  # column data type
    field_type5 = 'INTEGER NOT NULL'  # column data type
    field_type6 = 'INTEGER DEFAULT 0'  # column data type

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()


    c.execute('CREATE TABLE {tn} ({nf} {ft} ,{nf2} {ft2} ,{nf3} {ft3},{nf4} {ft4},{nf5} {ft5},{nf6} {ft6})'\
            .format(tn=table_name1, nf=new_field, ft=field_type, nf2=new_field2, ft2=field_type2, nf3=new_field3, ft3=field_type3, nf4=new_field4, ft4=field_type4, nf5=new_field5, ft5=field_type5, nf6=new_field6, ft6=field_type6))

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()