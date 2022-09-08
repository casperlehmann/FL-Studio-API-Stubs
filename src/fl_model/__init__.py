"""
Provides a model of FL Studio, which integrates with the other stub files in
order to facilitate testing of MIDI scripts.

NOTE: This module is not included in FL Studio's runtime, and should not be
imported from within your main script. It is intended to be used within a
testing framework in order to help validate the behavior of MIDI scripts.
"""

__all__ = [
    'getState',
    'setState',
    'resetState',
    'FlContext',
    'config',
    'deprecate',
]

from .configuration import config
from .decorators import deprecate

from .state import (
    getState,
    setState,
    resetState,
    FlContext,
)
