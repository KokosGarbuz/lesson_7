from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.1',
      description='Clean Folder',
      author='Mykhailo Levchuk',
      author_email='mihaluch2511@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)