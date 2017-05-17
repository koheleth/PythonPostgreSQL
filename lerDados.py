import psycopg2

con = psycopg2.connect(host='localhost', user='postgres', dbname='mydatabase')
c = con.cursor()

c.execute('SELECT * FROM albuns')
registros = c.fetchall()

print('────────────────────────────────────')
print('\tid\t\t\t| Nome')
print('────────────────────────────────────')

for i in registros:
    print('\t', i[0], '\t\t\t|',i[1])
    print('────────────────────────────────────')
