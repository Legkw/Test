from io import StringIO
from unittest.mock import patch

def hello():
    print('Hello world')

	
@patch('sys.stdout', new_callable=StringIO)
def test_hello(mock_stdout):
    hello()
    assert mock_stdout.getvalue() == 'Hello world\n'
