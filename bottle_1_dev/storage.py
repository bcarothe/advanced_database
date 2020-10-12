import sqlite3


def get_items():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return result


def get_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return result


def update_status(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status=? where id=?", (value, id))
    connection.commit()
    cursor.close()


def create_item(task, status):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo (task, status) values (?,?)", (task, status))
    id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return id


def update_item(id, task):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set task=? where id=?", (task, id))
    connection.commit()
    cursor.close()


def delete_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    connection.commit()
    cursor.close()


def test_get_items():
    print("Testing get_items()...")
    results = get_items()
    assert type(results) is list
    assert len(results) > 0, "Length is not greator than 0"
    for item in results:
        assert type(item) is tuple
    id, task, status = results[0]
    assert type(id) is int
    assert type(task) is str
    assert type(status) is int
    assert status in [0, 1]
    print("Test get_items() passed")


def test_get_item():
    print("Testing get_item()...")
    results = get_items()
    assert len(results) > 0
    id, task, status = results[0]
    result = get_item(id)
    assert type(result) is tuple
    id2, task2, status2 = result
    assert id2 == id
    assert task2 == task
    assert status2 == status
    print("Test get_item() passed")


# Will only do something id directly run the file
if __name__ == "__main__":
    # test_get_items()
    test_get_item()
    print("Done")
