#!/usr/bin/env python

from setuptools import setup, find_packages

package_name='baldor'
setup(
        name=package_name,
        version='0.1.3',
        description='The baldor package',
        author='Francisco Suarez-Ruiz',
        author_email='fsuarez6@gmail.com',
        url='http://wiki.ros.org/baldor',
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        data_files=[
            ('share/' + package_name, ['package.xml']),
            ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
            ],
        install_requires=["setuptools"],
        )
