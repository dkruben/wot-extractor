# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/login/SocialLoginView.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/SocialLoginView.py
from __future__ import absolute_import
import BigWorld
from gui.login.social_networks import SOCIAL_NETWORKS
from gui.Scaleform.daapi.view.login.LoginView import LoginView
from gui.Scaleform.daapi.view.login.login_modes.social_mode import SOCIAL_NETWORK_TO_DOMAIN_MAPPING

class SocialLoginView(LoginView):

    def onRegister(self, host):
        self._loginMode.doSocialLogin(SOCIAL_NETWORKS.WGNI, host, True)

    def onLoginBySocial(self, socialNetworkName, serverName):
        self._loginMode.doSocialLogin(socialNetworkName, serverName, False)

    def onTextLinkClick(self, socialNetworkName):
        if socialNetworkName in SOCIAL_NETWORK_TO_DOMAIN_MAPPING:
            BigWorld.wg_openWebBrowser(SOCIAL_NETWORK_TO_DOMAIN_MAPPING[socialNetworkName])
            return
        super(SocialLoginView, self).onTextLinkClick(socialNetworkName)
