# Script for Huffman Coding using Min Heap


class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.val = ''
        self.left = None
        self.right = None


def extract_min(heap, n):
    temp = heap[0]
    heap[0] = heap[n-1]
    heap.pop()
    heapify(heap, 0, n - 1)
    return temp, n - 1


def insert(heap, temp):
    heap.append(temp)
    n = len(heap)
    parent = n//2-1
    child = n-1
    while parent >= 0 and heap[parent].freq > heap[child].freq:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = (parent+1)//2 - 1

    return n


def heapify(arr, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].freq < arr[smallest].freq:
        smallest = left
    if right < n and arr[right].freq < arr[left].freq:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest, n)

    return arr


def create_heap(arr, freq, n):
    heap = [0] * n
    for i in range(n):
        heap[i] = Node(arr[i], freq[i])

    for i in range((n//2)-1, -1, -1):
        heap = heapify(heap, i, n)

    return heap


def print_tree(root):

    if not (root.left and root.right):
        print(root.data, '-', root.val)
        return
    if root.left:
        root.left.val = root.val + '0'
        print_tree(root.left)
    if root.right:
        root.right.val = root.val + '1'
        print_tree(root.right)


def huffman(a, freq, n):
    heap = create_heap(a, freq, n)
    while n > 1:
        left, n = extract_min(heap, n)
        right, n = extract_min(heap, n)
        temp = Node(left.data+right.data, left.freq + right.freq)
        temp.left = left
        temp.right = right
        n = insert(heap, temp)
    return heap[0]


def main():
    a = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    n = len(a)
    root = huffman(a, freq, n)
    print_tree(root)


if __name__ == '__main__':
    main()
