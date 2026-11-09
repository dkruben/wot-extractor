# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/factories/composite.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/factories/composite.py
from debug_utils import LOG_ERROR
from gui.prb_control.factories.ControlFactory import ControlFactory
from gui.prb_control.factories.PreQueueFactory import PreQueueFactory
from gui.prb_control.factories.LegacyFactory import LegacyFactory
from gui.prb_control.factories.UnitFactory import UnitFactory
from gui.prb_control.settings import CTRL_ENTITY_TYPE, FUNCTIONAL_FLAG
from soft_exception import SoftException
_ORDER_TO_CREATE = (
 CTRL_ENTITY_TYPE.LEGACY,
 CTRL_ENTITY_TYPE.UNIT,
 CTRL_ENTITY_TYPE.PREQUEUE)

class ControlFactoryComposite(ControlFactory):

    def __init__(self):
        self.__factories = {(CTRL_ENTITY_TYPE.LEGACY): (LegacyFactory()), 
           (CTRL_ENTITY_TYPE.UNIT): (UnitFactory()), 
           (CTRL_ENTITY_TYPE.PREQUEUE): (PreQueueFactory())}

    def clear(self):
        self.__factories.clear()

    def get(self, ctrlType):
        if ctrlType in self.__factories:
            return self.__factories[ctrlType]
        else:
            return

    def createEntry(self, ctx):
        ctrlType = ctx.getCtrlType()
        if ctrlType in self.__factories:
            return self.__factories[ctrlType].createEntry(ctx)
        else:
            LOG_ERROR('Entry factory is not found', ctx)
            return

    def createEntryByAction(self, action):
        for ctrlType in _ORDER_TO_CREATE:
            result = self.__factories[ctrlType].createEntryByAction(action)
            if result is not None:
                return result

        return

    def createEntity(self, ctx):
        for ctrlType in _ORDER_TO_CREATE:
            result = self.__factories[ctrlType].createEntity(ctx)
            if result is not None:
                return result

        return

    def createLeaveCtx(self, flags=FUNCTIONAL_FLAG.UNDEFINED, entityType=0):
        raise SoftException('This method should not be reached in this context')

    def createStateEntity(self, entity):
        raise SoftException('This method should not be reached in this context')
