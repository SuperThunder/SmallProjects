try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': '',
    'url': 'Project URL',
    'download_url': 'Download URL',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ProjectName'],
    'scripts': [],
    'name': 'Project Name'
}

setup(**config)
