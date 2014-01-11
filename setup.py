from setuptools import setup, find_packages
import version

PACKAGE = 'python-dogeapi'

setup(name = PACKAGE, version = version.VERSION,
    license = "WTFPL",
    description = "dogeapi.com API client",
    author = "Jean-Christophe Saad-Dupuy",
    author_email = "saad.dupuy@gmail.com",
    url = "https://github.com/jcsaaddupuy/xbmc-client",
    packages = find_packages('src'),
    package_dir = {'':'src'},   # tell distutils packages are under src
    include_package_data = True,
    install_requires = ["requests", ]
    )
