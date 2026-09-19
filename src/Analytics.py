from tkinter import Tk
from tkinter import filedialog
import pandas as pd

def data_overview(db):
    while True:
        print("\n==== Data Overview ====")
        print("1. Total Sales Records")
        print("2. Total Customers")
        print("3. Total Products")
        print("4. Dataset Date Range")
        print("5.Close Database Connection")
        print("6. Back to Main Menu")
        
        ch = input("Select an option: ")
        
        if ch == '1':
            rows = db.fetch("SELECT COUNT(*) FROM sales;")
            print(f"\nTotal Sales Records: {rows[0][0]}")
        elif ch == '2':
            rows = db.fetch("SELECT COUNT(*) FROM customer;")
            print(f"\nTotal Customers: {rows[0][0]}")
        elif ch == '3':
            rows = db.fetch("SELECT COUNT(*) FROM product;")
            print(f"\nTotal Products: {rows[0][0]}")
        elif ch == '4':
            rows =db.fetch("SELECT MIN(invoicedate), MAX(invoicedate) FROM sales;")
            print(f"Dataset Date Range: {rows[0][0]} to {rows[0][1]}")
        elif ch == '5':
            db.close()
            print("Database connection closed.")
        elif ch == '6':
            break
        else:
            print("Invalid option. Please try again.")
            
def sales_analytics(db):
    while True:
        print("\n==== Sales Analytics ====")
        print("1. Monthly Revenue Trends")
        print("2. Top 10 Selling Product")
        print("3. Country Wise Revenue")
        print("4. Daily Running Revenue")
        print("5. Average Order Value")
        print("6. Back to Main Menu")
        
        ch = input("Select an option: ")
        
        if ch == '1':
            rows =db.fetch("SELECT TO_CHAR(DATE_TRUNC('month',invoicedate), 'Mon YYYY') AS month, SUM(unitprice * quantity) from sales GROUP BY month ORDER BY month;")
            print("\nMonthly Revenue Trends: ")
            for row in rows:
                print(f"{row[0]}: {row[1]}")
        elif ch == '2':
            rows =db.fetch("SELECT description,SUM(quantity) AS quantitys from sales GROUP BY description ORDER BY quantitys DESC LIMIT 10;")
            print("\nTop 10 Selling Product: ")
            for row in rows:
                print(f"{row[0]} : {row[1]}")
        elif ch == '3':
            rows =db.fetch("SELECT country,SUM(unitprice * quantity) from sales GROUP BY country;")
            print("\nCountry Wise Revenue")
            for row in rows:
                print(f"{row[0]}:{row[1]}")
        elif ch == '4':  
            sm = input("\n Enter Start Date (YYYY-MM-DD):")
            em = input("\n Enter End Date (YYYY-MM-DD):")
            rows =db.fetch("SELECT TO_CHAR(DATE_TRUNC('day', invoicedate), 'DD Mon') AS day, SUM(quantity * unitprice) FROM sales WHERE invoicedate BETWEEN {sm} AND {em} GROUP BY DATE_TRUNC('day', invoicedate) ORDER BY DATE_TRUNC('day', invoicedate);")
            for row in rows:
                print(f"{row[0]}: {row[1]}")
        elif ch == '5':
            rows =db.fetch("SELECT AVG(order_total) AS avg_order_total FROM ( SELECT invoiceno,AVG(unitprice*quantity) AS order_total FROM sales GROUP BY invoiceno);")
            print(f"\nAverage Order Value: {rows[0][0]}")
        elif ch == '6':
            break
        else:
            print("Invalid option. Please try again.")

def customer_analytics(db):
    while True:
        print("\n==== Customer Analytics ====")
        print("1. Top Customer by Revenue")
        print("2. Repeat vs New Customers")
        print("3. Customer Lifetime Value")
        print("4. Country Wise Customer Distribution")
        print("5. Back to Main Menu")
        
        ch = input("Select an option: ")
        
        if ch == '1':
            dt = int(input("\n Enter the number of top customers to display: "))
            rows =db.fetch("SELECT customer.customer_id, customer.country,SUM(quantity) AS total FROM sales JOIN customer ON sales.customerid = customer.customer_id GROUP BY customer.customer_id, customer.country ORDER BY total DESC LIMIT {dt};")
            for row in rows:
                print(f"Customer ID: {row[0]}, Country: {row[1]}, Total Revenue: {row[2]}")
        elif ch == '2':
            rows =db.fetch("SELECT customerid, COUNT(invoiceno) AS ORDERS FROM sales GROUP BY customerid ORDER BY ORDERS;") 
            for row in rows:
                print(f"Customer ID: {row[0]}, Orders: {row[1]}") 
        elif ch == '3':
            rows =db.fetch("SELECT customerid,SUM(quantity * unitprice) AS customer_lifetime_value FROM sales GROUP BY customerid ORDER BY customer_lifetime_value DESC;")
            for row in rows:
                print(f"Customer ID: {row[0]}, Customer Lifetime Value: {row[1]}")
        elif ch == '4':  
            rows =db.fetch("SELECT country,COUNT(DISTINCT(customerid)) AS customers FROM sales GROUP BY country ORDER BY customers;")
            for row in rows:
                print(f"country: {row[0]} , Customers: {row[1]}")
        elif ch == '5':
            break
        else:
            print("Invalid option. Please try again.")

