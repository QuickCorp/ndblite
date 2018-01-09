from distutils.core import setup
setup(
  name = 'ndblite',
  packages = ['ndblite'], # this must be the same as the name above
  version = '0.1.1',
  description = 'Quick Corp ndblite',
  author = 'Jean Machuca',
  author_email = 'correojean@gmail.com',
  url = 'https://github.com/QuickGroup/ndblite.git', # use the URL to the github repo
  download_url = 'https://github.com/QuickGroup/ndblite/archive/master.zip', # I'll explain this in a second
  keywords = ['ndb', 'gae', 'sqlite','google','app','engine','sqlite3','sqlitemodel'], # arbitrary keywords
  classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Environment :: Web Environment',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Topic :: Communications :: Email',
      'Topic :: Office/Business',
      'Topic :: Software Development :: Bug Tracking',
      ],
  install_requires=['sqlitemodel>=0.1.1']
)
# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
