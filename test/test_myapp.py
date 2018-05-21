import pytest, json
from flask import url_for
from unittest.mock import Mock
from myapp import create_app

@pytest.fixture
def mock_storage():
    storage = Mock()
    storage.add = Mock()
    storage.get = Mock()
    storage.delete = Mock()
    return storage

@pytest.fixture
def app(mock_storage):
    app = create_app(mock_storage)
    app.debug = True
    return app

def test_items_delete_noarg(client, mock_storage):
    res = client.delete(url_for('items'))
    assert res.status_code == 405
    mock_storage.delete.assert_not_called()
    
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
    mock_storage.delete.assert_not_called()


@pytest.mark.xfail
def test_item_post():
    assert False

@pytest.mark.xfail
def test_item_get():
    assert False

@pytest.mark.xfail
def test_item_delete():
    assert False