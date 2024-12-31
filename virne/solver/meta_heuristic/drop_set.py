

class DropSet: 
    
    def __init__(self, global_drop_variable: int):
        self.global_drop_variable = global_drop_variable
        self.drop_value = 0
        
    def add_item(self, item, drop_set: dict):
        if(self.drop_value >= self.global_drop_variable):
            self.drop_value = 0
        drop_set[self.drop_value] = item
        self.drop_value = self.drop_value + 1               
        

# if __name__ == "__main__":
#     drop_set = DropSet(6)
#     items = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six']
#     drop_set_results = {} 
#     for i in items:
#         drop_set.add_item(i, drop_set_results)
#     print(drop_set_results)
    