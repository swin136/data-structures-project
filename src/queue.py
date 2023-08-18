class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, address):
        self.__next_node = address


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        # Аттрибуты головы и хвоста очереди
        self.__head = None
        self.__tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.__head is None:
            # Очередь пустая
            self.__head = node
            self.__tail = node
        else:
            # Очередь не пустая!
            self.__tail.next_node = node
            self.__tail = node

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.__head is None:
            # Очередь пустая -> возвращаем None
            return None
        else:
            # Очередь не пустая - берем данные из начала очереди
            data = self.__head.data
            if self.__head == self.__tail:
                # Мы извлекли данные из последнего элемента очереди - присваиваем указателям начала и конца очереди
                # значение None
                self.__tail = None
                self.__head = None
            else:
                # Указатель начала очереди указывает на элемент после извлеченного
                self.__head = self.__head.next_node
            return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.__head is None:
            # Очередь пустая
            return ""
        else:
            # Очередь не пустая
            node = self.__head
            str_data = ""
            # Последовательно проходим по очереди
            while node is not None:
                str_data += node.data + "\n"
                node = node.next_node
        return str_data.strip()
