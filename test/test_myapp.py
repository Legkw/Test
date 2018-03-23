import pytest, json
from flask import url_for


def test_items_delete(client):
    res = client.delete(url_for('items'))
    assert res.status_code == 405

    
def test_items_post_noarg(client):
    res = client.post(url_for('items'))
    assert res.status_code == 500

    
def test_items_post_valid(client):
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
    #TODO: check if it called add()

def test_items_post_bogus(client):
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
   

@pytest.mark.xfail
def test_item_post():
    assert False

@pytest.mark.xfail
def test_item_get():
    assert False

@pytest.mark.xfail
def test_item_delete():
    assert False