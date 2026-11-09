# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_state_machine/actions_base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_state_machine/actions_base.py
from __future__ import absolute_import
import abc, logging, CGF
from py2to3.patched_future import with_metaclass

class ActionBase(with_metaclass(abc.ABCMeta, object)):
    _DEV_ONLY = False
    _logger = logging.getLogger('CGFStateMachine')

    @classmethod
    def isDevOnly(cls):
        return cls._DEV_ONLY

    @classmethod
    def actionTypeName(cls):
        return cls.__name__

    @classmethod
    def actionDisplayName(cls):
        return cls.__name__

    @abc.abstractmethod
    def execute(self, gameObject):
        raise NotImplementedError
