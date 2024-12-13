import pytest 
from items import Item 

def test_item ():
    item = Item('pillow', 50, 2)
    assert item.name == ' pillow'
    assert item._Item__price == 50 
    assert item.quantity == 2
    assert item.total_price == 100

def test_discount():
    item = Item('discounted item', 100.0, 2)
    item.apply_discount ()
    assert item._Item_price == 70.0

def test_name_setter():
   item = Item('bedsheets', 100, 1)
   item.name = 'NewName'
   with pytest.raises(ValueError):
       item.name = 'this name is too long'  

def test_total_price():
    item = ('wardrobe', 400,3 )
    assert item.total_price == 1200
    
