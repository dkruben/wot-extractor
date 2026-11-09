# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/FlagModel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/FlagModel.py
from __future__ import absolute_import
from collections import namedtuple
from Math import Matrix
import BigWorld, AnimationSequence
FlagSettings = namedtuple('FlagSettings', ['flagCompounModel', 'flagAlias', 
 'flagAnim', 'flagBackgroundTex', 'flagEmblemTex', 
 'flagEmblemTexCoords', 
 'spaceID'])

class FlagModel(object):
    model = property((lambda self: self.__flagCompoundModel))

    def __init__(self):
        self.__flagCompoundModel = None
        self.__flagStaffFashion = None
        self.__flagFashion = None
        self.__flagAnimator = None
        self.__spaceID = None
        return

    def setupFlag(self, position, flagSettings, color):
        self.__spaceID = flagSettings.spaceID
        self.__flagCompoundModel = flagSettings.flagCompounModel
        self.__flagCompoundModel.position = position
        self.__flagStaffFashion = BigWorld.WGAlphaFadeCompoundFashion()
        self.__flagFashion = BigWorld.WGFlagAlphaFadeFashion()
        self.__flagFashion.setColor(color)
        self.__flagFashion.setFlagBackgroundTexture(flagSettings.flagBackgroundTex)
        self.__flagFashion.setEmblemTexture(flagSettings.flagEmblemTex, flagSettings.flagEmblemTexCoords)
        translationMatrix = Matrix()
        translationMatrix.setTranslate(position)
        self.__flagFashion.overridePosition(translationMatrix)
        self.__flagCompoundModel.setupFashions((self.__flagStaffFashion, self.__flagFashion))
        self.__flagAnimator = flagSettings.flagAnim
        if self.__flagAnimator is not None:
            self.__flagAnimator.bindTo(AnimationSequence.PartWrapperContainer(self.__flagCompoundModel, self.__spaceID, flagSettings.flagAlias))
        return

    def changeFlagColor(self, color):
        if self.__flagFashion:
            self.__flagFashion.setColor(color)

    def startFlagAnimation(self):
        if self.__flagAnimator:
            self.__flagAnimator.start()
