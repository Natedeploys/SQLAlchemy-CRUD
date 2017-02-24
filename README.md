# SQLAlchemy-CRUD
Utilising Python with SQL Alchemy, SQLite &amp; Vagrant to run CRUD functions.

With SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

## FILES

database_setup.py - This file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program).

## INSTALLATION

Download Vagrant and Virtual Box
Recommend download GIT Gui
Download or clone Github Repo
Make sure your command line has python, if not download python to your terminal

## CONFIGURATION

All tournament pairing scripts within a file housing Vagrant in the following structure:

/vagrant/tournament/tournament.py, tournament_test.py, tournament.sql.

## RUNNING

The scripts have been previously executed with GIT command line.

Using GIT Gui, CD into root directory of vagrant file:
cd /vagrant

Within the vagrant folder type:

vagrant up
vagrant ssh


CD to /vagrant/tournament folder:

cd /vagrant/tournament


Connect to postgresql:

psql


Execute the tournament database schema setup:

\i tournament.sql;

\q


Back on /vagrant/tournament, execute the tests:

python tournament_test.py


You will see a list of test results.
