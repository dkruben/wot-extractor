# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/ingame_help/detailed_help_pages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/ingame_help/detailed_help_pages.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl import backport
from gui.ingame_help.detailed_help_pages import DetailedHelpPagesBuilder, addPage
from gui.shared.formatters import text_styles
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Union, List, Any
    from frameworks.wulf import PyResAccessor

class Comp7CorePagesBuilder(DetailedHelpPagesBuilder):
    _PAGE_NAMES = ('seasonModifiers', 'poi', 'roleSkills', 'rules')
    _CORE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7Core
    _CORE_RES_ROOT_IMAGES = R.images.comp7_core.gui.maps.icons.battleHelp
    _MODE_RES_ROOT_TEXTS = None
    _MODE_RES_ROOT_IMAGES = None

    @classmethod
    def priority(cls):
        raise NotImplementedError

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        for pageName in cls._PAGE_NAMES:
            addPage(datailedList=pages, headerTitle=cls._getHeader(pageName), title=cls._getTitle(pageName), descr=cls._getDescr(pageName), keys=[], image=cls._getImage(pageName))

        return pages

    @classmethod
    def _getPageResBranchTexts(cls, pageName):
        corePageAccess = cls._CORE_RES_ROOT_TEXTS.dyn(pageName)
        if corePageAccess.isValid():
            return corePageAccess
        return cls._MODE_RES_ROOT_TEXTS.dyn(pageName)

    @classmethod
    def _getPageResBranchImages(cls, pageName):
        corePageAccess = cls._CORE_RES_ROOT_IMAGES.dyn(pageName)
        if corePageAccess.isValid():
            return corePageAccess
        return cls._MODE_RES_ROOT_IMAGES.dyn(pageName)

    @classmethod
    def _getHeader(cls, pageName):
        return backport.text(cls._MODE_RES_ROOT_TEXTS.mainTitle())

    @classmethod
    def _getTitle(cls, pageName):
        return backport.text(cls._getPageResBranchTexts(pageName).title())

    @classmethod
    def _getDescr(cls, pageName):
        return text_styles.mainBig(backport.text(cls._getPageResBranchTexts(pageName)()))

    @classmethod
    def _getImage(cls, pageName):
        return backport.image(cls._getPageResBranchImages(pageName)())
