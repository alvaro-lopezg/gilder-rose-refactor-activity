# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_sellin_decrease_by_one_every_Day(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        days = 3

        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEqual(7, item.sell_in)

    def test_quantity_decrease_by_one_every_Day(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        days = 3

        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEqual(17, item.quality)

    def test_quality_no_negative(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=1)
        gilded_rose = GildedRose([item])
        days = 3

        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEqual(0, item.quality)

    def test_validate_sulfuras_no_change(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        self.assertEqual(80, item.quality)
        self.assertEqual(0, item.sell_in)

    def test_validate_sellin_passed(self):  # sell_in date has passed, the value for quality degrades twice faster.
        item = Item(name="+5 Dexterity Vest", sell_in=0, quality=60)
        gilded_rose = GildedRose([item])
        days = 4

        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEqual(52, item.quality)

    def test_validate_aged_brie(self):
        item = Item(name="Aged Brie", sell_in=10, quality=2)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        self.assertEqual(3, item.quality)
        self.assertEqual(9, item.sell_in)

    def test_quality_exceeded_limit(self):
        item = Item(name="Aged Brie", sell_in=10, quality=50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(50, item.quality)

    def test_validate_backstage_quality(self):  # sell_in value is more than 10, quality increases by 1.
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=40)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(41, item.quality)

    def test_validate_backstage_quality_double(self):  # sell_in value is less than 10, quality increases by 2.
        items = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=40)
        gilded_rose = GildedRose([items])
        gilded_rose.update_quality()
        self.assertEqual(42, items.quality)

    def test_validate_backstage_quality_triple(self):  # sell_in value is less than 5, quality increases by 3
        items = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=40)
        gilded_rose = GildedRose([items])
        gilded_rose.update_quality()
        self.assertEqual(43, items.quality)

    def test_validate_backstage_quality_set_zero(self):
        items = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-9, quality=30)
        gilded_rose = GildedRose([items])
        gilded_rose.update_quality()
        self.assertEqual(0, items.quality)

    def test_conjured(self):
        items = Item(name="Conjured", sell_in=6, quality=2)
        gilded_rose = GildedRose([items])
        gilded_rose.update_quality()
        self.assertEqual(0, items.quality)
        self.assertEqual(5, items.sell_in)


if __name__ == '__main__':
    unittest.main()
