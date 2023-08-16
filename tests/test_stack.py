"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node
from src.stack import Stack


class TestNodeStack(unittest.TestCase):
    def test_node(self):
        """Тестирование класса Node"""
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1, n2.next_node)

    def test_stack_push(self):
        """Тестирование метода push класса Stack"""
        # Инициализируем объект stack - экземпляр класса Stack
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        # Проверяем что поле top объекта stack указывает на элемент класса Node
        self.assertTrue(isinstance(stack.top, Node))

        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertIs(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)

    def test_stack_pop(self):
        """Тестирование метода pop класса Stack"""

        # Инициализируем объект stack - экземпляр класса Stack
        stack = Stack()
        stack.push('testdata')
        data = stack.pop()
        self.assertEqual(data, 'testdata')
        self.assertIs(stack.top, None)

        # Инициализируем объект stack - экземпляр класса Stack
        stack = Stack()
        stack.push('data_01')
        stack.push('data_02')
        stack.push('data_03')

        data = stack.pop()
        self.assertEqual(data, 'data_03')
        data = stack.pop()
        self.assertEqual(data, 'data_02')
        self.assertEqual(stack.top.data, 'data_01')
