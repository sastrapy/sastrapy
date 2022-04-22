from setuptools import setup, find_packages

setup(
    name='Sastrapy',
    version='0.1.9',
    description='A simple text processing for Bahasa Indonesia',
    long_description='A simple text processing for Bahasa Indonesia',
    url='https://github.com/sastrapy/sastrapy',
    author='Khoerul Umam',
    author_email='id.khoerulumam@gmail.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['pathlib'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='stopword remover tokenize slang converter text processing',
    package_data={
        '': ['Corpus/Dictionary/*.txt'],
    },
)
