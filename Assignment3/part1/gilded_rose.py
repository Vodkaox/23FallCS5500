# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  

            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in > 10:
                    item.quality += 1 
                elif 6 <= item.sell_in <= 10:
                    item.quality += 2 
                elif 1 <= item.sell_in <= 5:
                    item.quality += 3 
                else:
                    item.quality = 0 
                item.quality = min(item.quality, 50)
                item.sell_in -= 1

            else:
                decrement = 1 
                if 'Conjured' in item.name:
                    decrement *= 2
                if item.sell_in <= 0:
                    decrement *= 2
                item.quality = max(0, item.quality - decrement)
                item.sell_in -= 1
