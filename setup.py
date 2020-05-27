from setuptools import find_packages, setup

dependencies = [
    "requests==2.19.1"
]

setup(
    name='flip_rpc_client',
    version='1.0.0',
    url='https://github.com/flipsidecrypto/flip-rpc-client-python',
    description='Python client accessing Flip RPC interface.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    python_requires='>=3.6',
    classifiers=[      
        'Development Status :: 5 - Production/Stable',       
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)