# Class Node
class Node:
    def __init__(self, data):
        self.data_node = data
        self.left_node = None
        self.right_node = None

    def is_leaf_node(self):
        return ((self.left_node is None) and (self.right_node is None))

# Class PrefixCodeTree
class PrefixCodeTree:

    # Constructor
    def __init__(self):
        self.root_node = Node('')

    # Insert
    def insert(self, codeword, symbol):
        node = self.root_node

        for code in codeword:
            if (code == 0):
                if (node.left_node is None):
                    node.left_node = Node('')
                    node = node.left_node
                else:
                    node = node.left_node
            else:
                if (node.right_node is None):
                    node.right_node = Node('')
                    node = node.right_node
                else:
                    node = node.right_node

        node.data_node = symbol

    # Decode
    def decode(self, encodedData, datalen):
        message = ''

        # Transform encodedData to bit data
        bit_data = ''.join(f'{_:08b}' for _ in encodedData)
        bit_data = ''.join(bit_data.split())
        bit_data = bit_data[:datalen]

        node = self.root_node

        for i in range(datalen):
            if (bit_data[i] == '0'):
                node = node.left_node
            else:
                node = node.right_node
            if (node.is_leaf_node()):
                message = message + node.data_node
                node = self.root_node

        return message


def test():
    codeTree = PrefixCodeTree()

    codebook = {'x1': [0],
                'x2': [1,0,0],
                'x3': [1,0,1],
                'x4': [1,1]}

    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)

    print(codeTree.decode(b'\xd2\x9f\x20', 21))

if __name__ == "__main__":
     test()
    