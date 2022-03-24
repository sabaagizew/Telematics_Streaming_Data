# create_firehose.py: Create firehose stream and s3 bucket. No need to edit.
import _setup
firehose, s3, records = _setup.ex_vars

# Create s3 bucket
s3.create_bucket(Bucket='sd-vehicle-data')

# Create Firehose delivery stream
res = firehose.create_delivery_stream(
    DeliveryStreamName =  "gps-delivery-stream",
    DeliveryStreamType = "DirectPut",
    
    # Specify configuration of the destination S3 bucket
    S3DestinationConfiguration = {
        "BucketARN": "arn:aws:s3:::sd-vehicle-data",
        "RoleARN": "arn:aws:iam::0000000:role/firehoseDeliveryRole"
    })
    
