# pyramda [![Build Status](https://travis-ci.org/jackfirth/pyramda.svg?branch=master)](https://travis-ci.org/jackfirth/pyramda)
Python package supporting heavy functional programming through currying and function composition. Translation of the Ramda library from javascript to python. Currently only Python 3 is supported.

```python
>>> from pyramda import map, inc
>>> inc(1)
2
>>> map(inc, [1, 2, 3]
[2, 3, 4]
>>> incEach = map(inc)
>>> incEach([1, 2, 3])
[2, 3, 4]
```

### Provided functions

Type Synonyms

```
Predicate a = a -> Boolean
Relation a = a -> a -> Boolean
Operation a = a -> a -> a
```

Function

```
apply :: (a -> ... -> z) -> (a, ...) -> z
compose :: (y -> z) ... (a -> b) -> a -> z
curry :: (a b ... -> z) -> a -> b -> ... -> z
```

Iterable

```
all_satisfy :: Predicate a -> Predicate [a]
any_satisfy :: Predicate a -> Predicate [a]
chain :: (a -> [b]) -> [a] -> [b]
concat :: Operation [a]
cons :: a -> [a] -> [a]
contains :: a -> Predicate [a]
contains_with :: Relation a -> a -> Predicate [a]
drop :: Number -> [a] -> [a]
filter :: Predicate a -> [a] -> [a]
map :: (a -> b) -> [a] -> [b]
reduce :: (a -> b -> b) -> a -> [b] -> a
take :: Number -> [a] -> [a]
```

Math

```
add :: Operation Number
dec :: Number -> Number
divide :: Operation Number
inc :: Number -> Number
mean :: [Number] -> Number
modulo :: Operation Number
multiply :: Operation Number
negate :: Number -> Number
product :: [Number] -> Number
subtract :: Operation Number
sum :: [Number] -> Number
```

Other

```
equal :: a -> b -> Boolean
getattr :: attr : String -> Object { attr :: a | * } -> a
getitem :: key : k -> Collection { key :: v | * } -> v
isinstance :: Class -> Predicate a
```
