# Astronomical Data for Machine Learning - Eric Tang and Calvin Grewal
This is a dataset containing astronomical postion data for the 8 planets in the solar system obtained from JPL Horizons and Astropy ephemerus data, in conjunction with astronomical event data from the NASA SkyEvents Calendar Database for the last 20 years. We obtained 20 years of positional data as well as astrological event data (Eclipses, Equinoxes, etc.) for each of the planets in the Solar System, relative to 1000 different locations on Earth for the purpose of being able to train a geocentric model that would be able to predict location of planets relative to time and locations on earth. We then cleaned and organized the positions/time/location data such that each is accessible easily via a pandas dataframe. The final dataset is too large to be stored on github and consists of 10 GB of raw text data stored on the google drive linked below.

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
4. Run the generate data function to generate dataframes for use
The generate data function takes in the following arguments
  * `num_locations`
    - The number of locations to include in the dataframe (unless further specified by the location parameter). Max value 999, Min value 2.
  * `num_days`
    - The number of days of data to include in the dataframe. All data starts at 01-01-2000 00:00 and is offset by a gap of one day per data point.
  * `time_step`
    - The number of days at which to sample each data point in the dataframe. Must be an integer.
  * `planet`
    - A list containing the numbers corresponding to which planets should have their data included in the dataframe. Valid indices are listed in the table below
  
                                     | Index | Planet    |
                                     |-------|--------   |
                                     | 1     |    Mercury|
                                     | 2     |    Venus  |
                                     | 3     |    Earth  | 
                                     | 4     |     Mars  | 
                                     | 5     |    Jupiter|
                                     | 6     |    Saturn | 
                                     | 7     |     Uranus| 
                                     | 8     |    Neptune|
   * `location`
     - A list containing the numbers corresponding to which planets should have their data included in the dataframe. Valid indices range from 1 to 999. Exact mappings from index to name are listed in locations.txt. All included indices must also fall in `range(1, num_locations)`, so those who intend to use this argument should set num_locations to 999.
## Data Generation Examples

## Data Format
Below is an example of the return value of a generated dataframe. Each row of the dataframe correspondes to one set of observations from one location on earth at a given time. The lat/lon and the Geocentric XYZ vector coordinates of the location on earth are included, as well as the ra/dec, az/alt, and Geocentric XYZ vector coordinates of the planet at the given time as well. Event data is appended to the positional data at the end of the dataframe, with each event being one hot encoded based on the date for each row (1 implying the event occurred on that date and 0 implying the event did not occur on that date). The full list of columns of the dataframe can be found in df_columns.txt. 
![](https://github.com/erictang000/astro-data/blob/master/example_data/dataframe.png?raw=true)



