from setuptools import setup

setup(name='reagle',
      version='0.1.0',
      description='For creating data visualisations from EAGLE snapshots',
      url='https://github.com/Alex-Tremayne/reagle',
      author='Alex Tremayne',
      author_email='alexjtremayne@gmail.com',
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6'],
      packages=['reagle'],
      install_requires=['numpy','h5py'],
      zip_safe=False)
