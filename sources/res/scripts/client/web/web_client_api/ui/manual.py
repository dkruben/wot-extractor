# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/manual.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/manual.py
from __future__ import absolute_import
from gui.doc_loaders.manual_xml_data_reader import getPagesIndexesList
from helpers import dependency
from skeletons.gui.game_control import IManualController
from web.web_client_api import W2CSchema, w2c, Field

def _chapterIndexValidator(key, _):
    manualController = dependency.instance(IManualController)
    return key in getPagesIndexesList(manualController.pageFilter)


class _OpenManualWindowSchema(W2CSchema):
    ignore_chapter = Field(type=bool, default=False)
    chapter_index = Field(required=False, type=int, default=1, validator=_chapterIndexValidator)


class ManualPageWebApiMixin(object):
    manualController = dependency.descriptor(IManualController)

    @w2c(_OpenManualWindowSchema, 'manual')
    def openManualPage(self, cmd):
        if self.manualController.isActivated():
            self.manualController.show(None if cmd.ignore_chapter else cmd.chapter_index)
        return
