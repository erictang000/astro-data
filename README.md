# Astronomical Data for Machine Learning - Eric Tang and Calvin Grewal
This is a dataset containing postional data obtained from JPL Horizons and Astropy, as well as astronomical event data from NASA SkyEvents Calendar Database for 20 years.

## Setup
The relevant code used for scraping the dataset is contained within the `gen_input.py` and the `sample_horizons_batch_script.pl` files, and the relevant code and instructions for accessing the data can be obtained in the `189 Early Project.ipynb` file. 

### Instructions
1. Download data locally from [Google Drive](https://drive.google.com/drive/u/1/folders/16cBlFRV02PcA1_ypUR4UUju3h61P0zgg)
2. Make sure there is a file named `planets.csv` as well as all of the `output_i_j.txt` files in the same directory as the Jupyter Notebook file.
3. Open `189 Early Project.ipynb` and run all of the cells to create the dataset. 
