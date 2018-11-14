from db import get_users_table

def get():
    table = get_users_table()
    return table.all()