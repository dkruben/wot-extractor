# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pathes_config/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pathes_config/__init__.py
from __future__ import absolute_import
import os, sys, site
from soft_exception import SoftException

def setupPaths():
    root = '../../../../..'

    def expandPath(item):
        if not os.path.isabs(item):
            if item[0] == '~':
                item = os.path.expanduser(item)
            else:
                item = os.path.join(os.path.split(os.path.abspath(__file__))[0], item)
        return os.path.normpath(item)

    try:
        from pycommon import platform_info
    except:
        raise SoftException('pycommon.platform_info is unavailable - cannot determine platform')

    platformSuffix = platform_info.getPlatformSuffix()
    noarchSuffix = platform_info.getNoarchSuffix()
    if not platformSuffix or not noarchSuffix:
        raise SoftException('Unable to determine platform suffix')
    addPath = [
     root + '/tools/bigworld/server',
     root + '/res/bigworld/scripts/common',
     root + '/res/bigworld/scripts/common/Lib',
     root + '/res/bigworld/scripts/common/site-packages',
     root + '/res/bigworld/scripts/server_common',
     root + '/res/bigworld/scripts/server_common/lib-dynload-' + platformSuffix,
     root + '/res/wot/scripts',
     root + '/res/wot/scripts/base',
     root + '/res/wot/scripts/base/account_helpers',
     root + '/res/wot/scripts/server_common',
     root + '/res/wot/scripts/server_common/virtual_machine',
     root + '/res/wot/scripts/server_common/site-packages/' + platformSuffix,
     root + '/res/wot/scripts/server_common/site-packages/' + noarchSuffix,
     root + '/res/wot/scripts/common',
     root + '/res/wot/scripts/development/libs',
     root + '/tools/wot/server/bw_lib/bigworld/fake']
    for path in addPath:
        norm_path = expandPath(path)
        if 'site-packages' in norm_path:
            site.addsitedir(norm_path)
        else:
            sys.path.append(norm_path)

    bw_xml = expandPath(root + '/res/wot/server/bw.xml')
    if not os.path.exists(bw_xml):
        from shutil import copyfile
        copyfile(expandPath(root + '/res/wot/server/bw.xml.dist'), bw_xml)
