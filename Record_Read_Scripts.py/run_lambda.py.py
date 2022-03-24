# PLEASE DO NOT EDIT
# run_lambda.py
# This executes a lambda function with a sample event.
from dcs.util.aws_lambda import * 
import json


# Clean up any old lambda functions
clean_lambdas()

# Create a new lambda 
create_lambda("recordReaderS3", "record_created_handler")

# Read the test event JSON file as dictionary
with open("./dcs/sample_events/s3_event_c2l1.json") as json_file:
    payload = json.load(json_file)

# Invoke lambda with test event, print result
result = invoke_function_and_get_message("recordReaderS3", payload)
print(json.dumps(json.loads(result), indent=4))