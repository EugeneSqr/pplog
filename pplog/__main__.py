import sys
import signal
from pprint import pformat

import jq
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.terminal import TerminalFormatter

from .log_entry_parser import get_selections

def main():
    signal.signal(signal.SIGINT, lambda _, __: sys.exit(0))
    compiled_query = jq.compile(sys.argv[1] if len(sys.argv) > 1 else '')
    for line in sys.stdin:
        for selection in get_selections(line):
            deserialized_selection = selection.deserialize()
            if not deserialized_selection:
                continue
            query_result = query_safely(deserialized_selection, compiled_query)
            line = line.replace(selection.serialize(), to_pretty_string(query_result))
        sys.stdout.write(line)

def query_safely(obj, query):
    try:
        result_items = query.input(obj).all()
        return result_items[0] if len(result_items) == 1 else result_items
    except ValueError:
        return obj

def to_pretty_string(obj):
    return highlight(pformat(obj), PythonLexer(), TerminalFormatter())[:-1]

if __name__ == '__main__':
    main()
