from flask_table import Table, Col, LinkCol

#for showing users
class Results(Table):
    id = Col('Id', show=True)
    username = Col('Names')
    email = Col('Emails')

#showing Primary items.
class P_Items(Table):
    id = Col('Id', show=True)
    clothingItem = Col('Clothing Item')
    quantity = Col('Quantity')
    edit = LinkCol('Edit', 'editDb', url_kwargs=dict(id='id'))
    
#showing 'other' items.
class Other_Items(Table):
    id = Col('Id', show=True)
    clothingItem = Col('Clothing Item')
    quantity = Col('Quantity')

#showing highschool items.
class high_clothes_table(Table):
    id = Col('Id', show=True)
    clothingItem = Col('Clothing Item')
    quantity = Col('Quantitiy')