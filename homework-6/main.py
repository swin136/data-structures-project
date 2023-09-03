from src.linked_list import LinkedList

if __name__ == '__main__':
    # Создаем и наполняем односвязный список
    ll = LinkedList()

    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})

    # метод to_list()
    lst = ll.to_list()
    for item in lst:
        print(item)
    # {'id': 0, 'username': 'serebro'}
    # {'id': 1, 'username': 'lazzy508509'}
    # {'id': 2, 'username': 'mik.roz'}
    # {'id': 3, 'username': 'mosh_s'}

    # метод get_data_by_id()
    user_data = ll.get_data_by_id(3)
    assert user_data == {'id': 3, 'username': 'mosh_s'}

    # работа блока try/except
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    user_data = ll.get_data_by_id(2)
    # Данные не являются словарем или в словаре нет id.
    # Данные не являются словарем или в словаре нет id.
    print(user_data)
    # {'id': 2, 'username': 'mosh_s'}
