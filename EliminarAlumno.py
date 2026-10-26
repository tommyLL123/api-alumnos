import boto3

def lambda_handler(event, context):
    # Entrada desde la URL (pathParameters)
    tenant_id = event['pathParameters']['tenant_id']
    alumno_id = event['pathParameters']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        ReturnValues='ALL_OLD'  # Solicita a DynamoDB retornar los datos eliminados
    )
    
    # Salida (json)
    return {
        'statusCode': 200,
        'alumno_eliminado': response.get('Attributes', None)
    }
