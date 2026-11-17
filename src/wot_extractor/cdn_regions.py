"""CDN targets only: intentionally separate from local-install detection support."""
import json
from pathlib import Path

CATALOG_PATH = Path(__file__).with_name('data') / 'wg_realms.json'
CDN_REGIONS = json.loads(CATALOG_PATH.read_text(encoding='utf-8'))


def require_region(realm):
    if realm not in CDN_REGIONS:
        raise ValueError('Unsupported CDN region: {}. Allowed: {}. RU/LESTA are excluded.'.format(
            realm, ', '.join(CDN_REGIONS)))
    return CDN_REGIONS[realm]


def matrix(selection):
    requested = list(CDN_REGIONS) if selection.strip().upper() == 'ALL' else [
        item.strip().upper() for item in selection.split(',')]
    if not requested or any(not item for item in requested):
        raise ValueError('Specify ALL or a comma-separated list of CDN regions')
    result = []
    for realm in dict.fromkeys(requested):
        target = require_region(realm)
        result.append(dict(realm=realm, **target))
    return {'include': result}
