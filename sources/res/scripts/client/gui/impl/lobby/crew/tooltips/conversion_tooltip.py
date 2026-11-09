# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/conversion_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/conversion_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.conversion_tooltip_book_model import ConversionTooltipBookModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.conversion_tooltip_model import ConversionTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class ConversionTooltip(ViewImpl):
    _itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = ('__books', '__title', '__description')

    def __init__(self, books, **kwargs):
        settings = ViewSettings(R.views.lobby.crew.tooltips.ConversionTooltip())
        settings.model = ConversionTooltipModel()
        self.__books = books
        self.__title = kwargs.get('title')
        self.__description = kwargs.get('description')
        super(ConversionTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ConversionTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ConversionTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setTitle(self.__title)
            vm.setDescription(self.__description)
            booksList = vm.getBooksList()
            booksList.clear()
            for book, value in self.__books:
                tbm = ConversionTooltipBookModel()
                tbm.setIcon(book.getBonusIconName())
                tbm.setTitle(backport.text(R.strings.crew_books.c_items.dyn(book.getBookType()).noNationName()))
                tbm.setNation(backport.text(R.strings.nations.dyn(book.getNation())()))
                tbm.setValue(value)
                booksList.addViewModel(tbm)
