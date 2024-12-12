# MCMC Spectrum Fitting for G-Type Stars

## Description
A tutorial-based project exploring Markov Chain Monte Carlo (MCMC) methods for stellar spectrum fitting, submitted as part of my Computational Methods final project in the CUNY Astrophysics Masters Program.

## Installation

Clone the repository

git clone ttps://github.com/astro-andrea/finalproject_comp.git
cd finalproject_comp

Run the Jupyter Notebook from the cloned repository

jupyter notebook finalnotebook.ipynb


## Setup Instructions
1. The first cell in the notebook will run setup.py to install any packages needed for the tutorial. No extra scripts need to be run, everything is in the notebook if you run the cells consecutively!
2. I have included comments along the way to explain chunks of the code, and certain things to lookout for if you choose to implement this on your own data

## Tutorial Overview
The tutorial is divided into the following sections:
1. **Part 1: Getting Familiar with the Spectrum**: Opens fits file, sets variables, truncates around h-alpha line
2. **Part 2: MCMC on Fake Data**: Implements MCMC on simulated data
3. **Part 3: MCMC on Real Data**: Implements MCMC on our spectrum and produces a model and various plots

## Future Work
This project is a starting point for applying MCMC methods in spectrum fitting. Future improvements could include:
- Expanding tutorial to create complete packages for ease of use on other spectra
- Building in more models to use for other more complex features features in the spectra

## Contact
For questions, feedback, or collaboration, please contact:
Andrea Bracamonte 
abracamonte@gradcenter.cuny.edu
CUNY Astrophysics 

## Acknowledgements

Thank you to the contributers of emcee for creating such a great package and documentation that inspired me to build on.
- [Foreman-Mackey, Hogg, Lang & Goodman (2012)](https://arxiv.org/abs/1202.3665)
- [emcee.readthedocs.io](http://emcee.readthedocs.io/)

Thank you to Jared Goldberg for teaching such a comprehensive and thorough computational methods course!

