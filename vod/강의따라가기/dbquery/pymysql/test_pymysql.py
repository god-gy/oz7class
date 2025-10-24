import pymysql

# (1) db connection
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='20241013',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# (2) CRUD

## 1. sekect * from

def get_customers():
    cursor = connection.cursor()

    sql = "select * from customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers: ", customers)
    print("customers: ", customers['customerNumber'])
    print("customers: ", customers['country'])
    print("customers: ", customers['customerName'])

    cursor.close()

## 2. insert into

def add_customers():
    cursor = connection.cursor()

    name = 'inseop'
    family_name = 'kim'
    sql = f"insert into customers(customerNumber, customerName, contactLastName) values(1006, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()

    cursor.close()

# add_customers()

## 3. update into

def update_customers():
    cursor = connection.cursor()
    update_name = 'update_inseop'
    contactLastName = 'update_kim'
    sql = f"update customers set customerName='{update_name}',contactLastName='{contactLastName}' where customerNumber=1005"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

# update_customers()

## 4. delete from

def delete_customers():
    cursor = connection.cursor()
    sql = "delete from customers where customerNumber=1006"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customers()
