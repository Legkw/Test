from mystorage import inmemory

class item:
    id = -1

def test_add():
    #Arrange
    db = {}
    sut = inmemory(db)
    it = item()
    
    #Act
    x = sut.add(it)
    
    #Assert
    assert it.id == 0
    assert len(db) == 1
    assert it.id in db
    
def test_add_two_times():
    # Arrange
    db = {}
    sut = inmemory(db)
    first = item()
    second = item()
    
    # Act
    sut.add(first)
    sut.add(second)
    
    # Assert
    assert len(db) == 2
    assert second.id == 1

def test_get():
    #Arrange
    db = {44: "x"}
    sut = inmemory(db)
    
    #Act
    x = sut.get(44)
    
    #Assert
    x == "x"

def test_delete():
    #Arrange
    db = {44: "x"}
    sut = inmemory(db)
    
    #Act
    sut.delete(44)
    
    #Assert
    assert len(db) == 0
   
def test_delete_a_non_existent_item():
    #Arrange
    db = {}
    sut = inmemory(db)
    
    #Act
    try:
       sut.delete(44)
    except KeyError:
        return

    # Assert
    assert False
