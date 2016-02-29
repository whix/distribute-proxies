import sqlite3
import requests
import re
from datetime import datetime
import httplib
import sys
import os

conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath('__path__')), 'db.sqlite3'))
cur = conn.cursor()
results = cur.execute('select * from proxies_proxies order by add_date')
# print results.fetchall()
# print results.fetchone()

print type(results)
for r in results:
    print r[0], r[1], r[2], r[3], r[4]
conn.close()