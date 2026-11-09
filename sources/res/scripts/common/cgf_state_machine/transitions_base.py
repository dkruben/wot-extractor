# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_state_machine/transitions_base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_state_machine/transitions_base.py
from __future__ import absolute_import
import abc, logging
from py2to3.patched_future import with_metaclass

class TransitionBase(with_metaclass(abc.ABCMeta, object)):
    _DEV_ONLY = False
    _logger = logging.getLogger('CGFStateMachine')

    @classmethod
    def isDevOnly(cls):
        return cls._DEV_ONLY

    @classmethod
    def transitionTypeName(cls):
        return cls.__name__

    @classmethod
    def transitionDisplayName(cls):
        return cls.__name__

    def activate(self, gameObject):
        pass

    def deactivate(self):
        pass

    @abc.abstractmethod
    def update(self):
        return False
