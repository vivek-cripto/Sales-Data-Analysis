from database import DATABASE
import Analytics

def connect_db():
    while True:
        print("\n==== Connect to Retail Database ====")
        database = input("Enter database name: ")
        user = input("Enter user name: ")
        password = input("Enter password: ")
        try:
            db = DATABASE(database, user, password)
            print("Connected to database successfully!")
            return db
        except Exception as e:
            print(f"Error connecting to database: {e}")
            print("Please try again.")
            
def main_menu(db):
    while True:
        print("\n==== Retail Database Analytics ====")
        print("\n=====MAIN MENU =====")
        print("1. Data Overview")
        print("2. Sales Analytics")
        print("3. Customer Analytics")
        print("4. Product Analytics")
        print("5. Export Reports")
        print("6. Exit")
        
        ch = input("Select a Option:")
        
        if ch == '1':
            Analytics.data_overview(db)
        elif ch == '2':
            Analytics.sales_analytics(db)
        elif ch == '3':
            Analytics.customer_analytics(db)
        elif ch == '4':
            Analytics.product_analytics(db)
        elif ch == '5':
            Analytics.export(db)
        elif ch == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
db = connect_db()
main_menu(db)

    

            
        


    