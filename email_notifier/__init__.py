import logging
import smtplib
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
                "a",
                status_code=200
        )

    try:
        email = "schedumail.skr@gmail.com"
        passw = os.environ["gmail_app_pass"]

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(email,passw)
        server.sendmail(email,email,"hello world")
        server.quit()

    except Exception as e:
                return func.HttpResponse(
                e,
                status_code=200
        )
    else:
        return func.HttpResponse(
                os.environ["myvartest"],
                status_code=200
        )