# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pytest

from mediagoblin.init.plugins import setup_plugins
from mediagoblin.tests import MGClientTestCase

class ThreeDeeBureauBaseTestCase(MGClientTestCase):

    usernames = [(u'admin', dict(privileges=[u'active', u'admin'])),
                 (u'lindsay', dict(privileges=[u'active'])),
                 (u'rodrigo', dict(privileges=[u'active'])),
                 (u'daniel', dict())]

    def login(self, user=u'rodrigo', password='toast'):
        self.test_app.post(
            '/auth/login/', {
                'username': user,
                'password': password})

    def logout(self):
        self.test_app.get('/auth/logout/')
