# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

SQLALCHEMY_DATABASE_URIS = {
   'relengapi': 'sqlite:///relengapi.db',
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

SESSION_COOKIE_NAME='relengapi_ses'
SECRET_KEY='23-4589020389p5890-'  # NOT THAT SECRET
