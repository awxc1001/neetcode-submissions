#doublely linked node
class Node:
    #Node 里要存 key 和 val，是因为删除 LRU 节点时，
    #需要通过 node.key 从 hashmap 里 del dict[key]，否则无法locate key O(1) 删除。
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    # prev  <-  node  ->  next
    # None      node      None

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.cache = {}

        #use two sentinel dummy for easy insert,remove,get. no need edge case check
        #if no two dummy每删一个节点，你都要问一遍：“它是不是头？它是不是尾？它是不是唯一的节点？
        #we dont care what they store, because our cache dict will not store them with any key
        #no key pair in our cache for these 2
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        #link these two first   #head <-> real nodes here <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

        #head.next will always be the oldest,  tail.prev will alwasy be the most recent


    #two inside function for linked list operation, we use node as input
    #head <-> real nodes <-> tail, this wont cause none.next none.prev edge cases
    def add_to_tail(self, node):
        #add to infront of tail only, no other operations like remove, done by other api
        prev = self.tail.prev
        
        prev.next = node
        node.next = self.tail
        
        self.tail.prev = node
        node.prev = prev


    #simply remove from the linkedlist
    def remove(self, node):
        #only reassign pointers, removely this node from list only
        node.prev.next = node.next
        node.next.prev = node.prev

    #get = 查 hashmap + 移到尾部（变最近使用）
    def get(self, key: int) -> int:
        if key in self.cache:
            target_node = self.cache[key]
            #base LRU policy remove first, and add to tail as latest
            self.remove(target_node)
            self.add_to_tail(target_node)
            return target_node.val
        return -1

    #put = 更新/删除旧节点 + 必要时淘汰 LRU + 插入新节点
    def put(self, key: int, value: int) -> None:
        #make a new key-value pair in cache with this new node, update create new one same thing
        new_node = Node(key, value)

        #if already stored remove the old node
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        #update cache and list, insert this new one in tail
        self.cache[key] = new_node
        self.add_to_tail(new_node)

        #remove least node in cache if capcity broke
        if len(self.cache) > self.capa:
            least_node = self.head.next
            key = least_node.key
            self.remove(least_node)
            del self.cache[key]
            
        
