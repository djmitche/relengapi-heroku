# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

SQLALCHEMY_DATABASE_URIS = {
   'relengapi': os.environ['CLEARDB_DATABASE_URL'],
}

# ===== Authentication and Authorization =====

RELENGAPI_AUTHENTICATION = {
    'type': 'browserid',
}

RELENGAPI_PERMISSIONS = {
    'type': 'static',
    'permissions': {
        'dustin@mozilla.com': [
            'base.tokens.prm.view',
            'base.tokens.prm.issue',
            'base.tokens.prm.revoke',
            'base.tokens.tmp.issue',
            'base.tokens.usr.view.all',
            'base.tokens.usr.issue',
            'base.tokens.usr.revoke.all',
            'base.badpenny.view',
        ],
    },
}

DEBUG=True

SESSION_COOKIE_NAME='relengapi_ses'
SECRET_KEY=os.environ['SECRET_KEY']

# allow flask to generate correct URLs (e.g., for Persona)
PREFERRED_URL_SCHEME='https'
