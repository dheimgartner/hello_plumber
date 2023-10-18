from setuptools import setup, find_packages

setup(
    name='hello_plumber',
    version='0.0.1',
    install_requires=[
      "requests",
    ],
    packages=find_packages('.', exclude=['tests']),
    include_package_data=True,
    scripts=['bin/example',
             'bin/start_api'],
    entry_points={
      'console_scripts': [
         'install_rapi = hello_plumber.install:install_r_package',
         'uninstall_rapi = hello_plumber.install:uninstall_r_package' 
      ] ,
    },
)
