# Astronomical Data for Machine Learning - Eric Tang and Calvin Grewal
This is a dataset containing astronomical postion data for the 8 planets in the solar system obtained from JPL Horizons and Astropy ephemerus data, in conjuncton with astronomical event data from the NASA SkyEvents Calendar Database for the last 20 years. We obtained 20 years of positional data as well as astrological event data (Eclipses, Equinoxes, etc.) for each of the planets in the Solar System, relative to 1000 different locations on Earth for the purpose of being able to train a geocentric model that would be able to predict location of planets relative to time and locations on earth. We then cleaned and organized the positions/time/location data such that each is accessible easily via a pandas dataframe. The final dataset is too large to be stored on github and consists of 10 GB of raw text data stored on the google drive linked below.

## Requirements
The following must be installed to run the associated jupyter notebook:
* pandas (1.0.1)
* astropy (4.0.2)
* astroquery (0.4.1)
A working perl environment along with Python 3 must be installed to run the `gen_input.py` and the `sample_horizons_batch_script.pl` files, which send HTTP requests to the JPL Horizons system database. An example input file and output file is included in the example_data folder of the repository
The relevant code and instructions for accessing the data can be found in the `189 Early Project.ipynb` file, which should run on any working Jupyter version and Python 3 installation.

## Accessing Data
1. Clone this Git repository and install the required packages listed above.
2. Download and unzip data locally from the linked [Google Drive](https://drive.google.com/drive/u/1/folders/16cBlFRV02PcA1_ypUR4UUju3h61P0zgg) (note this requires a UC Berkeley email to access). 
2. Make sure that the unzipped data files named `planets.csv` as well as all of the `outputi_j.txt` files exist in the same directory as the `189 Early Project.ipynb`.
3. Open `189 Early Project.ipynb` and run the cells in order. 

## Data Format
![](https://github.com/erictang000/astro-data/example_data/dataframe.jpg?raw=true)



