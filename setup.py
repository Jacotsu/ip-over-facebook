from setuptools import setup

classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Telecommunications Industry ",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: GNU Affero General Public License v3 or "
    "later (AGPLv3+)",
    "Natural Language :: English",
    "Operating System :: Unix"
    "Programming Language :: Python :: 3.7"
]

setup(
    name='ip-over-facebook',
    version=0.3,
    author="Benjamin Eriksson, Raffaele Di Campli",
    author_email="dcdrj.pub@gmail.com",
    license='AGPLv3+',
    install_requires=[
        "requests>=2.21.0",
        "python_pytun>=2.3.0",
        "setuptools>=40.8.0",
        "appdirs>=1.4.3"
    ],
    python_requires='>=3.7',
    packages=['IPoFB'],
    include_package_data=True,
    description="Use facebook as a network layer",
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'IPoFB-tun=ip_over_facebook.tun:main',
            'IPoFB-send_file=ip_over_facebook.sendFile:main',
        ]
    }
)
