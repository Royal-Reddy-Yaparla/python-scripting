# Script 001

"""
This Script Creates a New SNS Topic
"""

import boto3
import botocore


def create_sns_topic(name, display_name, key, value):
    """
    Creates a SNS Topic and prints the ARN

    Args:
        name (str) : The Name For the SNS Topic
        display_name (str) : The Display Name For the SNS Topic
        key (str) : The Tag Key
        value (str) : The Tag Value
    
    Returns:
        None
    """

    try:
        sns_resource = boto3.resource("sns")

        topic = sns_resource.create_topic(
            Name=name,
            Attributes={
                "DisplayName": display_name
                },
            Tags=[
                {
                    "Key": key, "Value": value
                }
            ],
        )

        print(f"SNS Topic has been created: {topic.arn}")
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)


if __name__ == "__main__":
    try:
        topic_name = input("Enter the Topic Name: ")
        topic_display_name = input("Enter the Topic Display Name: ")
        tag_key = input("Enter the Tag Key: ")
        tag_value = input("Enter the Tag Value: ")

        create_sns_topic(topic_name, topic_display_name, tag_key, tag_value)
    except ValueError as value_error:
        print(value_error)
    except KeyboardInterrupt:
        print("Keyboard Interrupt! Exiting the Script!")
