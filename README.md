STRUCTURAL
==========

checks two "json-like" values have same "structure" or not

USAGE
------

A code like below checks "structural" equality (or match) between a and b.

```
Structure.of(a) == Structure.of(b)
```

Or, umatch with

```
Structure.of(a) != Structure.of(b)
```

### non-container values (primitive)

For now, this library focusing to JSON,
non-list and non-dict values are "Primitive", or not investigated.

*NOTE* : `collections.abc.Mapping` or `collections.abc.Sequence` are not supported, now.

They matches when they are same type value.

```py
assert Structure.of(2) == Structure.of(3)

assert Structure.of(2.0) != Structure.of(2) # because, int is not float.

assert Structure.of(2) != Structure.of('2') # because, int is not str.
```

### LIST

Lists match each other when

- length of 2 lists are same.
- each element matches to another, index-by-index.

e.g.

```py
assert Structure.of([1, 2, 3]) == Structure.of([4, 5, 6])
# Match. same langth, elements are same type each other.

assert Structure.of([1, 2, 3]) != Structure.of([4, 5])
# Not match. lengthes are different.

assert Structure.of([1, 2, 3]) != Structure.of([1, "2", 3])
# Not match. Type of elements are different (at index 1).
```

### DICT

As like as list, 2 dicts matches when

- they have same key
- each value mathes to another, key-by-key

e.g.

```py
assert Structure.of({'a': 12, 'b': ['a', 'b']}) == Structure.of({'a': 0, 'b': ['cd', 'df']})

assert Structure.of({'a': 12, 'b': ['a', 'b']}) != Structure.of({'b': ['cd', 'df']})
# because keys do not match.

Structure.of({'a': 12, 'b': ['a', 'b']}) != Structure.of({'a': 0, 'b': ['cd', 'df', 'fg']})
# because, there are unmatch in the key 'b'.
```

(Now, you know, checking works recursively)
