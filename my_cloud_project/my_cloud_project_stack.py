from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_s3_notifications as s3n,
    # aws_sqs as sqs,
)
from constructs import Construct

class MyCloudProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        my_bucket = s3.Bucket(self,"UploadBucket")

        #This is the Robot(The lambda function)
        my_function = _lambda.Function(
            self,"ProcessFunction",
            runtime = _lambda.Runtime.PYTHON_3_9,
            handler = "process.handler",

            #This line of code looks at your folder
            code = _lambda.Code.from_asset("lambda")
        )

        #telling s3 to triger Lambda when a file is saved
        my_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(my_function)
        )



