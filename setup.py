from distutils.core import setup

with open(('README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TinyDBOperations',
    packages=['TinyDBOperations'],
    version='0.1',
    license='MIT',
    description='A python wrapper used to perform additional TinyDB operations',
    long_description=long_description,
    author='multiii',
    author_email='76multi@gmail.com',
    url='https://github.com/multiii/TinyDBOperations',
    download_url='',
    keywords=['TinyDB', 'tinydb', 'operations'],
    install_requires=[
        'TinyDB',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
