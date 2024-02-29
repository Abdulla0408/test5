


import psycopg2 as sql

db = sql.connect(
    database='lesson10',
    host='localhost',
    user='postgres',
    password='1',
    port='5432'
)

cursor = db.cursor()

cursor.execute('''select model_id,model_name,brand_name from models join brands on models.brand_id = brands.brand_id  ''')

brands = cursor.fetchall()



cursor.execute('''
    select * from employees
    union
    select * from customers;
''')
email =cursor.fetchall()

cursor.execute('''
    select country, count(customer_id) from customers group by country order by count(customer_id)
''')

delievery_num = cursor.fetchall()
for son in delievery_num == cursor.fetchall():
    print(son)


cursor.execute('''
select brands, count(model_id) from models group by brands order by count(model_id)
''')

model_soni = cursor.fetchall()
for soni in model_soni:
    print(soni)





db.commit()
db.close()
