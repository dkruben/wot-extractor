# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/resources/models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/models.py
from typing import Optional, Union, TYPE_CHECKING
from gui.game_loading.resources.consts import InfoStyles
if TYPE_CHECKING:
    from gui.game_loading.resources.consts import ImageVfxs

class BaseResourceModel(object):
    __slots__ = ('minShowTimeSec', )

    def __init__(self, minShowTimeSec):
        self.minShowTimeSec = max(minShowTimeSec, 0)


class LocalImageModel(BaseResourceModel):
    __slots__ = ('imageRelativePath', 'vfx', 'localizationText', 'descriptionText',
                 'transition', 'imageAbsolutePath')

    def __init__(self, imageRelativePath, vfx=None, localizationText=None, descriptionText=None, minShowTimeSec=0, transition=0, imageAbsolutePath=None):
        super(LocalImageModel, self).__init__(minShowTimeSec=minShowTimeSec)
        self.imageRelativePath = imageRelativePath
        self.vfx = vfx
        self.localizationText = localizationText
        self.descriptionText = descriptionText
        self.transition = transition
        self.imageAbsolutePath = imageAbsolutePath

    def __repr__(self):
        string = '<{}(image={}, vfx={}, localizationExist={}, descriptionExist={}, minShowTimeSec={}, transition={})>'
        return string.format(self.__class__.__name__, self.imageRelativePath, self.vfx, bool(self.localizationText), bool(self.descriptionText), self.minShowTimeSec, self.transition)


class LogoModel(BaseResourceModel):
    __slots__ = ('type', 'showCopyright', 'showVersion', 'transition', 'info', 'infoStyle')

    def __init__(self, logoType, minShowTimeSec=0, showCopyright=True, showVersion=True, transition=0, info='', infoStyle=InfoStyles.DEFAULT):
        super(LogoModel, self).__init__(minShowTimeSec=minShowTimeSec)
        self.type = logoType
        self.showCopyright = showCopyright
        self.showVersion = showVersion
        self.transition = transition
        self.info = info
        self.infoStyle = infoStyle

    def __repr__(self):
        return ('<LogoModel(type={}, minShowTimeSec={}, copyright={}, version={}, transition={}, info={}, infoStyle={})>').format(self.type, self.minShowTimeSec, self.showCopyright, self.showVersion, self.transition, self.info, self.infoStyle)


class StatusTextModel(BaseResourceModel):
    __slots__ = ('text', )

    def __init__(self, text, minShowTimeSec=0):
        super(StatusTextModel, self).__init__(minShowTimeSec=minShowTimeSec)
        self.text = text

    def __repr__(self):
        return ('<StatusTextModel(text={}, minShowTimeSec={})>').format(self.text, self.minShowTimeSec)
