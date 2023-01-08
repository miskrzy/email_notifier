import logging
import smtplib
import os

import azure.functions as func

from email_notifier import coordinator

def main(dailyTrigger: func.TimerRequest):
    logging.info('Python HTTP trigger function processed a request.')
    coordinator.run()
