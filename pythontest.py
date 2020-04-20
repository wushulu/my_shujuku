import sqlite3
if __name__ == "__main__":
    conn = sqlite3.connect('shujuku.db')
    c = conn.cursor()
    data = (5,18)
    sql = "INSERT INTO mytesttable (ID,AGE) \
    VALUES (?, ? )"
    c.execute(sql,data)
    #cursor = conn.execute("SELECT ID,AGE mytesttable")
    cursor = conn.execute("SELECT *from mytesttable")
    conn.commit()



    for row in cursor:
        print(row[0])
        print(row[1])

        #print(row[4])

    conn.close()