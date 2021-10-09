from setuptools import setup

setup(
    name='myapp',
    entry_points={
        'console_scripts': [
            'myapp = app:cli',
        ],
    }
)