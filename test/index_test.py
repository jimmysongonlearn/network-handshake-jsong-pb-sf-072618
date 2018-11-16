from unittest import TestCase
from ipynb.fs.full.index import *

class SimpleNodeTest(TestCase):

    def test_handshake(self):
        node = SimpleNode('tbtc.programmingblockchain.com', testnet=True)
        node.handshake()
