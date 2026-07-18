import aws_cdk as core
import aws_cdk.assertions as assertions

from my_cloud_project.my_cloud_project_stack import MyCloudProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_cloud_project/my_cloud_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyCloudProjectStack(app, "my-cloud-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
