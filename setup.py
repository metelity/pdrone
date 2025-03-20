from setuptools import setup, find_packages

setup(
    name="pdrone",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        'colorama',
        'dadata',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'pdrone=pdrone.cli:main',
        ],
    },
    author="metelity",
    description="A tool to get phone number information",
    license="MIT",
    keywords="phone number information",
    url="https://github.com/metelity/pdrone",
)