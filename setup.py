from setuptools import setup, find_packages

setup(
    name='inlinestyler',
    version=__import__('inlinestyler').__version__,
    description='Inlines external CSS into HTML elements.',
    long_description=open('README.rst').read(),
    author='Dave Cranwell',
    maintainer='Dan Langer',
    maintainer_email='daniel@langer.me',
    license='BSD',
    url='http://github.com/dlanger/inlinestyler',
    download_url='http://github.com/dlanger/inlinestyler/downloads',
    include_package_data=True,
    zip_safe=False,
    keywords=['html', 'css', 'inline', 'style', 'email'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    install_requires=[
        'cssutils',
        'lxml',
        'requests>=1.0.0',
    ]
)
