from setuptools import setup


setup(
    name='httpie-next',
    description='Use urllib3.future alongside HTTPie.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    version='1.1.0',
    author='Ahmed TAHRI',
    author_email='ahmed.tahri@cloudnursery.dev',
    license='MIT',
    url='https://github.com/Ousret/httpie-next',
    py_modules=['httpie_next'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.transport.v1': [
            'httpie_next = httpie_next:HTTPNextTransportPlugin'
        ]
    },
    install_requires=[
        'httpie>=3.0',
        'urllib3.future>=2.0.931'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
