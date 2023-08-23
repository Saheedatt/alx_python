## wEEK FOR SQL ALCHEMY AND OBJECT-RELATIONAL MAPPERS

This repository contains a collection of Python scripts that utilize SQLAlchemy to interact with a MySQL database. These scripts were developed as part of my learning journey and practical experience in database management using SQLAlchemy. I solved ten questions that were provided by ALX in an attempt to try to put what I had learnt to use.

### Contents

1. [Description](#description)
2. [Scripts](#scripts)
3. [Dependencies](#dependencies)
4. [Acknowledgements](#acknowledgements)

## Description

The scripts in this repository serve various purposes related to querying and managing data in a MySQL database. They are designed to be modular and reusable, utilizing SQLAlchemy's ORM capabilities. We were provided with databases and we had to write codes to query each database. I had difficulty in solving the "filter states" question until I came across the use of query_template and BINARY.

## Scripts
1. **0-select_states.py**: This script lists all states from the hbtn_0e_0_usa database.

2. **1-filter_states.py**: This script lists all states with a name starting with N (upper N) from the hbtn_0e_0_usa database.

3. **2-my_filter_states.py**: This script takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

4. **3-my_safe_filter_states**: This script lists states from the hbtn_0e_0_usa database based on search criteria.Here , we learn about sql injection and how to write our script in a way that is safe from injection.

5. **4-cities_by_state.py**: This script lists all cities from the hbtn_0e_4_usa database by their states.

6. **5-filter_cities.py**: This script lists all cities of a given state from the hbtn_0e_4_usa database.

7. **model_state.py**: Here, we beign to make use of SQLAlchemy.; learning to trust the ORM magic. We make use of python classes too. This script is a module for defining a State class using SQLAlchemy.

8. **7-model_state_fetch_all.py**: This script lists all State objects from the hbtn_0e_6_usa database but unlike we did earlier, we start to make use of python classes inheritance from the model_state.py.

9. **8-model_state_fetch_first.py**: This script prints the first State object from the database `hbtn_0e_6_usa`. 

10. **9-model_state_filter_a.py**: This script lists all State objects that contain the letter 'a' in their name from the database `hbtn_0e_6_usa`. Like the 8 & 9, it also inherits from the model_states.py.

### Dependencies
- Python 3.x
- SQLAlchemy
- mysqlclient


### Acknowledgements
These scripts were created for educational purposes and practical learning. They were developed based on my understanding of SQL, databases, and SQLAlchemy. I would like to acknowledge the resources and tutorials provided by ALX and Holberton school that helped me gain the knowledge required to create these scripts.