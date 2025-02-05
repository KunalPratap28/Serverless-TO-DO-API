import json
from service import update_todo_item
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        logger.info(f"Received event: {event}")
        todo_id=event['pathParameters']['id']
        body=event.get("body","{}")
        return update_todo_item(todo_id,body)
    
    except Exception as e:
        return {
            'statusCode':500,
            'body':json.dumps({'error':str(e)})
        }