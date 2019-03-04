import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

# -- Apps Definition -- #
app_package = 'all_about_a_hart_henrichsen'
release_package = 'tethysapp-' + app_package
app_class = 'all_about_a_hart_henrichsen.app:AllAboutAHartHenrichsen'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

# -- Python Dependencies -- #
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='Me, great, Civil Engineering, 10/10, , Hart',
    description='This app explains where I came from where am I and Where will I go',
    long_description='',
    keywords='',
    author='Hart Henrichsen',
    author_email='hart@byu.net',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
