# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/mapbox/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/mapbox/__init__.py
from __future__ import absolute_import
from past.builtins import basestring
from helpers import dependency
from skeletons.gui.game_control import IMapboxController
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _SurveyCompletedSchema(W2CSchema):
    name = Field(required=True, type=basestring)


@w2capi(name='mapbox', key='action')
class MapboxWebApi(W2CSchema):
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    @w2c(_SurveyCompletedSchema, name='survey_complete')
    def handleSurveyCompleted(self, cmd):
        self.__mapboxCtrl.handleSurveyCompleted(cmd.name)
