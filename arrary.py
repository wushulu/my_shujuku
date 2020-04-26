import sqlite3
import numpy as np
import io

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


# Converts np.array to TEXT when inserting
sqlite3.register_adapter(np.ndarray, adapt_array)

# Converts TEXT to np.array when selecting
sqlite3.register_converter("array", convert_array)

#x = np.arange(10)#.reshape(2,5)
a = [0.1,10.0,20.0,99.5]
#print(type(x[0]))

x = np.asarray(a)
y = np.arange(10)
#x = [1 2 3 4]
#x = [0, 1,2,3]

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test (arr array)")
cur.execute("insert into test (arr) values (?)", (x, ))
cur.execute("insert into test (arr) values (?)", (y, ))

cur.execute("select arr from test")
for  row in cur:
    print(row[0])
#print(cur)
#data = cur.fetchone()[0]

#print(type(data[1]))