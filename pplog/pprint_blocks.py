import re
import json

import jq

def get(log_entry):
    if not log_entry:
        return []
    return filter(lambda x: x.parsed, map(_parse, re.finditer('({.*?})', log_entry)))

def transform(data, query):
    try:
        return next(iter(jq.compile(query).input(data).all()), None)
    except ValueError:
        return data

def _parse(match):
    matched_string = _get_matched_string(match)
    return type('', (), {
        'raw': matched_string,
        'parsed': _parse_json(matched_string) or _parse_python_dict(matched_string),
    })

def _get_matched_string(match):
    return match.group(0)

def _parse_json(matched_string):
    try:
        return json.loads(matched_string)
    except json.decoder.JSONDecodeError:
        return None

def _parse_python_dict(matched_string):
    try:
        return eval(matched_string) #pylint:disable=eval-used; this is by design
    except Exception:               #pylint:disable=broad-except; eval can throw anything
        return None
