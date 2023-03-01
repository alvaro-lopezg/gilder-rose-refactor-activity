# -*- coding: utf-8 -*-


QUALITY_MAX_LIMIT = 50
BACKSTAGE_UPPER_LIMIT = 11
BACKSTAGE_MIDDLE_LIMIT = 6
BACKSTAGE_LOWER_LIMIT = 1


def other_process(item):
    if item.quality > 0:
        if item.name == "Conjured":
            item.quality -= 2
        else:
            item.quality -= 1
    if item.sell_in < 1 and item.quality > 0:
        item.quality -= 1


def aged_bried_processor(item):
    if item.quality < QUALITY_MAX_LIMIT:
        item.quality += 1
        if item.sell_in < 1:
            item.quality += 1
    item.sell_in = item.sell_in - 1


def backstage_processor(item):
    if item.quality < QUALITY_MAX_LIMIT:
        item.quality += 1
    if item.sell_in < BACKSTAGE_UPPER_LIMIT:
        item.quality = item.quality + 1
    if item.sell_in < BACKSTAGE_MIDDLE_LIMIT:
        item.quality = item.quality + 1
    if item.sell_in < BACKSTAGE_LOWER_LIMIT:
        item.quality = 0


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                aged_bried_processor(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_processor(item)
            else:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    other_process(item)
                    item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
