from setuptools import setup, find_packages

setup(
    name='love_encoder',
    version='0.1.0',
    author='lovevsick',
    author_email='laiquanguy82@gmail.com',
    description='Custom Encode Of Love(Cant Decode, IDK)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zx155/love_encode.git',  
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)