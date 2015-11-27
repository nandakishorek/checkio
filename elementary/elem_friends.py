class Friends:
    
    def __init__(self, connections):
        self.network = {}
        for con in connections:
            self.add(con)

    def add(self, connection):
        added = False
        for f in connection:
            diff = connection.difference({f})
            try:
                self.network[f].update(diff)
            except KeyError:
                self.network[f] = diff
                added = True
        return added

    def remove(self, connection):
        try:
            for f in connection:
                self.network[f] -= connection.difference({f})
                if len(self.network[f]) < 1:
                    del self.network[f]
            return True
        except KeyError:
            return False

    def names(self):
        nodes = set(self.network.keys())
        return nodes

    def connected(self, name):
        try:
            return self.network[name]
        except KeyError:
            return set()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
