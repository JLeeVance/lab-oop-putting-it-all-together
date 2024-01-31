#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, count):
        self.title = title
        self.page_count = count

    @property
    def page_count(self):
        return self._page_count
        
    @page_count.setter
    def page_count(self, count):
        if type(count) == int:
            self._page_count = count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        

            


    

# print("hi")