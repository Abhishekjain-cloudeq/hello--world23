import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    print("I am laerning azure timer trigger function")

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
