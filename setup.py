

from setuptools import setup

package_name = 'Ofpp'

packages = [
    'numpy',
    ]

config = {
    'author': 'XU Xianghua',
    'author_email': 'dayigu@gmail.com',
    'description': 'A simple Python code for parse OpenFOAM data to Numpy.array',
    'license': 'MIT',
    'version': '0.1',
    'packages': [package_name],
    'install_requires': packages,
    'name': package_name,
    'zip_safe': False
}


setup(**config)
