from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]


setup(name='opsftmongo',
      version='1.0',
      description='opsftmongo',
      author='eggtree',
      author_email='eggtree@requiredhealth.org',
      url='http://www.requiredhealth.org/',
      packages = find_packages(),
      install_requires=reqs,
     # install_requires=['Flask==0.10.1','Flask-RESTful==0.2.5','six==1.4.1','requests==2.0.0'],
     )

