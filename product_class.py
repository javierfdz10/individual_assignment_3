# -*- coding: utf-8 -*-

#%%
#"""Imagine you’re creating an application for handling the stock
#of a small shop, and controlling when things go bad in the warehouse.
#
#Given the following class: """
    
class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

#We have a function that calculates the degrading quality of different
#products in a shop.
#Create all the tests you find meaningful for the following function.

def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
                