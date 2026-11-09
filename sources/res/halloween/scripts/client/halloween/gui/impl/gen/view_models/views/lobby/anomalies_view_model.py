# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/anomalies_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/anomalies_view_model.py
from frameworks.wulf import ViewModel
from halloween.gui.impl.gen.view_models.views.common.anomalies_matrix.anomalies_matrix_model import AnomaliesMatrixModel

class AnomaliesViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=2, commands=1):
        super(AnomaliesViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def matrix(self):
        return self._getViewModel(0)

    @staticmethod
    def getMatrixType():
        return AnomaliesMatrixModel

    def getSkinId(self):
        return self._getNumber(1)

    def setSkinId(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(AnomaliesViewModel, self)._initialize()
        self._addViewModelProperty('matrix', AnomaliesMatrixModel())
        self._addNumberProperty('skinId', 0)
        self.onClose = self._addCommand('onClose')
