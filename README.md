# SQLAlchemy-CRUD
Utilising Python with SQL Alchemy &amp; Vagrant to run CRUD functions on SQLite using python classes mapped by the ORM.

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

## FILES

database_setup.py - This file is used to setup our database on sql lite using Python classes (ORM).

## INSTALLATION

Download Vagrant and Virtual Box
Recommend download GIT Gui
Download or clone Github Repo
Make sure your command line has python, if not download python to your terminal

## CONFIGURATION

All tournament pairing scripts within a file housing Vagrant in the following structure:

/vagrant/crud

## RUNNING

The scripts have been previously executed with GIT command line.

Using GIT Gui, CD into root directory of vagrant file:
cd /vagrant

Within the vagrant folder type:

vagrant up
vagrant ssh

CD to /vagrant/crud folder:

cd /vagrant/crud

Start the web server:

python webserver.py

Go to your localhost and expirement

localhost 8080
