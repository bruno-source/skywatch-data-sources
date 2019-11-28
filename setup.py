from setuptools import setup

setup(
    name='skywatch-data-sources',
    version='0.1',
    py_modules=['skywatch_data_sources'],
    install_requires=[
        'beautifulsoup4',
        'click',
        'lxml',
        'requests',
        'tabulate',
    ],
    entry_points='''
        [console_scripts]
        skywatch-data-sources=skywatch_data_sources.cli:list_data_sources
    ''',
)
