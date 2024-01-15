from setuptools import setup
setup(
    name = 'pic_sorter',
    version = '0.1.0',
    packages = ['pic_sorter'],
    install_requires=['face_recognition','tdqm'],
    package_dir={'pic_sorter':'pic_sorter'},
    entry_points = {
        'console_scripts': [
            'pic_sorter = pic_sorter.__main__:main'
        ]
    })