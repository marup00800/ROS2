from setuptools import find_packages, setup

package_name = 'pack'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marup',
    maintainer_email='marup@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        "firstoop=pack.my_first_node_oop:main",
        "secondoop=pack.my_second_node_oop:main",
        "oops1=pack.my_first_node_oop:main",
        "oops2=pack.my_second_node_oop:main",
        "pub=pack.first_ros_pub:main",
        "pub1=pack.second_ros_pub:main",
        "sub=pack.first_ros_sub:main",
        "pub2=pack.pub_ascii:main",
        "sub2=pack.sub_ascii:main",
        "pub3=pack.fib_pub:main",
        "sub3=pack.fib_sub:main",
        "pub4=pack.large_pub:main",
        "sub4=pack.large_sub:main"
    ],
},
)
