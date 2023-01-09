from setuptools import setup, find_packages

setup(
    name='pplog',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'jq', 'Pygments',
    ],
    entry_points={
        'console_scripts': [
            'pplog = pplog.__main__:main',
        ],
    },
)
