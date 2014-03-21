from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

setup(
    name="notedown",
    version='1.0.4dev',
    description="Convert markdown to IPython notebook.",
    long_description=long_description,
    packages=['notedown'],
    author="Aaron O'Leary",
    author_email='dev@aaren.me',
    license='BSD 2-Clause',
    url='http://github.com/aaren/notedown',
    install_requires=['ipython', ],
    entry_points={
        'console_scripts': [
            'notedown = notedown:cli',
        ],
    }
)
