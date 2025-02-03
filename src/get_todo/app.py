import json
from service import get_todo_item
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        logger.info(f"Received event: {event}")
        response=get_todo_item()
        logger.info(f"Items fetched successfully")
        return {
            "statusCode":201,
            "body":json.dumps({
                "message":"TODO items fetched successfully",
                "data":response
            })
        }
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            "statusCode":500,
            "body":json.dumps({
                "message":"Error fetching ToDo items",
                "error":str(e)
            })
        }