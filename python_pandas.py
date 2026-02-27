import shared_functions as sf #get_records()
import datetime
import pandas

def main():
    records = sf.get_records('''
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
    output = pandas.DataFrame(records)
    output.columns = ['Customer','Age','Item','Quantity']

    #get current date and time
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime('%Y%m%d%H%M%S')

    #generate csv file
    output.to_csv(f'python_pandas_output_{timestamp}.csv', sep=';',index=False)

#execution
main()