
![Screenshot 2024-09-05 at 11 56 27 AM](https://github.com/user-attachments/assets/edfe9010-95da-4037-a840-b3a45ed61630)

# Overview
The Spotify Data Dashboard is an interactive web application built using Python and Streamlit. It provides visual insights into the most streamed Spotify songs of 2024. The dashboard displays various metrics such as song name, artist, total streams, release date, and duration, and offers dynamic visualizations to explore the data.

# Features
- Data Cleaning: A Jupyter Notebook (data_cleanup.ipynb) to clean and preprocess the raw dataset.
- Interactive Dashboard: A user-friendly dashboard built with Streamlit for visualizing top streamed songs, artists, and other metrics.
- Customizable Visualizations: Easily extendable to include additional charts, filters, and interactive elements.

# Getting Started
Follow these instructions to set up and run the project locally.

# Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pip (Python package installer)

# Installation
1. Clone the Repository:

```sh
git clone https://github.com/sahilmathur254/Spotify-Data-Dashboard.git
cd Spotify-Data-Dashboard
```
2. Install Required Packages:

Use the following command to install all necessary packages:

```sh
pip install -r requirements.txt
```

3. Prepare the Data:

Open `data_cleanup.ipynb` and run the notebook to clean the raw data.
Ensure that the cleaned dataset `(Most Streamed Spotify Songs 2024_cleaned.xlsx)` is available in the root directory.

# Running the Dashboard
To start the dashboard, run the following command from the terminal:

```sh
streamlit run main.py
```
This will launch the dashboard in your default web browser.

# Project Structure
```sh
Spotify-Data-Dashboard/
│
├── data_cleanup.ipynb                              # Jupyter Notebook for data cleaning
├── main.py                                         # Main script for running the Streamlit dashboard
├── utils.py                                        # Utility functions for data loading and visualization
├── Most Streamed Spotify Songs 2024_cleaned.xlsx   # Cleaned dataset used in the dashboard
├── requirements.txt                                # List of required Python packages
└── README.md                                       # Project documentation

```

# Customization
You can extend the dashboard by adding new features:

- Add Filters: Use Streamlit widgets like sliders or dropdowns to let users filter songs by artist, genre, or release date.
- More Visualizations: Incorporate more complex visualizations such as pie charts, line charts, or heatmaps to provide additional insights.


# Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/YourFeature
3. Commit your changes: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature/YourFeature
5. Open a pull request.

# Contact
For any questions or feedback, feel free to reach out:

- Author: Sahil Mathur
- Email: sahil.mathur2504@gmail.com
- GitHub: [sahilmathur254](https://github.com/sahilmathur254)
