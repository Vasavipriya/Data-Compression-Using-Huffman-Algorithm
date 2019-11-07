import heapq

class Huffman(object):
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

     def __repr__(self):
        return "Huffman(char=%s, freq=%s)" % (self.char, self.freq)

    # needed for node comparison. Utilized to order the nodes appropriately
    # in the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        return (self.left == None and self.right == None)


def maketree(frequencies):
    heap = []
    for char in frequencies: heapq.heappush(heap, char)
    while (len(heap) > 1):
        child0 = heapq.heappop(heap)
        child1 = heapq.heappop(heap)
        parent = Huffman(child0.freq + child1.freq, left=child0, right=child1)
        heapq.heappush(heap, parent)
    return None if heap == [] else heapq.heappop(heap)

def makecodemap(codetree):
    codemap = dict()
    walktree(codetree, codemap,'')
    return codemap
def walktree(codetree, codemap, codeprefix):
    if (len(codetree == 1)):
        freq, label = codetree[0]
        codemap[label] = codeprefix
    else:
        value, child0, child1 = codetree
        walktree(child0, codemap, codeprefix + "0")
        walktree(child1, codemap, codeprefix + "1")


def encode(message, frequencies):
 codemap = makecodemap(maketree(frequencies))
 return ''.join([codemap(letter) for letter in message])


def decode(encodedmessage, frequencies):
    codetree = entiretree = maketree(frequencies)
    decodedletters = []
    for digit in encodedmessage:
        if (digit == '0'):
            codetree = codetree[1]
        else:
            codetree = codetree[2]
            if (len(codetree) == 1):
                frequency, label = codetree[0]
                decoded.append(label)
                codetree = entiretree
    return ''.join(decoded)

    tree=maketree(frequencies)

frequencies = {"a":7, "b":2, "c":1, "d":1, "e":2}
message = "abacdaebfaabd"
encoded = encode(message, frequencies)
print("encoded", encoded)
encoded = '010101110101001000100010001'
decoded = decode(encoded, frequencies)
print("decoded", decoded)
