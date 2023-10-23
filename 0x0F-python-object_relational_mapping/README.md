Project Title:  Python - Object-relational mapping. 

Overview 

In this project, you learned about object-relational mapping (ORM) and how to work with databases using MySQLdb and SQLAlchemy. Below, I'll provide a simplified summary of each task in a more comprehensible manner: 

Project Description by task 

Task 0: Get all states
- Python script `0-select_states.py` lists all states in the `hbtn_0e_0_usa` database using MySQLdb.
- Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.
- Results are ordered by state ID. 

Task 1: Filter states
- Python script `1-filter_states.py` lists states with names starting with 'N' in the `hbtn_0e_0_usa` database using MySQLdb.
- Usage: `./1-filter_states.py <mysql username> <mysql password> <database name>`.
- Results are ordered by state ID. 

Task 2: Filter states by user input
- Python script `2-my_filter_states.py` lists states with names matching user input in the `hbtn_0e_0_usa` database using MySQLdb.
- Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
- Results are ordered by state ID. 

Task 3: SQL Injection protection
- Python script `3-my_safe_filter_states.py` lists states with names matching user input, protecting against SQL injections in the `hbtn_0e_0_usa` database using MySQLdb.
- Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
- Results are ordered by state ID. 

Task 4: Cities by states
- Python script `4-cities_by_state.py` lists all cities in the `hbtn_0e_4_usa` database using MySQLdb.
- Usage: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`.
- Results are ordered by city ID. 

Task 5: All cities by state
- Python script `5-filter_cities.py` lists all cities in a specific state in the `hbtn_0e_4_usa` database using MySQLdb.
- Usage: `./5-filter_cities.py <mysql username> <mysql password> <database name>`.
- Results are sorted by city ID. 

Task 6: First state model
- The `model_state.py` module defines a Python class `State` that represents a state and links to the MySQL table `states` using SQLAlchemy. 

Task 7: All states via SQLAlchemy
- Python script `7-model_state_fetch_all.py` lists all `State` objects from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>`.
- Results are sorted by state ID. 

Task 8: First state
- Python script `8-model_state_fetch_first.py` prints the first `State` object from the `hbtn_0e_6_usa` database using SQLAlchemy, ordered by state ID.
- Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>`.
- If the `states` table is empty, it prints "Nothing." 

Task 9: Contains 'a'
- Python script `9-model_state_filter_a.py` lists all `State` objects containing the letter 'a' in the `hbtn_0e_6_usa` database using SQLAlchemy.
- Usage: `./9-model_state_filter_a.py <mysql username> <mysql password> <database name>`.
- Results are ordered by state ID. 

Task 10: Get a state
- Python script `10-model_state_my_get.py` prints the ID of the `State` object with a name that matches the provided argument in the `hbtn_0e_6_usa` database using SQLAlchemy.
- Usage: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`.
- Displays the ID of the matched `State`, or "Not found" if no match is found. 

Task 11: Add a new state
- Python script `11-model_state_insert.py` adds a new `State` object named "Louisiana" to the `hbtn_0e_6_usa` database using SQLAlchemy.
- Usage: `./11-model_state_insert.py <mysql username> <mysql password> <database name>`.
- Prints the ID of the new `State` after creation. 

Task 12: Update a state
- Python script `12-model_state_update_id_2.py` changes the name of the `State` object with ID = 2 to "New Mexico" in the `hbtn_0e_6_usa` database using SQLAlchemy.
- Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>`. 

Task 13: Delete states
- Python script `13-model_state_delete_a.py` deletes all `State` objects with names containing the letter 'a' from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Usage: `./13-model_state_delete_a.py <mysql username> <mysql password> <database name>`. 

Task 14: Cities in state
- The `model_city.py` module defines a Python class `City` that represents a city and links to the MySQL table `cities` using SQLAlchemy.
- Python script `14-model_city_fetch_by_state.py` lists all `City` objects in the `hbtn_0e_14_usa` database using SQLAlchemy.
- Usage: `./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>`.
- Results are sorted by city ID. 

Task 15: City relationship
- The `relationship_state.py` module defines a Python class `State` that inherits from SQLAlchemy and has a relationship with the `City` class.
- The `relationship_city.py` module defines a Python class `City` that inherits from SQLAlchemy and is related to the `State` class.
- Python script `100-relationship_states_cities.py` adds a `State` ("California") with a `City` ("San Francisco") to the `hbtn_0e_100_usa` database using SQLAlchemy.
- Usage: `./100-relationship_states_cities.py <mysql username> <mysql password> <database name>`.
- Uses the `cities` relationship for all `State` objects. 

Task 16: List relationship
- Python script `101-relationship_states_cities_list.py` lists all `State` and corresponding `City` objects in the `hbtn_0e_101_usa` database using SQLAlchemy.
- Usage: `./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>`.
- Uses the `cities` relationship for all `State` objects.
- Results are sorted by state and city IDs. 

Task 17: List city
- Python script `102-relationship_cities_states_list.py` lists all `City` objects from the `hbtn_0e_101_usa` database 

Acknowledgement 

Special thanks to ALX community for their invaluable education and strong community network. 

Author 

Name: Ginika Elizabeth Nna 

Email: elizabethginika9@gmail.com 
