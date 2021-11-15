from setuptools import setup

package_name = 'client'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dave',
    maintainer_email='dave@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'client_start_g = client.client_node_getter:main',
		    'client_start_s = client.client_node_setter:main',
            'client_start = client.client_node:main',
            'client_start2 = client.client_node2:main',
        ],
    },
)
