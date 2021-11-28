# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_id=2
    task = filter(lambda t: t['id'] == task_id, tasks)
    print(list(task))
    task1 = filter(lambda t: t['id'] == 1, tasks)
    print(list(task1))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
