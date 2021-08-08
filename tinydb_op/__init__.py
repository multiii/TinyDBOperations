"""
Contains a Additional Set of TinyDB Operations
"""


def add(*fields, n):
    """
    Add ``n`` to the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc += n

    return transform


def subtract(*fields, n):
    """
    Subtract ``n`` from the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc -= n

    return transform


def multiply(*fields, n):
    """
    Multiply ``n`` to the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc *= n

    return transform


def divide(*fields, n):
    """
    Divide ``n`` from the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc /= n

    return transform


def modulo(*fields, n):
    """
    Return modulo of ``n`` from the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc /= n

    return transform


def exponent(*fields, n):
    """
    Return exponent of ``n`` to the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc **= n

    return transform


def append(*fields, n):
    """
    Append ``n`` to the Iterable in the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc.append(n)

    return transform


def remove(*fields, n):
    """
    Remove ``n`` from the Iterable in the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc.remove(n)

    return transform


def pop(*fields, n=None):
    """
    Pop ``n`` from the Iterable in the given fields in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        if n is None:
            doc.pop()
        else:
            doc.pop(n)

    return transform


def set(*fields, n):
    """
    Set given fields to ``n`` in the document.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc = n

    return transform


def increment(*fields):
    """
    Increment the given fields in the document by 1.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc += 1

    return transform


def decrement(*fields):
    """
    Decrement the given fields in the document by 1.
    """
    def transform(doc):
        for field in fields:
            doc = doc[field]
        doc -= 1

    return transform
