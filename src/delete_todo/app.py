import json
from service import delete_todo_item
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        logger.info(f"Received event: {event}")
        todo_id=event['pathParameters']['id']
        return delete_todo_item(todo_id)
    
    except Exception as e:
        return {
            'statusCode':500,
            'body':json.dumps({'error':str(e)})
        }