# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/container_views/example_view_skeleton/context.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/container_views/example_view_skeleton/context.py
from gui.impl.lobby.container_views.base.context import TankmanContext

class ExampleViewContext(TankmanContext):
    __slots__ = ('_exampleField', )

    def __init__(self, tankmanID):
        self._exampleField = None
        super(ExampleViewContext, self).__init__(tankmanID)
        return

    @property
    def exampleField(self):
        return self._exampleField

    def update(self, tankmanID):
        super(ExampleViewContext, self).update(tankmanID)
        self._exampleField = self._getExampleField()

    def _getExampleField(self):
        return 'some value'
