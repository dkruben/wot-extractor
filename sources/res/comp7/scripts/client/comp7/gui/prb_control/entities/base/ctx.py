# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/base/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/prb_control/entities/base/ctx.py
from __future__ import absolute_import
from gui.prb_control.entities.base.ctx import PrbAction
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getSquadSize', 'squadSize'))
class Comp7PrbAction(PrbAction):

    def __init__(self, actionName, squadSize, mmData=0, accountsToInvite=None):
        super(Comp7PrbAction, self).__init__(actionName, mmData, accountsToInvite)
        self.__squadSize = squadSize

    def getSquadSize(self):
        return self.__squadSize
