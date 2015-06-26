from setuptools import setup, find_packages

setup(
    name='pygkv',
    version='0.1a1',

    description="A library to use Git as Key-Value store",
    long_description="Uses Git as Key-Value store with a dictionary-like API",

    url="https://github.com/ishankhare07/PyGKV",

    author="Ishan Khare",
    author_email="ishankhare07@gmail.com",

    license="MIT",

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Database',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    keywords = "Git Data Persistence Databases Key-Value Store",
    
)
