from setuptools import setup, find_packages

setup(
    name='flatpack',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'flatpack=flatpack.cli:main',
        ],
    },
    author='Centaur Inc.',
    author_email='info@centaurinc.com',
    description='A tool for packing and unpacking directory structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/centaurinc/flatpack',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)