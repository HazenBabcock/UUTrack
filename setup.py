from setuptools import setup

setup(
    name='UUTracking',
    version='0.1',
    description='Camera framework',
    packages=['UUTrack',
              'UUTrack.View',
              'UUTrack.View.Camera',
              'UUTrack.Model',
              'UUTrack.Model.Cameras',
              'UUTrack.Controller',
              'UUTrack.Controller.devices',
              'UUTrack.Controller.devices.keysight',
              'UUTrack.Controller.devices.hamamatsu',
              'UUTrack.Controller.devices.PhotonicScience'],
    url='https://github.com/aquilesC/UUTrack',
    license='MIT',
    author='Aquiles',
    author_email='aquiles@aquicarattino.com',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ],
    package_data={'UUTrack': ['View/Camera/Icons/*.*', 'View/Camera/Icons/*.*']},
    include_package_data=True,
    install_requires=['lantz',]
)
