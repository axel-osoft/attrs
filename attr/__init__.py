from __future__ import absolute_import, division, print_function

from ._funcs import (
    asdict,
    assoc,
    has,
)
from ._make import (
    Attribute,
    Factory,
    NOTHING,
    attr,
    attributes,
    fields,
    make_class,
    validate,
)
from ._config import (
    get_run_validators,
    set_run_validators,
)
from . import validators

__version__ = "15.0.0.dev1"
__author__ = "Hynek Schlawack"
__license__ = "MIT"
__copyright__ = "Copyright 2015 Hynek Schlawack"


s = attributes
attr = ib = attr

__all__ = [
    "Attribute",
    "Factory",
    "NOTHING",
    "asdict",
    "assoc",
    "attr",
    "attributes",
    "fields",
    "get_run_validators",
    "has",
    "ib",
    "make_class",
    "s",
    "set_run_validators",
    "validate",
    "validators",
]