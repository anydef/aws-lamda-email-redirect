import boto3

import __template as _
import json

client = boto3.client('ses')
SUCCESS_RESPONSE = {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {},
    "body": "Email sent"
}


def failed_response(cause):
    return {
        "isBase64Encoded": False,
        "statusCode": 500,
        "headers": {},
        "body": {'status': 'ERROR', 'msg': cause}
    }


def handler(event, context):
    body = json.loads(event['body'])

    try:
        client.send_email(
            Source='source@email.com',
            Destination={
                'ToAddresses': [
                    'test_account@email.com',
                ]
            },
            Message={
                'Subject': {
                    'Data': body['subject'],
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': _.render_template(subject=body['subject'], name=body['name'], message=body['message']),
                        'Charset': 'UTF-8'
                    }}
            },
            ReplyToAddresses=[
                body['email']
            ]
        )

    except Exception as ex:
        return failed_response(str(ex))
    else:
        return SUCCESS_RESPONSE
