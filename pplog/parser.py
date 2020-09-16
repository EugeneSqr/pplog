import json

def parse_log_entry(log_entry):
    if not log_entry:
        return []
    return filter(lambda x: x.parsed, _parse(log_entry))

def _parse(log_entry):
    balance = 0
    blocks = []
    current_block = ''
    for char in log_entry:
        if char == '{':
            current_block += char
            balance += 1
        elif char == '}':
            current_block += char
            balance -= 1
            if balance == 0:
                blocks.append(type('block', (), {
                    'raw': current_block,
                    'parsed': _parse_json(current_block) or _parse_python_dict(current_block),
                }))
                current_block = ''
        elif balance > 0:
            current_block += char
    return blocks

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
