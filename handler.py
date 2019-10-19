import os
import json


# `sls offline` or `sls invoke local`
if os.getenv('IS_OFFLINE') == 'true' or os.getenv('IS_LOCAL'):
    import pydevd
    # pydevd.settrace('172.25.0.1', port=54321, stdoutToServer=True, stderrToServer=True)  # NG (`ip route` in docker)
    pydevd.settrace('host.docker.internal', port=54321, stdoutToServer=True, stderrToServer=True)


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
