# Telematics_Streaming_Data

INTRODUCTION

Telematics is the merging of two tech fields ‒ telecommunications (a branch of technology dealing with long distance
transmission of information by cables, phone lines, etc.) and informatics (the study of computational systems).

Telematics deals with building a network of vehicles and telecommunication devices, 
and as such it falls under the IoT (Internet of Things) umbrella.

How Do Telematics Systems Works?

Benefits of telematics systems are;

Reduce fuel and operating costs,

Optimize fleet management and driving standards,

Perform remote diagnostics,

Improve driver and vehicle safety,

Make more informed decisions, and

Provide efficient customer support.

Objective of the project

By creating a firehose stream and written records to the stream we want to read those records 
and do some basic analysis. If we're successful, we will be able to analyse top speeds reached 
by each vehicle. Having this information would prevent drivers from violating speed limits, and 
would likely save many lives.


Skills

How boto3 to use Kinesis and Lambda.

How to run certain operations on AWS.

How to created a few Firehose streams.

How to generating ARNs for various S3 buckets.

How to write a Lambda function that runs every time Firehose writes file to S3.

How to create a Lambda function that transforms data as it moves through the Firehose stream.

How to write code for a Lambda function that transforms the speed from MPH to KPH as it moves through the stream.

Work flow

•	Create Firehose delivery stream. It will set up for being able to send data to the stream, and the stream will put it into the S3 bucket.

•	Create an "sd-vehicle-data" S3 bucket to be used as the destination for our stream.

•	Writing a record to a firehose stream.

•	Reading data from s3 based on an event. We're going to write a Lambda function that runs every time Firehose writes a new file to S3.

Lambda flow

	Firehose writes incoming recordsmto the s3 bucket.

	Put object event fired by S3 triggers our lambda function.

	Lambda layer enables use of pandas to the lambda handler.

	Lambda function handler executes and triggers SNS notification.

	Cody receives sms.

•	Encoding and decoding base64.

•	Create a transformational lambda. First write code for a Lambda function that transforms 
  the speed from MPH to KPH as it moves through the stream.

•	Building a kinesis data analytics application.

•	Get the daily top speed

•	Visualizing streaming data using elastic search.





