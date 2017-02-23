#########Config code ####################################

#provides number of functions to manipulate run time environment
import sys

#Used when writing the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

#We will use in the configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#We use to create our foreign key relationships, used for mapper too
from sqlalchemy.orm import relationship

#We use in our configuration file end of code
from sqlalchemy import create_engine

#Let sqlalchemy know that our classes are special sqlalchemy classes
#That correspond to tables in our database
#Our class code will inherit this base class
Base = declarative_base()

#########Tables #########################################

class Restaurant(Base):
    #Create table representation
    __tablename__ = 'restaurant'
    #Use mapper code to create columns with variables representing col attributes
    name = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)

class MenuItem(Base):
    #Create table representation
    __tablename__ = 'menu_item'
    #Use mapper code to create variables representing columns
    name = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)

    course = Column(
        String(250))

    description = Column(
        String(250))

    price = Column(
        String(8))

    #Go into restaurant and retrieve the ID column as foreign key
    restaurant_id = Column(
        Integer, ForeignKey('restaurant.id'))

    #The relationship between my class Restaurant
    restaurant = relationship(Restaurant)

#########Insert at the end of file ######################

#Instance of create engine and point to our database
engine = create_engine(
    'sqlite:///restaurantmenu.db')

#Goes into the database and adds classes as new tables
Base.metadata.create_all(engine)