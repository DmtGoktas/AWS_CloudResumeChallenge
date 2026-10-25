import json
import boto3
print(boto3.__version__)
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("visitorCounter")

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": 1},
            UpdateExpression="ADD #count :inc",
            ExpressionAttributeNames={"#count": "count"},
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW"
        )

        count = int(response["Attributes"]["count"])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://demetgoktas.me",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            },
            "body": json.dumps({"count": count})
        }

    except Exception as e:
        print(f"Counter error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://demetgoktas.me"
            },
            "body": json.dumps({"error": "Counter unavailable"})
        }


print(boto3.__version__)
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("visitorCounter")

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": 1},
            UpdateExpression="ADD #count :inc",
            ExpressionAttributeNames={"#count": "count"},
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW"
        )

        count = int(response["Attributes"]["count"])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://demetgoktas.me",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            },
            "body": json.dumps({"count": count})
        }

    except Exception as e:
        print(f"Counter error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://demetgoktas.me"
            },
            "body": json.dumps({"error": "Counter unavailable"})
        }


