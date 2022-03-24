import os
# Get Enviroment Variabels, specify defaults
PHONE_NUMBER = os.environ.get("ALERT_PHONE_NUMBER", "+12234441111")
# cody's number is default
RECEIVER = os.environ.get("RECEIVER_NAME", "Cody") # Cody is default 
receiver
DEPARTMENT = os.environ.get("DEPARTMENT", "Fleet Department")
# Construct message 
message = """Hello {} from {}!
Here are the speeders:
{}
""".format(RECEIVER, DEPARTMENT, speeders.to_string())
# Send message
sns.publish(PhoneNumber = PHONE_NUMBER, Message = message)
