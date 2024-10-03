import mysql.connector
from mysql.connector import Error

# Function to create a connection to the database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host= 'localhost',
            user='root',
            passwd='12345',
            database='iimt'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to execute a single query (for INSERT, UPDATE, DELETE)
def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Function to fetch query results (for SELECT queries)
def fetch_query_results(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

# Add a new employee
def add_employee(connection):
    eid=int(input("Enter the employee id:"))
    ename=input("Enter the Employee name:")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    salary=input("Enter the salary:")
    department = (input("Enter department: "))
    post = (input("Enter position : "))

    query = """
    INSERT INTO employee (eid, ename, email, phone,salary, department, post)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (eid, ename, email, phone,salary, department, post)
    execute_query(connection, query, values)

# Remove an employee
def remove_employee(connection):
    employee_id = int(input("Enter the employee ID to remove: "))
    query = "DELETE FROM employee WHERE eid = %s"
    values = (employee_id,)
    execute_query(connection, query, values)

# View employee department
def view_employee_department(connection):
    employee_id = int(input("Enter the employee ID: "))
    query = """
    SELECT e.eid, e.ename, d.department
    FROM Employees e
    JOIN Departments d ON e.department_id = d.department_id
    WHERE e.eid = %s
    """
    values = (employee_id,)
    results = fetch_query_results(connection, query, values)
    if results:
        for row in results:
            print(f"Employee: {row[0]} {row[1]}, Department: {row[2]}")
    else:
        print("Employee not found.")

# Update employee salary
def update_employee_salary(connection):
    employee_id = int(input("Enter the employee ID: "))
    new_salary = float(input("Enter the new salary: "))
    query = """
    UPDATE Salaries
    SET salary = %s
    WHERE eid = %s
    """
    values = (new_salary, employee_id)
    execute_query(connection, query, values)

# Main menu
def main_menu(connection):
    while True:
        print("\n=== Employee Management Menu ===")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employee Department")
        print("4. Update Employee Salary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_employee(connection)
        elif choice == '2':
            remove_employee(connection)
        elif choice == '3':
            view_employee_department(connection)
        elif choice == '4':
            update_employee_salary(connection)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Establishing connection
connection = create_connection("localhost", "root", "password", "iimt")

# Run the main menu
if connection:
    main_menu(connection)

