import logging

import azure.functions as func

from smsAlert import smsAlertMsg

username = 'madhurdk2001@gmail.com'  # add your SMS Alert username
password = '123456'  # add your SMS Alert password

client = smsAlertMsg(username=username, password=password)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    mobileno = req.params.get('mobileno')
    message = req.params.get('message')
    senderid = req.params.get('sender')
    route = req.params.get('route')

    if not (message and mobileno):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            message = req_body.get(message)
            mobileno = req_body.get(mobileno)
            senderid = req_body.get('sender')
            route = req_body.get('route')

    if (message and mobileno):
        res = client.send_sms(mobileno, message, senderid, route)
        return func.HttpResponse(f"{res['description']['desc']}")
    else:
        return func.HttpResponse(
            "Pass the mobileno, message, sender, route in the query string to send the SMS.",
            status_code=200
        )
