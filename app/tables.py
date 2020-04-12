from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=True)
    username = Col('Names')
    email = Col('Emails')