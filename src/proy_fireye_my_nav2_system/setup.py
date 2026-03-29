from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'proy_fireye_my_nav2_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'param'), glob('param/*.yaml')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'map'), glob('map/*.pgm')),
        (os.path.join('share', package_name, 'map'), glob('map/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='grey',
    maintainer_email='122355310+GreysyBurgos@users.noreply.github.com',
    description='Navigation2 setup for Fireye',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'initial_pose_pub = proy_fireye_my_nav2_system.initial_pose_pub:main',
        ],
    },
)
