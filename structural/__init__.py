"""
STRUCTURAL
==========

checks two "json-like" values have same "structure" or not,
where "json-like" values mean tree-formed value with dict and list.

USAGE
------

A code like below checks "structural" equality (or match) between a and b.

   Structure.of(a) == Structure.of(b)

Or, umatch with

    Structure.of(a) != Structure.of(b)

### non-container values (primitive)

For now, this library focusing to JSON,
non-list and non-dict values are "Primitive", or not investigated.

*NOTE* : `collections.abc.Mapping` or `collections.abc.Sequence` are not supported, now.

They matches when they are same type value.

>>> Structure.of(2) == Structure.of(3)
True

>>> Structure.of(2.0) != Structure.of(2)
True

because, int is not float.

>>> Structure.of(2) != Structure.of('2')
True

because, int is not str.

### LIST

Lists match each other when

- length of 2 lists are same.
- each element matches to another, index-by-index.

e.g.

>>> Structure.of([1, 2, 3]) == Structure.of([4, 5, 6])
True

Match. same langth, elements are same type each other.

>>> Structure.of([1, 2, 3]) == Structure.of([4, 5])
False

Not match. lengthes are different.

>>> Structure.of([1, 2, 3]) == Structure.of([1, "2", 3])
False

Not match. Type of elements are different (at index 1).

### DICT

As like as list, 2 dicts matches when

- they have same key
- each value mathes to another, key-by-key

e.g.

>>> Structure.of({'a': 12, 'b': ['a', 'b']}) == Structure.of({'a': 0, 'b': ['cd', 'df']})
True

>>> Structure.of({'a': 12, 'b': ['a', 'b']}) != Structure.of({'b': ['cd', 'df']})
True

because keys do not match.

>>> Structure.of({'a': 12, 'b': ['a', 'b']}) != Structure.of({'a': 0, 'b': ['cd', 'df', 'fg']})
True

beacuse, there are unmatch in the key 'b'.
(Now, you know, checking works recursively)
"""


class Structure(object):
    def __new__(cls, other):
        if isinstance(other, Structure):
            return other
        return super().__new__(cls)

    def __init__(self, value, structure):
        self.value = value
        self.structure = structure

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        other = Structure.of(other)
        return self.structure == other.structure

    @classmethod
    def of(cls, value):
        if isinstance(value, Structure):
            return value
        if isinstance(value, dict):
            return DictStructure(value)
        elif isinstance(value, list):
            return ListStructure(value)
        else:
            return Primitive(value)


class Primitive(Structure):
    """non-container value.
    this matches with a same-typed value.
    """
    def __init__(self, value):
        super().__init__(value, type(value))

class DictStructure(Structure):
    """structure of dictionaly.
    this matches with another dict which has same structued value for each keys.
    """
    def __init__(self, value):
        if not isinstance(value, dict):
            raise ValueError(
                'DictStructure requires dict object (but {})'
                .format(value)
            )
        structure = {k: Structure.of(v) for k, v in value.items()}
        super().__init__(value, structure)
        
    def keys(self):
        return self.structure.keys()

    def __getitem__(self, key):
        return self.structure[key]


class ListStructure(Structure):
    """structure of list.
    this matches with another list which has same structued value for each indice.
    """
    def __init__(self, value):
        if not isinstance(value, list):
            raise ValueError(
                'ListStructure requires list value (But {})'
                .format(value)
            )
        value = value
        structure = [Structure.of(i) for i in value]
        super().__init__(value, structure)

    def __getitem__(self, idx):
        return self.structure[idx]

    def __len__(self, idx):
        return len(self.structure)

    def __iter__(self):
        return iter(self.structure)
