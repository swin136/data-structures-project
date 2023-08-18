class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data: dict, next_node):
        if next_node is None:
            self.__next_node = None
        else:
            if type(next_node) != self.__class__:
                raise TypeError
            self.__next_node = next_node
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, address):
        if address is None:
            self.__next_node = None
        else:
            if type(address) != self.__class__:
                raise TypeError
            self.__next_node = address


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.__begin = None
        self.__end = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.__begin is None:
            # Список пустой
            self.__begin = Node(data, None)
            self.__end = self.__begin
        else:
            # Список непустой
            node = Node(data, self.__begin)
            self.__begin = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.__end is None:
            # Список пустой
            self.__end = Node(data, None)
            self.__begin = self.__end
        else:
            # Список непустой
            node = Node(data, None)
            self.__end.next_node = node
            self.__end = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.__begin
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
