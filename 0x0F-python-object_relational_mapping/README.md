# Python - Object-relational Mapping (ORM)

## Overview

This project focuses on learning Object-Relational Mapping (ORM) techniques, enabling you to interact with databases through Python code instead of SQL queries. Using tools like MySQLdb and SQLAlchemy, we worked with databases in an efficient, Pythonic way.

## Project Breakdown

### Task 0: Get All States
- **Script**: `0-select_states.py`
- **Objective**: Lists all states from the `hbtn_0e_0_usa` database using MySQLdb.
- **Usage**: `./0-select_states.py <mysql username> <mysql password> <database name>`
- **Output**: Results are sorted by state ID.

### Task 1: Filter States
- **Script**: `1-filter_states.py`
- **Objective**: Lists all states with names starting with 'N' from the `hbtn_0e_0_usa` database.
- **Usage**: `./1-filter_states.py <mysql username> <mysql password> <database name>`
- **Output**: Results are sorted by state ID.

### Task 2: Filter States by User Input
- **Script**: `2-my_filter_states.py`
- **Objective**: Lists states matching user input in the `hbtn_0e_0_usa` database.
- **Usage**: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`
- **Output**: Results are sorted by state ID.

### Task 3: SQL Injection Protection
- **Script**: `3-my_safe_filter_states.py`
- **Objective**: Protects against SQL injections while filtering states in the `hbtn_0e_0_usa` database based on user input.
- **Usage**: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`
- **Output**: Results are sorted by state ID.

### Task 4: Cities by State
- **Script**: `4-cities_by_state.py`
- **Objective**: Lists all cities from the `hbtn_0e_4_usa` database.
- **Usage**: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`
- **Output**: Results are sorted by city ID.

### Task 5: All Cities by State
- **Script**: `5-filter_cities.py`
- **Objective**: Lists all cities in a specific state from the `hbtn_0e_4_usa` database.
- **Usage**: `./5-filter_cities.py <mysql username> <mysql password> <database name>`
- **Output**: Results are sorted by city ID.

### Task 6: First State Model
- **Module**: `model_state.py`
- **Objective**: Defines a `State` class and links it to the MySQL table `states` using SQLAlchemy.

### Task 7: All States via SQLAlchemy
- **Script**: `7-model_state_fetch_all.py`
- **Objective**: Lists all `State` objects from the `hbtn_0e_6_usa` database using SQLAlchemy.
- **Usage**: `./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>`
- **Output**: Results are sorted by state ID.

### Task 8: First State
- **Script**: `8-model_state_fetch_first.py`
- **Objective**: Prints the first `State` object from the `hbtn_0e_6_usa` database.
- **Usage**: `./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>`
- **Output**: If no states are present, it prints "Nothing."

### Task 9: Contains 'a'
- **Script**: `9-model_state_filter_a.py`
- **Objective**: Lists all `State` objects containing the letter 'a' from the `hbtn_0e_6_usa` database using SQLAlchemy.
- **Usage**: `./9-model_state_filter_a.py <mysql username> <mysql password> <database name>`
- **Output**: Results are sorted by state ID.

### Task 10: Get a State
- **Script**: `10-model_state_my_get.py`
- **Objective**: Prints the ID of the `State` object whose name matches the input in the `hbtn_0e_6_usa` database.
- **Usage**: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`
- **Output**: Prints the ID of the matched `State`, or "Not found."

### Task 11: Add a New State
- **Script**: `11-model_state_insert.py`
- **Objective**: Adds a new `State` named "Louisiana" to the `hbtn_0e_6_usa` database.
- **Usage**: `./11-model_state_insert.py <mysql username> <mysql password> <database name>`
- **Output**: Prints the ID of the newly created `State`.

### Task 12: Update a State
- **Script**: `12-model_state_update_id_2.py`
- **Objective**: Updates the `State` object with ID = 2 to "New Mexico" in the `hbtn_0e_6_usa` database.
- **Usage**: `./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>`

### Task 13: Delete States
- **Script**: `13-model_state_delete_a.py`
- **Objective**: Deletes all `State` objects with names containing the letter 'a' from the `hbtn_0e_6_usa` database.
- **Usage**: `./13-model_state_delete_a.py <mysql username> <mysql password> <database name>`

### Task 14: Cities in State
- **Module**: `model_city.py`
- **Objective**: Defines a `City` class linked to the MySQL table `cities` using SQLAlchemy.
- **Script**: `14-model_city_fetch_by_state.py`
- **Usage**: Lists all `City` objects from the `hbtn_0e_14_usa` database.

### Task 15: City Relationship
- **Modules**: `relationship_state.py`, `relationship_city.py`
- **Objective**: Defines relationships between `State` and `City` classes.
- **Script**: `100-relationship_states_cities.py`
- **Output**: Adds a `State` ("California") and a `City` ("San Francisco").

### Task 16: List Relationship
- **Script**: `101-relationship_states_cities_list.py`
- **Objective**: Lists all `State` and corresponding `City` objects in the `hbtn_0e_101_usa` database using SQLAlchemy.

### Task 17: List City
- **Script**: `102-relationship_cities_states_list.py`
- **Objective**: Lists all `City` objects in the `hbtn_0e_101_usa` database using SQLAlchemy.

## Acknowledgement

Special thanks to the ALX community for their invaluable education and strong support network.

## Author

- **Name**: Ginika Elizabeth Nna
- **Email**: elizabethginika9@gmail.com
