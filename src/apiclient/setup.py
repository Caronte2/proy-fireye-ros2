from setuptools import setup, find_packages

package_name = 'apiclient'

setup(
    name=package_name,
    version='0.0.1',

    packages=find_packages(),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],

    install_requires=[
        'setuptools',
        'requests'
    ],

    zip_safe=True,
    maintainer='Manuel Perez',
    description='Servicio de comunicación con API local',
    license='Apache-2.0',

    entry_points={
        'console_scripts': [
            'connection_service = apiclient.connection_node:main',

            'test_get_alertas = apiclient.test.test_get_alertas:main',

            'test_insert_alerta = apiclient.test.test_insert_alerta:main',

            'test_flow = apiclient.test.test_flow:main',
        ],
    },
)