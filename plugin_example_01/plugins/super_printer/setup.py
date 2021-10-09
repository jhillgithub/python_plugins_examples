from setuptools import setup

setup(
    name='super_printer',
    entry_points={
        'myapp_plugins': [
            'super_printer = super_printer:main',
        ],
    }
)