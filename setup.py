from setuptools import setup

setup(
    name='cassandra-importer',
    version='0.1.0',
    author='Utkarsh Sengar',
    author_email='usengar@ebay.com',
    packages=['ci'],
    entry_points={
        'console_scripts':
            ['cassandra_importer = ci.cass_importer:runner']
    },
    license='LICENSE.txt',
    description='Script to move cassandra data from one cluster to another.',
    long_description=open('README.md').read(),
    install_requires=[
        "pycassa >= 1.8.0-3",
    ],
    zip_safe=False,
)
