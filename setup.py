from distutils.core import setup
import cyflib
long_desc = open("cyflib/long_desc.txt").read()
setup(
    name='cyflib',
    version=cyflib.__version__,
    author='inobagger',
    author_email='inobagger@gmail.com',
    packages=['cyflib', 'cyflib/packages/ecdsa', 'cyflib/packages'],
    data_files=[('txt', ['cyflib/readme.txt', 'cyflib/license.txt', 'cyflib/changes.txt', 'cyflib/long_desc.txt'])],
    url='http://cyfnet.com/cyflib',
    license='Creative Commons Attribution 4.0 International Public License',
    description='CyfNet Python Library',
    download_url='http://cyfnet.com/cyflib/download',
    long_description=long_desc
)
