import psycopg2
import tkinter as tk





# Database connection
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="localhost"
)
cursor = conn.cursor()

# Creating the Soles table with sizes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Soles (
        id SERIAL PRIMARY KEY,
        article VARCHAR(100) NOT NULL,
        color VARCHAR(50),
        ddt VARCHAR(50),
        delivery_date DATE,
        size_38 INTEGER DEFAULT 0,
        size_39 INTEGER DEFAULT 0,
        size_40 INTEGER DEFAULT 0,
        size_41 INTEGER DEFAULT 0,
        size_42 INTEGER DEFAULT 0,
        size_43 INTEGER DEFAULT 0,
        size_44 INTEGER DEFAULT 0,
        size_45 INTEGER DEFAULT 0,
        size_46 INTEGER DEFAULT 0,
        quantity INTEGER
    )
''')

# Inserting sample data
cursor.execute('''
    INSERT INTO Soles (article, color, ddt, delivery_date, size_38, size_39, size_40, size_41, size_42, size_43, size_44, size_45, size_46, quantity)
    VALUES 
    ('Sport Sole', 'Black', 'DDT123', '2023-01-15', 10, 15, 5, 0, 0, 0, 0, 0, 0, 25),
    ('Elegant Sole', 'Brown', 'DDT124', '2023-02-20', 5, 8, 3, 2, 0, 0, 0, 0, 0, 13),
    ('Casual Sole', 'Blue', 'DDT125', '2023-03-10', 8, 12, 0, 0, 0, 0, 0, 0, 0, 20);
''')

# Executing a query to retrieve data from the Soles table
cursor.execute('SELECT * FROM Soles')

# Retrieving query results
rows = cursor.fetchall()

# Displaying results
for row in rows:
    print(row)

# Closing the connection
conn.commit()
conn.close()



## Manual data entry using keyword input and tkinker

def insert_data():
    article_val = article_entry.get()
    color_val = color_entry.get()
    ddt_val = ddt_entry.get()
    size_38_val = size_38_entry.get()
    size_39_val = size_39_entry.get()
    size_40_val = size_40_entry.get()
    size_41_val = size_41_entry.get()
    size_42_val = size_42_entry.get()
    size_43_val = size_43_entry.get()
    size_44_val = size_44_entry.get()
    size_45_val = size_45_entry.get()
    size_46_val = size_46_entry.get()
    date_val = date_entry.get()
    quantity_val = quantity_entry.get()

    conn = psycopg2.connect(
        dbname="your_database",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    query = '''
        INSERT INTO Soles (article, color, ddt, size_38, size_39, size_40, size_41, size_42, size_43, size_44, size_45, size_46, date, quantity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''

    cursor.execute(query, (article_val, color_val, ddt_val, size_38_val, size_39_val, size_40_val, size_41_val, size_42_val, size_43_val, size_44_val, size_45_val, size_46_val, date_val, quantity_val))
    conn.commit()
    conn.close()

# Creating the Tkinter window
root = tk.Tk()
root.title("Insert Data into SQL")

# Input fields
article_label = tk.Label(root, text="Article:")
article_label.pack()
article_entry = tk.Entry(root)
article_entry.pack()

color_label = tk.Label(root, text="Color:")
color_label.pack()
color_entry = tk.Entry(root)
color_entry.pack()

ddt_label = tk.Label(root, text="DDT:")
ddt_label.pack()
ddt_entry = tk.Entry(root)
ddt_entry.pack()

size_38_label = tk.Label(root, text="Size 38:")
size_38_label.pack()
size_38_entry = tk.Entry(root)
size_38_entry.pack()

size_39_label = tk.Label(root, text="Size 39:")
size_39_label.pack()
size_39_entry = tk.Entry(root)
size_39_entry.pack()

size_40_label = tk.Label(root, text="Size 40:")
size_40_label.pack()
size_40_entry = tk.Entry(root)
size_40_entry.pack()

size_41_label = tk.Label(root, text="Size 41:")
size_41_label.pack()
size_41_entry = tk.Entry(root)
size_41_entry.pack()

size_42_label = tk.Label(root, text="Size 42:")
size_42_label.pack()
size_42_entry = tk.Entry(root)
size_42_entry.pack()

size_43_label = tk.Label(root, text="Size 43:")
size_43_label.pack()
size_43_entry = tk.Entry(root)
size_43_entry.pack()

size_44_label = tk.Label(root, text="Size 44:")
size_44_label.pack()
size_44_entry = tk.Entry(root)
size_44_entry.pack()

size_45_label = tk.Label(root, text="Size 45:")
size_45_label.pack()
size_45_entry = tk.Entry(root)
size_45_entry.pack()

size_46_label = tk.Label(root, text="Size 46:")
size_46_label.pack()
size_46_entry = tk.Entry(root)
size_46_entry.pack()

date_label = tk.Label(root, text="Date:")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Button to insert data
insert_button = tk.Button(root, text="Confirm", command=insert_data)
insert_button.pack()

# Run the window
root.mainloop()


# SQL query for summing sizes for each article and color
query = '''
    SELECT article, color,
           SUM(size_38) AS total_size_38,
           SUM(size_39) AS total_size_39,
           SUM(size_40) AS total_size_40,
           SUM(size_41) AS total_size_41,
           SUM(size_42) AS total_size_42,
           SUM(size_43) AS total_size_43,
           SUM(size_44) AS total_size_44,
           SUM(size_45) AS total_size_45,
           SUM(size_46) AS total_size_46,
           SUM(quantity) AS total_quantity
    FROM Soles
    GROUP BY article, color
    ORDER BY article;
'''

# Execution of the query
cursor.execute(query)

# Retrieving the results of the query
rows = cursor.fetchall()

# Displaying the results
for row in rows:
    print(row)

# Closing the connection
conn.commit()
conn.close()


