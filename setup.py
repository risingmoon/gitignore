import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitignore-risingmoon',  # Replace with your own username
    version='0.0.1',
    author='Justin Lee',
    author_email='justindavidlee88@gmail.com',
    description='A simple gitignore generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/risingmoon/gitignore',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control :: Git'
    ],
    entry_points={
        'console_scripts': [
            'gitignore=gitignore:main',
        ],
    },
    python_requires='>=3.7.7',
)
