
def update_database():
    import sqlite3

    sqlite_file = 'Project1DB'  # name of the sqlite database file

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute("UPDATE Products SET Name ='peaches' WHERE ID=(3)")

    conn.commit()
    conn.close()