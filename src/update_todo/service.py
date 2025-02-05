import os
import uuid
import boto3
import json

dynamodb=boto3.resource("dynamodb")
table_name=os.environ["TABLE_NAME"]
table=dynamodb.Table(table_name)

def update_todo_item(id,data):
    try:
        response=table.get_item(
            Key={'id':id}
        )
        if 'Item' not in response:
            return {
                'statusCode':404,
                'body':json.dumps({'error':'ToDo item not found'})
            }
        logger.info(f"Item fetched successfully {response}")
        existing_item = response['Item']
        update_expression=[]
        expression_atttribute_values={}
        if 'title' in data:
            update_expression.append('title = :title')
            expression_atttribute_values[':title']=data['title']
        if 'description' in data:
            update_expression.append('description = :description')
            expression_atttribute_values[':description']=data['description']
        if 'isCompleted' in data:
            update_expression.append('isCompleted = :isCompleted')
            expression_atttribute_values[':isCompleted']=data['isCompleted']
        
        if not update_expression:
            return {
                'statusCode':400,
                'body':json.dumps({'error':'No fields provided to update'})
            }
        update_expression_str='SET '+', '.join(update_expression)
        updated_data=table.update_item(
            Key={'id':id},
            UpdateExpression=update_expression_str,
            ExpressionAttributeValues=expression_atttribute_values,
            ReturnValues="ALL_NEW"
        )
        logger.info(f"Item updated successfully  {updated_data}")
        return {
            'statusCode':200,
            'body':json.dumps({
                'message':'ToDo item updated successfully',
                'data':updated_data
            })
        }
    
    except Exception as e:
        return {
            'statusCode':500,
            'body':json.dumps({'error':str(e)})
        }