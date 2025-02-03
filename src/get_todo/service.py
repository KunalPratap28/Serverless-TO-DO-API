import os
import uuid
import boto3

dynamodb=boto3.resource("dynamodb")
table_name=os.environ["TABLE_NAME"]
table=dynamodb.Table(table_name)

def get_todo_item():
    try:
        response=table.scan()
        items=response.get("Items",[])
        return items
    
    except Exception as e:
        raise RuntimeError(f"Error fetching ToDo items from DynamoDB: {str(e)}")