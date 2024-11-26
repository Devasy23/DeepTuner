from setuptools import setup, find_packages

setup(
    name='deeptuner',
    version='0.1.8',
    author='Devasy Patel',
    author_email='patel.devasy.23@gmail.com',
    description='A package for fine-tuning deep learning models with Siamese architecture and triplet loss',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Devasy23/DeepTuner',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    install_requires=[
        'tensorflow>=2.12.0',
        'numpy>=1.21.0',
        'scikit-learn>=1.0.0',
        'Pillow>=9.0.0',
        'wandb>=0.15.0',
        'efficientnet>=1.0.0',
        'facenet-pytorch>=2.5.0',
        'requests>=2.31.0',
        'tqdm>=4.65.0',
    ],
    python_requires='>=3.7',
)
