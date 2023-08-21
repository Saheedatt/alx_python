"""
Script to list all states from the hbtn_0e_0_usa database.

Usage:
    python script.py <username> <password> <database> <number_of_rows>

This script connects to a MySQL server running on localhost at port 3306.
It retrieves a specified number of rows of states from the specified database
and displays them.

Arguments:
    <username>: MySQL username.
    <password>: MySQL password.
    <database>: Database name.
    <number_of_rows>: Number of rows to retrieve.
"""


import MySQLdb


def main(username, password, database):
    """
    Fetches and lists specified number of rows from the hbtn_0e_0_usa database

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
        <num_rows>: Number of rows to retrieve.
    Returns:
        None
    """
    # Connect to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        password=password, db=database
        )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT name FROM states ORDER BY id ASC")

    # Fetch all rows
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row[0])

    # Close the cursor object
    cursor.close()

    # Close the connection to the database
    connection.close()

if __name__ == "__main__":
    # Get the arguments
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter MySQL database name: ")

    # Run the main function
    main(username, password, database)
