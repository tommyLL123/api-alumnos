import boto3

def lambda_handler(event, context):
    # Entrada desde la URL (pathParameters)
    tenant_id = event['pathParameters']['tenant_id']
    alumno_id = event['pathParameters']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    item = response.get('Item', None)
    
    # Salida (json)
    return {
        'statusCode': 200,
        'alumno': item
    }
