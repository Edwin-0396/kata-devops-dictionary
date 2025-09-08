import pytest
from dictionary import Dictionary

def test_add_and_lookup_word():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    assert d.look("Apple") == "A fruit that grows on trees"

def test_lookup_missing_word():
    d = Dictionary()
    assert d.look("Banana") == "Can't find entry for Banana"

def test_update_existing_word():
    d = Dictionary()
    d.newentry("Apple", "Updated definition")
    assert d.look("Apple") == "Updated definition"
