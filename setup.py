#!/usr/bin/env python
import pytest
from setuptools import setup, Command

class TestCommand(Command):
    """Runs the test suite."""
    description = """Runs the test suite."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import pytest
        pytest.main('./mediagoblin_scad/tests')

__VERSION__="0.1.0"
setup(
    name='mediagoblin-scad',
    version=__VERSION__,
    description='SCAD mediatype for GNU Mediagoblin',
    author='Rodrigo Rodrigues da Silva',
    author_email='rsilva@metamaquina.com.br',
    url='https://gitorious.org/metamaquina/mediagoblin-scad',
    download_url='https://gitorious.org/metamaquina/mediagoblin-scad/mediagoblin-scad-' + __VERSION__,
    packages=['mediagoblin_scad'],
    include_package_data=True,
    license=(b'License :: OSI Approved :: GNU Affero General Public License '
             b'v3 or later (AGPLv3+)'),
    cmdclass={'test': TestCommand},
)
