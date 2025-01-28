import json
from service import create_todo_item
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        logger.info(f"Received event: {event}")
        body=json.loads(event.get("body","{}"))
        response=create_todo_item(body)
        logger.info(f"Item created successfully")
        return {
            "statusCode":201,
            "body":json.dumps({
                "message":"TODO item created successfully",
                "data":response
            })
        }
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            "statusCode":500,
            "body":json.dumps({
                "message":"Error creating ToDo item",
                "error":str(e)
            })
        }