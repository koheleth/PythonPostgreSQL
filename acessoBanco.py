import psycopg2

con = psycopg2.connect(host='localhost', user='postgres', dbname='mydatabase')
c = con.cursor()
