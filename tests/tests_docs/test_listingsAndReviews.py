import os
import json
from bson import json
from dotenv import load_dotenv 
import pymongo
from monggregate import Pipeline, S
from pathlib import Path


expected_documents = Path(__file__).parent / "data" / "test_pipeline_reviews_results.json"

with open(expected_documents, encoding="utf-8") as f:
    expected_documents = json.loads(json_util.dumps(results))

# The reviewer_id whose reviews we want to retrieve
reviewer_id = "2961855"
load_dotenv(verbose=True)
MONGODB_URI = os.environ["MONGODB_URI"]
client = pymongo.MongoClient(MONGODB_URI)
db = client["sample_airbnb"]
# Building the pipeline
pipeline = Pipeline()
pipeline.unwind(
    "reviews"
    ).replace_root(
        "reviews"
    ).match(
        reviewer_id=reviewer_id
    )

# Executing the pipeline
cursor = db["listingsAndReviews"].aggregate(pipeline=pipeline.export())
documents = list(cursor)

assert documents == expected_documents