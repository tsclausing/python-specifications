"""
Base classes supporting specification

    "The central idea of Specification is to separate the statement of how to
    match a candidate, from the candidate object that it is matched against. As
    well as its usefulness in selection, it is also valuable for validation and
    for building to order." -- "Specifications", Eric Evans and Martin Fowler
"""


class Satisfaction(object):
    def is_satisfied_by(self, candidate):
        raise NotImplementedError()


class Composite(Satisfaction):
    """Base class for the specification"""

    def conjoin(self, other):
        """
        Conjunction factory

        Usage::
            >>> from specs.specs import Composite, Conjunction
            >>> s = Composite().conjoin(Composite())
            >>> assert isinstance(s, Conjunction)
            >>> s = Composite().and_(Composite())
            >>> assert isinstance(s, Conjunction)
            >>> s = Composite() & Composite()
            >>> assert isinstance(s, Conjunction)
        """
        return Conjunction(self, other)

    def and_(self, other):
        """Short-hand conjunction"""
        return self.conjoin(other)

    def __and__(self, other):
        """Bitwise subversion: conjunction"""
        return self.conjoin(other)

    def disjoin(self, other):
        """
        Disjunction factory

        Usage::
            >>> from specs.specs import Composite, Disjunction
            >>> s = Composite().disjoin(Composite())
            >>> assert isinstance(s, Disjunction)
            >>> s = Composite().or_(Composite())
            >>> assert isinstance(s, Disjunction)
            >>> s = Composite() | Composite()
            >>> assert isinstance(s, Disjunction)
        """
        return Disjunction(self, other)

    def or_(self, other):
        """Short-hand disjunction"""
        return self.disjoin(other)

    def __or__(self, other):
        """Bitwise subversion: disjunction"""
        return self.disjoin(other)

    def negate(self):
        """
        Negation factory

        Usage::
            >>> from specs.specs import Composite, Negation
            >>> s = Composite().negate()
            >>> assert isinstance(s, Negation)
            >>> s = Composite().not_()
            >>> assert isinstance(s, Negation)
            >>> s = ~ Composite()
            >>> assert isinstance(s, Negation)
        """
        return Negation(self)

    def not_(self):
        """Short-hand negation"""
        return self.negate()

    def __invert__(self):
        """Bitwise subversion: negation"""
        return self.negate()


class Conjunction(Composite):
    """Represents a logical conjunction (AND)"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_satisfied_by(self, candidate):
        return bool(
            self.left.is_satisfied_by(candidate)
            and self.right.is_satisfied_by(candidate))


class Disjunction(Composite):
    """Represents a logical disjunction (OR)"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_satisfied_by(self, candidate):
        return bool(
            self.left.is_satisfied_by(candidate)
            or self.right.is_satisfied_by(candidate))


class Negation(Composite):
    """Represents a logical negation (NOT)"""

    def __init__(self, spec):
        self.spec = spec

    def is_satisfied_by(self, candidate):
        return not self.spec.is_satisfied_by(candidate)
