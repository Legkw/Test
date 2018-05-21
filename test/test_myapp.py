#bandit: disable=

import json
import pytest
from flask import url_for
from unittest.mock import Mock
from myapp import create_app

@pytest.fixture
def validid(): return 44

@pytest.fixture
def bogusid():
    return -1
    
@pytest.fixture
def mock_storage(validid, bogusid):
    storage = Mock()
    
    storage.get(validid, return_value=object())
    storage.get(bogusid, side_effect=KeyError('foo'))
    
    storage.add = Mock()
    
    storage.delete = Mock()
    
    return storage

@pytest.fixture
def app(mock_storage):
    app = create_app(mock_storage)
    app.debug = True
    return app

def test_items_post_noarg(client, mock_storage):
    res = client.post(url_for('items'))
    assert res.status_code == 500
    mock_storage.add.assert_not_called()
    
def test_items_post_valid(client, mock_storage):
    payload = {
        "date_from": "2018-03-23",
        "date_till": "2018-03-23"
        }
    res = client.post(
        url_for('items'), 
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json',}
        )
    assert res.status_code == 200
    mock_storage.add.assert_called()

def test_items_post_bogus(client, mock_storage):
    month = "13"
    payload = {
        "date_from": "2018-" + month + "-23",
        "date_till": "2018-03-23"
        }
    res = client.post(
        url_for('items'), 
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json',}
        )
    assert res.status_code == 500
    # TODO: mock_storage.add.assert_not_called()


def test_item_get_invalid(client, bogusid, mock_storage):
    # Arrange
    url = url_for('item', id=bogusid)
    
    # Act
    res = client.get(url)
    
    # Assert
    assert res.status_code == 404

def test_item_get_valid(client, validid, mock_storage):
    # Arrange
    url = url_for('item', id=validid)
    
    # Act
    res = client.get(url)
    
    # Assert
    mock_storage.get.assert_called_with(validid)
    
@pytest.mark.xfail
def test_item_delete_valid():
    assert False
    
    
def test_items_delete_noarg(client, mock_storage):
    res = client.delete(url_for('items'))
    assert res.status_code == 405
    mock_storage.delete.assert_not_called()
    
    