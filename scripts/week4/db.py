import datetime
import mysql.connector
import yaml

with open('config.yaml') as f:
    config = yaml.load(f)

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT username, email, is_superuser, date_joined FROM auth_user "
         "WHERE date_joined BETWEEN %s AND %s")

date_start = datetime.date(2017, 1, 1)
date_end = datetime.date(2017, 3, 10)

cursor.execute(query, (date_start, date_end))

for row in cursor:
    print row

cursor.close()
cnx.close()