import os

from dotenv import load_dotenv
import pymongo
from monggregate import Pipeline, S

# Creating connexion string securely
# You need to create a .env file with your password
load_dotenv(verbose=True)
MONGODB_URI = os.environ["MONGODB_URI"] 


# Connect to your MongoDB cluster:
client = pymongo.MongoClient(MONGODB_URI)

# Get a reference to the "sample_mflix" database:
db = client["sample_mflix"]

# Creating the pipeline
pipeline = Pipeline()

# The below pipeline will return the most recent movie with the title "A Star is Born"
pipeline.match(
    title="A Star Is Born"
).sort(
    by="year"
).limit(
    value=1
)

# Executing the pipeline
cursor = db["movies"].aggregate(pipeline.export())

# Printing the results
results = list(cursor)
expeted_results = results

# Assert

assert expeted_results == results