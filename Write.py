import csv
import random
from time import time
from time import sleep as wait



try:
    conn = #connect to database
    cur = conn.cursor()
    with open('csv_name', 'w', newline='') as f1:
        writer = csv.writer(f1)
        writer.writerow(["x", "exec_time"])
        for x in range(0, 10000):
            query1 = f"insert into dataset (pattern,print,fabric,native_product_id,primary_colour) values ('a','b','b',{x},'b')"
            query2 = "DELETE FROM dataset  WHERE ID=(SELECT MAX(id) FROM dataset)"
            tic = time()
            cur.execute(query1)
            toc = time()
            cur.execute(query2)
            execTime = toc - tic
            data = [x, execTime * 1000]
            writer.writerow(data)
        print("Done!")
    cur.close()
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
