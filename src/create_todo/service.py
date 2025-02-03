import os
import uuid
import boto3

dynamodb=boto3.resource("dynamodb")
table_name=os.environ["TABLE_NAME"]
table=dynamodb.Table(table_name)

def create_todo_item(data):
    item_id=str(uuid.uuid4())
    todo_item={
        "id":item_id,
        "title":data.get("title"),
        "description":data.get("description"),
        "isCompleted":True if data.get("isCompleted") == "Y" else False
    }
    table.put_item(Item=todo_item)
    return todo_item