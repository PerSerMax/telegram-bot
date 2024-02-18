import numpy as np
import pandas as pd


# df = pd.DataFrame({
#     'user_id': [],
#     'chat_id': [],
#     'group': []
# })
#
# df.to_json('users.json')


def add_user(user_id, chat_id, group):
    df = pd.read_json('users.json')
    if all(uid != user_id for uid in df['user_id']):
        df.loc[len(df.index)] = [user_id, chat_id, group]
        df.to_json('users.json')
    else:
        df



add_user(1, 2, 3)
add_user(2, 1, 4)


        

