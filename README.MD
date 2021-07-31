# Send SMS Messages With Python and Azure Functions:

## Prerequisites -

* You must have a valid [SMS Alert](https://www.smsalert.co.in) account.
* A Microsoft Azure account.
* Visual Studio Code.

## Steps -

1. Clone this repo
`git clone https://github.com/SMSAlert/azure-function-python-sample.git`

2. Import it into Visual Studio Code.

3. Add SMS Alert `username` & `password` in SendSMS >> __init__.py

4. Install 'Azure Functions' extension in VS Code. Sign in to your Azure account.

5. Deploy to Azure. This will give you an URL for the function once it's done deploying.

6. The URL could be like `https://'function-app'.azurewebsites.net/api/'function-name'`

7. To send the sms we have to pass the query string(mobileno, message, sender, route) in the URL as `https://'function-app'.azurewebsites.net/api/'function-name'?mobileno=918010551055&message=Hello%20from%20Azure&sender=CVDEMO&route=demo`

## More info

You can check out our website https://www.smsalert.co.in
For any questions, please contact us at support@cozyvision.com