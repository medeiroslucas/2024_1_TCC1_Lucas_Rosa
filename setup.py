from setuptools import setup

VERSION = "0.1.0"

requirements = open("requirements.txt").readlines()

if __name__ == "__main__":
    setup(
        name='cloud-pilot',
        version=VERSION,
        packages=['pilot'],
        license='MIT',
        author_email='medeirosrosalucas@gmail.com',
        description='Cloud Pilot - an AI developer that works with you to build complex projects',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
        ],
        install_requires=requirements,
        python_requires='>=3.9',
    )
