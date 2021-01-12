import json

class Selection():
    def __init__(self, serialized):
        self._serialized = serialized

    def serialize(self):
        return self._serialized

    def deserialize(self):
        return self._deserialize_json() or self._deserialize_python_dict()

    def _deserialize_json(self):
        try:
            return json.loads(self._serialized)
        except json.decoder.JSONDecodeError:
            return None

    def _deserialize_python_dict(self):
        try:
            return eval(self._serialized) #pylint:disable=eval-used; this is by design
        except Exception:                 #pylint:disable=broad-except; eval can throw anything
            return None

def get_selections(log_entry):
    if not log_entry:
        return []
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
                blocks.append(Selection(current_block))
                current_block = ''
        elif balance > 0:
            current_block += char
    return blocks
