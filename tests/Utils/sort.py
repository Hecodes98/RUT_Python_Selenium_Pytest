class Sort:
    @staticmethod
    def sort_elements(elements):
        elements = [element.text for element in elements]
        elements.sort() 
        return elements
