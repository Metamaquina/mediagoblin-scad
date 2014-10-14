# -*- coding: utf-8 -*-
#
# MediaGoblin SCAD -- SCAD mediatype for GNU Mediagoblin
# Copyright (C) 2014, Metamaquina.  See AUTHORS.
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

import os
import logging
import argparse
import subprocess

from mediagoblin import mg_globals as mgg
from mediagoblin.processing import (
    BadMediaFail, FilenameBuilder,
    MediaProcessor, ProcessingManager,
    request_from_args, get_process_filename,
    store_public, copy_original)


_log = logging.getLogger(__name__)

MEDIA_TYPE = 'mediagoblin_scad'
SUPPORTED_FILETYPES = ['scad']


def sniff_handler(media_file, **kw):
    _log.info('Sniffing {0}'.format(MEDIA_TYPE))
    if kw.get('media') is not None:  # That's a double negative!
        name, ext = os.path.splitext(kw['media'].filename)
        clean_ext = ext[1:].lower()  # Strip the . from ext and make lowercase

        if clean_ext in SUPPORTED_FILETYPES:
            _log.info('Found file extension in supported filetypes')
            return MEDIA_TYPE
        else:
            _log.debug('Media present, extension not found in {0}'.format(
                    SUPPORTED_FILETYPES))
    else:
        _log.warning('Need additional information (keyword argument \'media\')'
                     ' to be able to handle sniffing')

    return None

class FooProcessor:
    pass

class ScadProcessingManager(ProcessingManager):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.add_processor(FooProcessor)
