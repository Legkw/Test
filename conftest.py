import pytest
from unittest.mock import Mock 
from myapp import create_app


@pytest.fixture
def app():
    storage = Mock()
    storage.add = Mock()
    storage.get = Mock()
    storage.delete = Mock()

    app = create_app(storage)
    app.debug = True
    return app
   
