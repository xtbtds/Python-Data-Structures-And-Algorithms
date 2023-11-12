from collections import defaultdict
import heapq




def huffman_code(string):
    freq = defaultdict(int)

    for i in string:
        freq[i] += 1


    class TreeNode:
        def __init__(self, value, frequency, left=None, right=None, code = ''):
            self.value: str = value
            self.frequency: int = frequency
            self.left = left
            self.right = right
            self.code = code

        def __lt__(self, something):
            return self.frequency < something.frequency


    H = []

    for i in freq:
        heapq.heappush(H, TreeNode(i, freq[i]))


    while len(H) > 1:

        a: TreeNode = heapq.heappop(H)
        b: TreeNode = heapq.heappop(H)
        new_node = TreeNode(value = a.value + b.value, frequency=a.frequency + b.frequency, left=a, right=b)
        heapq.heappush(H, new_node)


    codes = {}
    queue = [H[0]]
    while queue:
        node = queue.pop(0)
        if len(freq) == 1:
            codes[node.value] = "0"
            break
        
        if node.left:
            node.left.code = node.code + "0"
            queue.append(node.left)
        if node.right:
            node.right.code = node.code + "1"
            queue.append(node.right)
        if not (node.right and node.left):
            codes[node.value] = node.code
    return codes





if __name__ == "__main__":

    string = input()
    codes = huffman_code(string)
    encoded_string = ''.join([codes[k] for k in string])
    print(f"{len(codes)} {len(encoded_string)}")

    for i in codes:
        print(f"{i}:", codes[i])

    print(encoded_string)
from collections import defaultdict
import heapq




def huffman_code(string):
    freq = defaultdict(int)

    for i in string:
        freq[i] += 1


    class TreeNode:
        def __init__(self, value, frequency, left=None, right=None, code = ''):
            self.value: str = value
            self.frequency: int = frequency
            self.left = left
            self.right = right
            self.code = code

        def __lt__(self, something):
            return self.frequency < something.frequency


    H = []

    for i in freq:
        heapq.heappush(H, TreeNode(i, freq[i]))


    while len(H) > 1:

        a: TreeNode = heapq.heappop(H)
        b: TreeNode = heapq.heappop(H)
        new_node = TreeNode(value = a.value + b.value, frequency=a.frequency + b.frequency, left=a, right=b)
        heapq.heappush(H, new_node)


    codes = {}
    queue = [H[0]]
    while queue:
        node = queue.pop(0)
        if len(freq) == 1:
            codes[node.value] = "0"
            break
        
        if node.left:
            node.left.code = node.code + "0"
            queue.append(node.left)
        if node.right:
            node.right.code = node.code + "1"
            queue.append(node.right)
        if not (node.right and node.left):
            codes[node.value] = node.code
    return codes





if __name__ == "__main__":

    string = input()
    codes = huffman_code(string)
    encoded_string = ''.join([codes[k] for k in string])
    print(f"{len(codes)} {len(encoded_string)}")

    for i in codes:
        print(f"{i}:", codes[i])

    print(encoded_string)
