# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileGlobalMapPromoView.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileGlobalMapPromoView.py
from __future__ import absolute_import
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import text_styles
from gui.shared.events import OpenLinkEvent
from gui.Scaleform.daapi.view.meta.ClanProfileGlobalMapPromoViewMeta import ClanProfileGlobalMapPromoViewMeta

class ClanProfileGlobalMapPromoView(ClanProfileGlobalMapPromoViewMeta):

    def showInfo(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_PROMO))

    def showMap(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_CAP))

    def _populate(self):
        super(ClanProfileGlobalMapPromoView, self)._populate()
        self.as_setDataS({'header': (text_styles.promoSubTitle(_ms(CLANS.GLOBALMAPVIEW_PROMO_HEADER))), 
           'description': (text_styles.main(_ms(CLANS.GLOBALMAPVIEW_PROMO_DESCRIPTION))), 
           'infoLinkLabel': (_ms(CLANS.GLOBALMAPVIEW_PROMO_INFOLINK)), 
           'mapLinkLabel': (_ms(CLANS.GLOBALMAPVIEW_PROMO_MAPLINK)), 
           'background': (RES_ICONS.MAPS_ICONS_CLANS_GLOBAL_MAP_PROMO)})
