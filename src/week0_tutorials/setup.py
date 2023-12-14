import os
from glob import glob
from setuptools import find_packages, setup
package_name = 'week0_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'my_launch.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anushka',
    maintainer_email='anushkav1888@gmail.com',
    description='erc',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'daughter1 = week0_tutorials.daughter1:main',
'daughter3 = week0_tutorials.daughter3:main',     
  'daughter2 = week0_tutorials.daughter2:main',
    'daughter4 = week0_tutorials.daughter4:main',
'basestation = week0_tutorials.basestation:main',
        ],
    },
)
