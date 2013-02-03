# Python Specifications
[![Build Status](https://secure.travis-ci.org/dalanhurst/python-specifications.png)](http://travis-ci.org/dalanhurst/python-specifications)

An implementation of ["Specifications" by Eric Evans and Martin Fowler](http://www.martinfowler.com/apsupp/spec.pdf) in Python.

    "The central idea of Specification is to separate the statement of how to
    match a candidate, from the candidate object that it is matched against. As
    well as its usefulness in selection, it is also valuable for validation and
    for building to order." -- "Specifications", Eric Evans and Martin Fowler

## Satisfaction
One of the most useful things a specification can do is determine if a given
candidate satisfies a list of requirements defined in the specification. For
example:

    ```python
    from specs.specs import Composite

    class Person(object):
        def __init__(self):
            self.changes_form_by_light_of_the_full_moon = False

    class Werewolf(Person):
        def __init__(self):
            super(Werewolf, self).__init__()
            self.changes_form_by_light_of_the_full_moon = True

    class IsHuman(Composite):
        def is_satisfied_by(self, candidate):
            return isinstance(candidate, Person)

    class FormAffectedByFullMoon(Composite):
        def is_satisfied_by(self, candidate):
            return candidate.changes_form_by_light_of_the_full_moon

    spec = IsHuman() & FormAffectedByFullMoon()

    assert spec.is_satisfied_by(Person()) == False
    assert spec.is_satisfied_by(Werewolf()) == True
    ```

Checkout tests/vampire_test.py for a more involved example of Satisfaction.

## Subsumption
It is also useful to compare one specification to another.

    "Specification B is a special case of Specification A if and only if for any
    possible candidate object X, where A is satisfied by X, B will always be
    satisfied by X also. If this is true, it is possible to apply any conclusion
    reached using B to A, hence B can subsume A."

However, subsumption on a composite specification appears to be NP-hard. See
[Boolean satisfiability problem](http://en.wikipedia.org/wiki/Boolean_satisfiability_problem)
and [this StackOverflow question](http://stackoverflow.com/questions/13713664/extending-linq-based-specification-pattern-to-implement-subsumption)
for more.
