import os
import uuid
import boto3

dynamodb=boto3.resource("dynamodb")
table_name=os.environ["TABLE_NAME"]
table=dynamodb.Table(table_name)

def delete_todo_item(id):
    try:
        response = table.delete_item(
            Key={"id": id},
            ReturnValues="ALL_OLD"
        )

        if "Attributes" in response:
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": f"To-Do item {id} deleted successfully",
                    "deletedItem": response["Attributes"]
                })
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Item not found"})
            }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }