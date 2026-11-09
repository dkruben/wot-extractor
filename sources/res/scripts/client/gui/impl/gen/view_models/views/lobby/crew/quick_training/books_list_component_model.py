# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/quick_training/books_list_component_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/quick_training/books_list_component_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.training_book_model import TrainingBookModel

class BooksListComponentModel(ComponentBaseModel):
    __slots__ = ('buy', 'select', 'mouseEnter', 'openPostProgression')

    def __init__(self, properties=2, commands=4):
        super(BooksListComponentModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return TrainingBookModel

    def _initialize(self):
        super(BooksListComponentModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self.buy = self._addCommand('buy')
        self.select = self._addCommand('select')
        self.mouseEnter = self._addCommand('mouseEnter')
        self.openPostProgression = self._addCommand('openPostProgression')
