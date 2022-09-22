import csv
import random
from time import time
from time import sleep as wait

conn = None
try:
    conn = #connect to database
    cur = conn.cursor()
    with open('csv_name', 'w', newline='') as f1:
        writer = csv.writer(f1)
        writer.writerow(["x", "exec_time"])
        for x in range(0, 10000):
            n = random.randint(1, 100000)
            query = f"SELECT textielSet.id, textielSet.pattern, persoonSet.achternaam FROM textielSet INNER JOIN persoonSet ON textielSet.id = persoonSet.id WHERE textielSet.id = {n}"
            tic = time()
            cur.execute(query)
            toc = time()
            execTime = toc - tic
            result = cur.fetchone()
            data = [x, execTime * 1000]
            writer.writerow(data)
        print("Done!")
    cur.close()
except (Exception) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
