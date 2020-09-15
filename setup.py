# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-actions is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()
OAREPO_VERSION = os.environ.get('OAREPO_VERSION', '3.3.0')
# Get the version string. Cannot be done with import!
install_requires = [
    'marshmallow',
    'flask'
]

tests_require = [
    # 'pytest>=4.6.3',
    # 'jsonschema',
    # 'pydocstyle',
    # 'isort',
    # 'check-manifest',
    'oarepo-mapping-includes',
    'oarepo-validate',
    'oarepo-invenio-model',
    # 'pytest-cov'
]

extras_require = {
    'tests': [
        *tests_require,
        'oarepo[tests]~={version}'.format(
            version=OAREPO_VERSION)],
    'tests-es7': [
        *tests_require,
        'oarepo[tests-es7]~={version}'.format(
            version=OAREPO_VERSION)],
}

setup_requires = [
    'pytest-runner>=2.7',
]
g = {}
with open(os.path.join('oarepo_actions', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='oarepo-actions',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='oarepo-actions Invenio',
    license='MIT',
    author='Alzbeta Pokorna',
    author_email='alzbeta.pokorna@cesnet.cz',
    url='https://github.com/oarepo-actions/oarepo-actions',
    packages=['oarepo_actions'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        # 'console_scripts': [
        #     'oarepo-actions = invenio_app.cli:cli',
        # ],
        'invenio_base.apps': [
            'oarepo_actions = oarepo_actions:Actions'
        ],
        # 'invenio_base.blueprints': [
        #     'oarepo_actions = oarepo_actions.theme.views:blueprint',
        # ],
        # 'invenio_assets.webpack': [
        #     'oarepo_actions_theme = oarepo_actions.theme.webpack:theme',
        # ],
        # 'invenio_config.module': [
        #     'oarepo_actions = oarepo_actions.config',
        # ],
    },
    setup_requires=setup_requires,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
