import os
import sys
import pandas as pd
from plotly.graph_objs import Figure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from songs_plots import plot_released_year_distribution


def test_plot_released_year_distribution_returns_figure():
    data = {
        "Track": ["Song A", "Song B"],
        "Artist": ["Artist1", "Artist2"],
        "Release Date": ["2020-01-01", "2021-06-15"],
        "Spotify Streams": [1000, 2000],
    }
    df = pd.DataFrame(data)
    fig = plot_released_year_distribution(df)
    assert isinstance(fig, Figure)
