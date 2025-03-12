from setuptools import setup

setup(
    name='freeMobileSMS',
    version='0.1',
    install_requires=[
        'importlib-metadata; python_version<"3.10"',
    ],
    entry_points={
        'console_scripts': [
            'sms = freeMobileSMS.__main__:main',
        ]
    }
)