import sqlite3
import csv
import datetime

def get_records(query):
    output = []
    db_conn = sqlite3.connect(r'db\yangcodb')
    cursor = db_conn.cursor()
    result = cursor.execute(query)
    output = result.fetchall()
    db_conn.close()

    return output

def create_output(records):
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime('%Y%m%d%H%M%S')

    with open (f'python_only_output_{timestamp}.csv','w',newline='') as csvfile:
        fieldnames = ['Customer','Age','Item', 'Quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=';')

        writer.writeheader()

        for rows in records:
            writer.writerow({
                'Customer' : rows[0],
                'Age' : rows[1],
                'Item' : rows[2],
                'Quantity' : rows[3]
            })

def main():
    records = get_records('''
        select
            c.customer_id,
            c.age,
            i.item_name,
            sum(o.quantity)
        from items i
        left join orders o on i.item_id = o.item_id
        left join sales s on o.sales_id = s.sales_id
        left join customer c on s.customer_id = c.customer_id
        group by c.customer_id, c.age, i.item_name
        order by c.customer_id, o.quantity
    ''')

    create_output(records)
    
main()
    


