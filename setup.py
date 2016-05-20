from setuptools import setup, find_packages
setup(
  name = 'playlyfe_grapqhl',
  version = '0.1.0',
  packages= ['src'],
  description='This is the official Playlyfe Python GraphQL API V3 SDK for the Playlyfe V3 API.',
  long_description='''
    It supports the JWT flow.
  ''',
  url='https://github.com/playlyfe/playlyfe-python-graphql-sdk',
  author='Peter John',
  author_email='peter@playlyfe.com',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.5'
  ],
  keywords='GraphQL, Playlyfe V3 API, Playlyfe SDK, Gamification'
)
