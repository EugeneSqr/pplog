from pprint import pformat
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.terminal import TerminalFormatter

def pprint(obj):
    return highlight(pformat(obj), PythonLexer(), TerminalFormatter())[:-1]
