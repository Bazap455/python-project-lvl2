import json
import yaml
from pathlib import Path


def parse(file_path):
    file_extension = Path(file_path).suffix

    if file_extension == '.json':
        data = json.load(open(file_path))
    elif (file_extension == '.yml') or (file_extension == '.yaml'):
        stream = open(file_path, 'r')
        data = yaml.safe_load(stream)
        stream.close()
    else:
        raise Exception(UnboundLocalError)

    return data
