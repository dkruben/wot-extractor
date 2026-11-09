# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/graphics_settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/graphics_settings.py
from __future__ import absolute_import
from debug_utils import LOG_DEBUG
from gui.shared.utils import graphics
from web.web_client_api import w2c, W2CSchema

class GraphicsSettingsWebApiMixin(object):

    @w2c(W2CSchema, 'graphics_settings')
    def graphicsSettings(self, cmd):
        settings = {}
        settingNames = ('TEXTURE_QUALITY', 'LIGHTING_QUALITY', 'SHADOWS_QUALITY', 'SNIPER_MODE_GRASS_ENABLED',
                        'EFFECTS_QUALITY', 'SNIPER_MODE_EFFECTS_QUALITY', 'FLORA_QUALITY',
                        'POST_PROCESSING_QUALITY', 'VEHICLE_DUST_ENABLED', 'CUSTOM_AA_MODE',
                        'MSAA_QUALITY', 'RENDER_PIPELINE')
        for settingName in settingNames:
            setting = graphics.getGraphicsSetting(settingName)
            if setting is not None:
                settings[settingName] = setting.value
            else:
                LOG_DEBUG('Settings "%s" not found!' % settingName)

        return {'request_id': 'graphics_settings', 'settings': settings}
