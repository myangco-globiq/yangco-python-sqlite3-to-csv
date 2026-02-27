create table if not exists customer(
    customer_id integer primary key autoincrement,
    age numeric not null
);

create table if not exists items(
    item_id integer primary key autoincrement,
    item_name text unique not null
);

create table if not exists sales(
    sales_id integer primary key autoincrement,
    customer_id integer references customer(customer_id) not null,
    unique(sales_id, customer_id)
);

create table if not exists orders(
    order_id integer primary key autoincrement,
    sales_id integer unique references sales(sales_id),
    item_id integer references items(item_id),
    quantity integer not null
);