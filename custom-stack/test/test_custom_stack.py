import pytest
from custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException 

def test_push():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.size() == 1
    stack.push(2)
    assert stack.size() == 2
    stack.push(3)
    assert stack.size() == 3

    # Verificar se a exceção StackFullException é levantada quando a pilha está cheia
    with pytest.raises(StackFullException):
        stack.push(4)

def test_pop():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    # Verificar se a exceção StackEmptyException é levantada quando a pilha está vazia
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_top():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.size() == 2

    stack.pop()
    assert stack.top() == 1
    assert stack.size() == 1

    stack.pop()
    # Verificar se a exceção StackEmptyException é levantada quando a pilha está vazia
    with pytest.raises(StackEmptyException):
        stack.top()

def test_size_and_isEmpty():
    stack = CustomStack(3)
    assert stack.size() == 0
    assert stack.isEmpty() == True

    stack.push(1)
    assert stack.size() == 1
    assert stack.isEmpty() == False

    stack.pop()
    assert stack.size() == 0
    assert stack.isEmpty() == True
