# Exoplanet Hunting Project

## Introduction

This project focuses on the search for new exoplanets using data collected from the NASA Kepler space telescope. The dataset contains observations of several thousand stars, each labeled as either "confirmed exoplanet" or "non-exoplanet." The goal is to develop a machine learning model that can identify stars with exoplanets based on changes in light intensity (flux) over time.

## Dataset Description

### Flux Diagram

Planets do not emit light themselves, but they cause periodic dimming of the light emitted by the stars they orbit. This dataset contains measurements of light intensity (flux) over time for each star, and stars with confirmed exoplanets exhibit characteristic patterns of flux dimming.

### Trainset

- 5087 rows or observations.
- 3198 columns or features.
- Column 1 is the label vector, with values 2 (confirmed exoplanet) or 1 (candidate system).
- Columns 2 - 3198 represent flux values over time.
- Contains 37 confirmed exoplanet-stars and 5050 non-exoplanet-stars.

### Testset

- 570 rows or observations.
- 3198 columns or features.
- Column 1 is the label vector, with values 2 (confirmed exoplanet) or 1 (candidate system).
- Columns 2 - 3198 represent flux values over time.
- Contains 5 confirmed exoplanet-stars and 565 non-exoplanet-stars.


## Project Usage

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Set up your Python environment and install the required libraries by running 'pip install -r requirements.txt' in your terminal.
3. Open and run the 'exoplanet-exploration-using-ml.ipynb' file located in the 'models' folder.

4. To launch the website:
5. Make sure the pickle file is saved in the 'models' folder after running the 'exoplanet-exploration-using-ml.ipynb' file.
6. Open your terminal and execute the following command "python manage.py runserver".

## Contributing

If you want to contribute to this project, please open an issue or submit a pull request. We welcome any contributions, whether they involve code, documentation, or improvements to the project. Thanks!
