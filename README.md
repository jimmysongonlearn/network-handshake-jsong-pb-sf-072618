
# Network Handshake

## Try it


```python
# Handshake Example

from network import SimpleNode, VersionMessage

node = SimpleNode('tbtc.programmingblockchain.com', testnet=True, logging=True)

version = VersionMessage()
node.send(version.command, version.serialize())
print(node.wait_for_commands([b'verack']))
```

## Test Driven Exercise


```python
# Exercise 4.1

from network import SimpleNode, VersionMessage

class SimpleNode(SimpleNode):

    def handshake(self):
        '''Do a handshake with the other node. Handshake is sending a version message and getting a verack back.'''
        # create a version message
        # send the command
        # wait for a verack message
        raise NotImplementedError
```
