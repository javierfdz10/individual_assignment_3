#%%

from product_class import recalculate_quality, Product

def test_recalculate_potato():
    potato = Product("potato",5)
    recalculate_quality(potato)
    assert potato.quality == 4.5
    
def test_recalculate_cheese():
    cheese = Product("cheese",5)
    recalculate_quality(cheese)
    assert cheese.quality == 3

def test_recalculate_water():
    water = Product("water",5)
    recalculate_quality(water)
    assert water.quality == 5

def test_recalculate_beer():
    beer = Product("beer",10.95)
    recalculate_quality(beer)
    assert beer.quality == 10.95

def test_recalculate_bread():
    bread = Product("bread",3)
    recalculate_quality(bread)
    assert bread.quality == 0
    
def test_recalculate_chocolate():
    chocolate = Product("chocolate",2)
    recalculate_quality(chocolate)
    assert chocolate.quality == -1
    
def test_recalculate_fish():
    fish = Product("fish",1.5)
    recalculate_quality(fish)
    assert fish.quality == -1.5

def test_recalculate_leila():
    leila = Product("leila",1)
    recalculate_quality(leila)
    assert leila.quality == -2