def product_analytics(db):
    while True:
        print("\n==== Product Analytics ====")
        print("1. Best Performing Products")
        print("2. Low Demanding Products")
        print("3. Product Sales Trends")
        print("4. Product Revenue Trend")
        print("5. Back to Main Menu")
        
        ch = input("Select an option: ")
        
        if ch == '1':
            dt = int(input("\n Enter the number of top products to display: "))
            rows =db.fetch("SELECT product_id, description,SUM(quantity) AS total FROM sales GROUP BY product_id,description ORDER BY total DESC LIMIT {dt};")
            for row in rows:
                print(f"Product ID: {row[0]}, Description: {row[1]}, Total Sales: {row[2]}")
        elif ch == '2':
            dt = int(input("\n Enter the number of low demanding products to display: "))
            rows =db.fetch("SELECT product_id, description FROM sales GROUP BY product_id,description ORDER BY SUM(quantity) ASC LIMIT {dt};")  
            for row in rows:
                print(f"Product ID: {row[0]}, Description: {row[1]}")
        elif ch == '3':
            dt = int(input("\n Enter the product ID to analyze sales trends: "))
            rows =db.fetch("SELECT TO_CHAR(DATE_TRUNC('month',invoicedate), 'Mon YYYY'),SUM(quantity) AS S FROM sales WHERE product_id = '{dt}' GROUP BY DATE_TRUNC('month',invoicedate);")
            for row in rows:
                print(f"Month: {row[0]}, Total Sales: {row[1]}")
        elif ch == '4':
            dt = int(input("\n Enter the product ID to analyze sales trends: "))
            rows =db.fetch("SELECT TO_CHAR(DATE_TRUNC('month',invoicedate), 'Mon YYYY'),SUM(quantity * unitprice) AS S FROM sales WHERE product_id = '{dt}' GROUP BY DATE_TRUNC('month',invoicedate);")
            for row in rows:
                print(f"Month: {row[0]}, Total Revenue: {row[1]}")
        elif ch == '5':
            break
        else:
            print("Invalid option. Please try again.")

def export(db):
    while True:
        print("\n==== Export Data ====")
        print("1. Export Monthly Revenue CSV")
        print("2. Export Top Product CSV")
        print("3. Export Sales Report CSV")
        print("4. Back to Main Menu")
        
        ch = input("Select an option: ")
        
        if ch == '1':
            export_monthly_revenue(db)
        elif ch == '2':
            export_top_product(db)  
        elif ch == '3':
            export_sales_report(db) 
        elif ch == '4':
            break
        else:
            print("Invalid option. Please try again.")
            
def export_monthly_revenue(db):
    query = """
        SELECT 
            DATE_TRUNC('month', invoicedate) AS month,
            SUM(quantity * unitprice) AS revenue
        FROM sales
        GROUP BY month
        ORDER BY month;
    """
    rows = db.fetch(query)
    df = pd.DataFrame(rows, columns=["month", "revenue"])
    df["month"] = df["month"].dt.strftime("%b %Y")
    
    path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV file", "*.csv")],
        title="Save Report"
    )

    if path:
        df.to_csv(path, index=False)
        print("Exported successfully")
    else:
        print("Export cancelled")
    
def export_top_product(db):
    query = """
        SELECT description,SUM(quantity) AS quantities from sales
        GROUP BY description 
        ORDER BY quantities DESC;
    """
    rows = db.fetch(query)
    df = pd.DataFrame(rows, columns=["description", "quantities"])
    
    path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV file", "*.csv")],
        title="Save Report"
    )

    if path:
        df.to_csv(path, index=False)
        print("Exported successfully")
    else:
        print("Export cancelled")


def export_sales_report(db):

    query = """
        SELECT 
            invoiceno,
            invoicedate,
            product_id,
            customerid,
            quantity,
            unitprice,
            quantity * unitprice AS revenue
        FROM sales
        ORDER BY invoicedate;
    """

    rows = db.fetch(query)

    df = pd.DataFrame(
        rows,
        columns=[
            "invoice_no",
            "invoice_date",
            "product_id",
            "customer_id",
            "quantity",
            "unit_price",
            "revenue"
        ]
    )
    
    path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV file", "*.csv")],
        title="Save Sales Report"
    )

    if path:
        df.to_csv(path, index=False)
        print("Sales report exported successfully")
    else:
        print("Export cancelled")
