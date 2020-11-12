legendary_item = "Sulfuras, Hand of Ragnaros"
backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
aged_brie = "Aged Brie"
conjured_item = "Conjured"

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def update_quality(self):
        for item in self.items:
            if item.name != aged_brie and item.name != backstage_pass:
                self.decrease_quality_for_not_legendary_item(item)
            else:
                self.increase_quality_and_check_for_backstage(item)
                    
            if item.name != legendary_item:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != aged_brie:
                    if item.name != backstage_pass:
                        self.decrease_quality_for_not_legendary_item(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.increase_quality(item)

    def decrease_quality_for_not_legendary_item(self,item):
        if item.quality > 0:
            if item.name != legendary_item:
                item.quality = item.quality - 1
                self.decrease_quality_for_conjured_item(item)


    def increase_quality_and_check_for_backstage(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

        if item.name == backstage_pass:
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
    
    def decrease_quality_for_conjured_item(self,item):
        if item.name == conjured_item:
            item.quality = item.quality - 2

""" def update_quality2(self):
       ##     for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
           if item.name != "Sulfuras, Hand of Ragnaros":
               item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1 """
