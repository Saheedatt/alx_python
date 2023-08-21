"""
Script to list all states from the hbtn_0e_0_usa database.

Usage:
    python script.py <username> <password> <database>

This script connects to a MySQL server running on localhost at port 3306.
It retrieves a sorted list of states from the specified database
and displays them.

Arguments:
    <username>: MySQL username.
    <password>: MySQL password.
    <database>: Database name.
"""

import MySQLdb


def list_states(username, password, database):
    """
    Fetches and lists all states from the hbtn_0e_0_usa database

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
    Returns:
        None
    """
    # connect to the server using context manager
    connection = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=username,
                                password=password,
                                db=database
                                )
    # create a cursor that aids interaction with database
    cursor = connection.cursor()

    # Gets the number of records in the states table
    cursor.execute("SELECT COUNT(*) FROM states")
    row = cursor.fetchone()
    num_records = row[0]

    
    # If there are no records, print an empty list
    if num_records == 0:
        print([])    
    
     # Otherwise, execute the query and print the results
    else:
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        results = cursor.fetchall()

        for row in results:
            print(row[1])

        # Close the cursor object
        cursor.close()
    # Close the connection to the database
        connection.close()
