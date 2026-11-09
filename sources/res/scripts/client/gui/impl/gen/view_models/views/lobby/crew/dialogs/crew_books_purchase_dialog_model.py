# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/crew_books_purchase_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/crew_books_purchase_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel

class CrewBooksPurchaseDialogModel(DialogTemplateViewModel):
    __slots__ = ('onStepperChanged', )

    def __init__(self, properties=10, commands=3):
        super(CrewBooksPurchaseDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def bookPrice(self):
        return self._getViewModel(6)

    @staticmethod
    def getBookPriceType():
        return CurrencyViewModel

    def getBookName(self):
        return self._getString(7)

    def setBookName(self, value):
        self._setString(7, value)

    def getIsBookPersonal(self):
        return self._getBool(8)

    def setIsBookPersonal(self, value):
        self._setBool(8, value)

    def getExperience(self):
        return self._getNumber(9)

    def setExperience(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(CrewBooksPurchaseDialogModel, self)._initialize()
        self._addViewModelProperty('bookPrice', CurrencyViewModel())
        self._addStringProperty('bookName', '')
        self._addBoolProperty('isBookPersonal', False)
        self._addNumberProperty('experience', 0)
        self.onStepperChanged = self._addCommand('onStepperChanged')
