import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fifa-player-recommendation-system',
    version='0.0.1',
    author='André Sousa',
    author_email='andreosousa95@gmail.com',
    description='Machine learning system to recommend FIFA players based on similar characteristics',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aosousa/FIFA-Player-Recommendation-System',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU GENERAL PUBLIC LICENSE',
        'Operating System :: OS Independent'
    ],
    packages = setuptools.find_packages(),
    install_requires=[
        "Flask==1.1.2",
        "Flask_Cors==3.0.10",
        "openpyxl==3.0.5",
        "PasteScript==3.3.0",
        "setuptools==56.0.0",
        "waitress==1.4.4"
    ],
    python_requires='>=3.6'
)