class Human:
    def __init__(self, name, *entities, magic=0):
        self.name = name
        self.entities = [entity for entity in entities]
        self.magic = magic

    def change_name(self, dname):
        self.name += ' ' + dname

    def __iadd__(self, other):
        self.entities.extend(other.split())
        self.magic += len(other) // 4
        return self

    def __sub__(self, other):
        newEntities = sorted(set(self.entities[:]))
        for entity in other.entities:
            if entity in newEntities:
                newEntities.remove(entity)
        newHuman = Human(self.name[:3].capitalize() + other.name[-3:].capitalize(), *newEntities)
        return newHuman

    def __call__(self, nm):
        return self.entities[:nm]

    def __eq__(self, other):
        if self.magic == other.magic:
            if len(self.entities) == len(other.entities):
                return self.name == other.name
        return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.magic < other.magic:
            return True
        elif self.magic == other.magic:
            if len(self.entities) < len(other.entities):
                return True
            elif len(self.entities) == len(other.entities):
                return self.name < other.name
        return False

    def __le__(self, other):
        if self.magic < other.magic:
            return True
        elif self.magic == other.magic:
            if len(self.entities) < len(other.entities):
                return True
            elif len(self.entities) == len(other.entities):
                return self.name <= other.name
        return False

    def __gt__(self, other):
        if self.magic > other.magic:
            return True
        elif self.magic == other.magic:
            if len(self.entities) > len(other.entities):
                return True
            elif len(self.entities) == len(other.entities):
                return self.name > other.name
        return False

    def __ge__(self, other):
        if self.magic > other.magic:
            return True
        elif self.magic == other.magic:
            if len(self.entities) > len(other.entities):
                return True
            elif len(self.entities) == len(other.entities):
                return self.name >= other.name
        return False

    def __str__(self):
        entities = ', '.join(self.entities)
        return f'''Human by name {self.name} ({entities}, {self.magic})'''


hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
hm.change_name('Rual')
id_hm = id(hm)
hm += 'Skyman'
print(hm, hm(2), sep='\n')
print(id_hm == id(hm))
