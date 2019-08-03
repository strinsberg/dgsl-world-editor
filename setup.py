from setuptools import setup

setup(
    name='dgsl_editor',
    version='0.1.0',
    packages=['dgsl_editor'],
    python_requires='>=3',
    entry_points={
        'console_scripts':[
            'dgsl-editor=dgsl_editor.__main__:main'
        ]
    },
)
