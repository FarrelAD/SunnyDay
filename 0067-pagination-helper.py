# TITLE: PAGINATION HELPER
# TASK : You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.
#        The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
#        The types of values contained within the collection/array are not relevant.
# Source: https://www.codewars.com/kata/515bb423de843ea99400000a
# 05 April 2024

# 1st
import math

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if len(self.collection) == 0 or page_index < 0 or page_index >= self.page_count():
            return -1
        
        if len(self.collection) % self.items_per_page == 0:
            return self.items_per_page
        else:
            if page_index == self.page_count() - 1:
                return int(len(self.collection) % self.items_per_page)
            elif page_index < self.page_count():
                return self.items_per_page
            else:
                return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        else:
            page = 0
            while item_index >= self.items_per_page:
                item_index -= self.items_per_page
                page += 1
            return page

# Testing
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0)) # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid