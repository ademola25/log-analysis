# Log Analysis Project
## Project Description:
Building an informative summary from logs is a real task that comes up very often in software engineering. This program  will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.(Project from [Full Stack Web Development Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/))
#### The project drives following conclusions:
* The Most popular three articles of all time.
* The Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

## Technologies used
1. PostgreSQL
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

## Project Setup:
This project is run on a virutal machine created using Vagrant:
#### Installing the dependencies and setting up the files:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data to get the newsdata.sql file.
1. Put the newsdata.sql file into the vagrant directory

#### Run these commands from the terminal to start the virtual machine: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python3 newsdata.py``` to run the reporting tool.
## Output: 
    Top Three Articles viewed:
        (1) "Candidate is jerk, alleges rival" ---> 338647 views
        (2) "Bears love berries, alleges bear" ---> 253801 views
        (3) "Bad things gone, say good people" ---> 170098 views
    Top popular Author By Views:
        (1) Ursula La Multa ---> 507594 views
        (2) Rudolf von Treppenwitz ---> 423457 views
        (3) Anonymous Contributor ---> 170098 views
        (4) Markoff Chaney ---> 84557 view
    Error of days with more than 1% Requests:
        July 17, 2016 ---> 2.3% errors
## no view is used
Since it is optional

