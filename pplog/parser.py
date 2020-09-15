import re
import json

def parse_log_entry(log_entry):
    if not log_entry:
        return []
    return filter(lambda x: x.parsed, map(_parse, re.finditer('({.*?})', log_entry)))

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
