from setuptools import setup

setup(
    name='anotherone',
    entry_points={
        'console_scripts': [
            'anotherone = anotherone:cli',
        ],
        'myapp_plugins': [
            'anotherone = anotherone:run',
        ],
    }
)