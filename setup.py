from setuptools import setup
setup(
    name="rinobot_plugin",
    version="0.0.1",
    packages=["rinobot_plugin"],
    description='Rinobot plugin helpers',
    author='Eoin Murray',
    author_email='eoin@rinocloud.com',
    url='https://github.com/rinocloud/rinobot-plugin',
    download_url='https://github.com/rinocloud/rinobot-plugin/tarball/0.1',
    keywords=['rinocloud', 'rinobot', 'plugin'],
    classifiers=[],
    test_suite='rinobot_plugin.test.all',
    tests_require=['mock'],
    install_requires=[],
)
