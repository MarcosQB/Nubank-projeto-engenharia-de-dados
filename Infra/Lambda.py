#Acionar StepFunction
import boto3
import json
import random

def lambda_handler(event, context):
    # Substitua 'YOUR_STEP_FUNCTIONS_ARN' pelo ARN da sua máquina de estados Step Functions
    name = random.randint(100000,10000000)
    stepfunctions_arn = 'arn:aws:states:us-east-1:373049988265:stateMachine:nubank-machine'
    
    # Dados que serão passados como entrada para a execução da Step Function
    input_data = {
        "key1": "value1",
        "key2": "value2"
        # Adicione mais dados conforme necessário
    }
    
    # Cria um cliente do AWS Step Functions usando o Boto3
    client = boto3.client('stepfunctions')
    
    try:
        # Inicia a execução da Step Function
        response = client.start_execution(
            stateMachineArn=stepfunctions_arn,
            name=str(name),  # Escolha um nome único para cada execução, ou deixe vazio para usar um nome gerado automaticamente
            input=json.dumps(input_data)
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Execução iniciada com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao iniciar a execução: {str(e)}')
        }
