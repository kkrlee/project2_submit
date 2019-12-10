import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestampe, data):
        if self.head is None:
            self.head = Block(timestamp, data, o)
            return
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp


def get_utc_time():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")


block0 = Block(get_utc_time(), "Some Information", 0)
block1 = Block(get_utc_time(), "Some Information", block0)
block2 = Block(get_utc_time(), "Some Information", block1)
print(block0)
print(block1)
print(block2)