# NoSQL

## Description
This project covers NoSQL databases with a focus on MongoDB. It includes tasks that explore document storage, querying information, insertion, updating, and deletion of information in NoSQL databases.

## Resources
Read or watch:
- NoSQL Databases Explained
- What is NoSQL?
- MongoDB with Python Crash Course - Tutorial for Beginners
- MongoDB Tutorial 2: Insert, Update, Remove, Query
- Aggregation
- Introduction to MongoDB and Python
- mongo Shell Methods
- The mongo Shell

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4)
- All your files should end with a new line
- The first line of all your files should be a comment: // my comment
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9) and PyMongo (version 4.8.0)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- Your code should not be executed when imported (by using if __name__ == "__main__":)

## More Info
### Install MongoDB 4.4 in Ubuntu 20.04
- Follow the [official installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

## Tasks
0. List all databases - File: 0-list_databases
1. Create a database - File: 1-use_or_create_database
2. Insert document - File: 2-insert
3. All documents - File: 3-all
4. All matches - File: 4-match
5. Count - File: 5-count
6. Update - File: 6-update
7. Delete by match - File: 7-delete
8. List all documents in Python - File: 8-all.py
9. Insert a document in Python - File: 9-insert_school.py
10. Change school topics - File: 10-update_topics.py
11. Where can I learn Python? - File: 11-schools_by_topic.py
12. Log stats - File: 12-log_stats.py