class DefaultList(list):
    
    def __init__(self, backup_value) -> None:
        super().__init__(self)
        self.backup_value = backup_value
    
    def __getitem__(self, index):
        try:
            return list.__getitem__(self, index)
        except IndexError:
            return self.backup_value

s = DefaultList(51)
s.extend([1, 5, 7])

indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")