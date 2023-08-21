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
import sys

def list_states(username, password, database, num_rows):
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
    try:
        # Connect to the server using context manager
        connection = MySQLdb.connect(
            host='localhost', user=username, passwd=password, db=database, port=3306
        )
        
        # Create a cursor that aids interaction with the database
        cursor = connection.cursor()
        
        # Execute the query to retrieve states with specified number of rows
        query = f"SELECT * FROM states ORDER BY states.id ASC LIMIT {num_rows}"
        cursor.execute(query)
        
        # Fetch all rows from the result
        rows = cursor.fetchall()
        
        # Print results in the expected format (state id and name)
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor object
        cursor.close()
        
        # Close the connection to the database
        connection.close()