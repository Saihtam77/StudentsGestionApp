from datetime import date
from Fonctions.StudentsFunction import *
from Database.connection import connection
import random

from faker import Faker

# Connect to the database
db = connection()

add_student(db)


    