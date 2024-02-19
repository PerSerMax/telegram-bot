import numpy as np
import pandas as pd


# Создание базы пользователей
def reset_users():
    df = pd.DataFrame({
        'user_id': [],
        'chat_id': [],
        'group':   []
    })

    df.to_json('users.json')


def add_user(user_id: str, chat_id: int, group: str):
    group = group.upper()
    df = pd.read_json('users.json')
    if all(uid != user_id for uid in df['user_id']):
        df.loc[len(df.index)] = [user_id, chat_id, group]
        df.to_json('users.json')
    else:
        for i in range(len(df['user_id'])):
            if df['user_id'][i] == user_id:
                df.loc[i] = [user_id, chat_id, group]
                df.to_json('users.json')
    print(user_id, chat_id, group)


def find_group(user_id):
    df = pd.read_json('users.json')
    for i in range(len(df['user_id'])):
        if df['user_id'][i] == user_id:
            return df['group'][i]


# Создание базы расписаний
def reset_schedule():
    df = pd.DataFrame({
        'group':      [],
        'day':        [],
        'number':     [],
        'time':       [],
        'classroom':  [],
        'lesson':     [],
        'teacher':    [],
    })

    df.to_json('schedule.json')


def set_schedule(group: str, day: str, number: str, time: str, classroom: str, lesson: str, teacher: str):
    day = day.upper()
    df = pd.read_json('schedule.json')
    if all(df['group'][i] != group and df['day'][i] != day and df['number'][i] != number for i in range(len(df['group']))):
        df.loc[len(df.index)] = [group, day, number, time, classroom, lesson, teacher]
        df.to_json('schedule.json')
    else:
        for i in range(len(df['group'])):
            if df['group'][i] == group and df['day'][i] == day and df['number'][i] == number:
                df.loc[i] = [group, day, number, time, classroom, lesson, teacher]
                df.to_json('schedule.json')


def find_schedule(group, day):
    df = pd.read_json('schedule.json')
    pass



