import re

def get(log_entry):
    if not log_entry:
        return []
    return map(_parse, re.finditer('({.*?})', log_entry))

def _parse(block_match):
    block_string = block_match.group(0)
    try:
        parsed = eval(block_string) #pylint:disable=eval-used; this is by design
    except Exception:               #pylint:disable=broad-except; eval can throw anything
        parsed = None
    return type('', (), {
        'raw': block_string,
        'parsed': parsed,
    })
