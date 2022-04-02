import json


def check_json_format(raw_msg):
    if isinstance(raw_msg, str):
        try:
            json.loads(raw_msg)
        except ValueError:
            return False
        return True
    else:
        return False

