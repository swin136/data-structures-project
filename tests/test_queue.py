"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import copy
import unittest
from src.queue import Node
from src.queue import Queue


def get_sample_queue():
    """Формируем очередь для проведения тестов"""
    sample_queue = Queue()
    sample_queue.enqueue('test data #1')
    sample_queue.enqueue('test data #2')
    sample_queue.enqueue('test data #3')
    return sample_queue


class TestNodeQueue(unittest.TestCase):
    def test_node(self):
        """Тестирование класса Node из src/queue.py"""

        # Создаем первый тестовый элемент
        node_1 = Node('Test data 1', None)
        self.assertEqual(node_1.data, 'Test data 1')
        # Тестируем защиту аттрибутов элемента класса
        with self.assertRaises(AttributeError):
            node_1.data = "Test data 2"

        # Создаем второй тестовый элемент и помещаем его в очередь вслед за первым
        node_2 = Node('Test data 2', None)
        node_1.next_node = node_2

        # Проверяем правильность доступа к аттрибутам второго элемента через первый
        self.assertEqual(node_1.next_node.data, 'Test data 2')
        self.assertIs(node_1.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            print(node_1.next_node.next_node.data)

    def test_str_method(self):
        """Проверяем магический метод __str__ класса Queue"""
        # Проверяем работу метода __str__ на пустой очереди
        self.assertEqual(str(Queue()), "")
        # Проверяем работу метода __str__ на заполненной очереди
        self.assertEqual(str(get_sample_queue()), 'test data #1\ntest data #2\ntest data #3')

    def test_storage_data(self):
        """Проверяем очередность хранения данных"""
        queue = copy.deepcopy(get_sample_queue())
        # queue = get_sample_queue()
        self.assertEqual(queue.head.data, 'test data #1')
        # Последний элемент очереди
        self.assertEqual(queue.tail.data, 'test data #3')

        # Проверяем правильность перемещения от первого элемента очереди к последнему
        self.assertEqual(queue.head.next_node.data, 'test data #2')
        self.assertEqual(queue.head.next_node.next_node.data, 'test data #3')
        # Проверяем, что последний элемент очереди ссылается на None
        self.assertIs(queue.head.next_node.next_node.next_node, None)
        # Проверяем, что последний элемент очереди, действительно является последним
        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)


    def test_dequeue(self):
        """Проверяем работу метода dequeue класса Queue"""
        queue = copy.deepcopy(get_sample_queue())
        self.assertEqual(queue.dequeue(), "test data #1")
        self.assertEqual(queue.dequeue(), "test data #2")
        self.assertEqual(queue.dequeue(), "test data #3")
        self.assertIs(queue.dequeue(), None)

        # Еще раз заполняем нашу очередь
        queue.enqueue('1-й элемент')
        queue.enqueue('2-й элемент')
        # Новая итерация тестирования метода dequeue
        self.assertEqual(queue.dequeue(), "1-й элемент")
        self.assertEqual(queue.dequeue(), "2-й элемент")
        self.assertIs(queue.dequeue(), None)
