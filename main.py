from Seeders.StudentsFactory import *
from datetime import date
from Fonctions.StudentsFunction import *
from Fonctions.SubjectFunction import *
from Database.connection import connection
from faker import Faker

fake = Faker()

# Connect to the database
db = connection()

# add_studentFactory(db)
# add_NoteFactory(db, "Jonathan", "Thompson")
# calculate_avarageRatings(db,"Jonathan", "Thompson","pe")
# calculate_OverallRating(db, "Jonathan", "Thompson")
addSubject(db, "_S", 3)







    