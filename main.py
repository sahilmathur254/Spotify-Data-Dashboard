import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
from plotly.offline import iplot
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
st.set_page_config(layout="wide")
from artist_plots import *
from songs_plots import *
from all_platform_plots import *
from cross_platform_plots import *

# Titles and Subtitles
st.title("Most Streamed Spotify Songs 2024")

# Loading the data
df = pd.read_excel('Most Streamed Spotify Songs 2024_cleaned.xlsx')

platforms_playlists_reach = ['Spotify Playlist Reach', 'YouTube Playlist Reach', 'Deezer Playlist Reach']
platforms_streams = ['Spotify Streams', 'YouTube Views', 'TikTok Views','AirPlay Spins', 'SiriusXM Spins', 'Pandora Streams', 
                         'Soundcloud Streams', 'Shazam Counts']
platforms_playlist_counts = ['Spotify Playlist Count', 'Apple Music Playlist Count', 'Deezer Playlist Count', 'Amazon Playlist Count','Pandora Track Stations']

# Extracting the year from the Release Date column
df['Year'] = pd.to_datetime(df['Release Date']).dt.year

# total streams across all platforms for each track
df['Total Streams'] = df[platforms_streams].sum(axis=1)


tab1, tab2, tab3, tab4 = st.tabs(["Songs", "Artists", "All Platform Stats", "Cross-Platform Comparisons"])

with tab1:
        st.header("Songs")
                # Table layout
        c1, c2= st.columns(2)
        c3, c4= st.columns(2)
        c5, c6= st.columns(2)
        c7, c8= st.columns(2)

        with c1:
            st.plotly_chart(plot_released_year_distribution(df))

        with c2:
            st.plotly_chart(plot_top_spotify_songs(df))

        with c3:
            st.plotly_chart(plot_top_10_songs_streams(df))

        with c4:
            st.plotly_chart(plot_top_10_songs_streams_minus_tiktok (df))

        with c5:
            st.plotly_chart(plot_top_10_songs_playlist_counts(df))

        with c6:
            st.plotly_chart(plot_explicit_tracks(df))

        with c7:
            st.plotly_chart(plot_explicit_vs_non_explicit(df))

        with c8:
            st.plotly_chart(plot_popularity_by_explicit_content(df))

        st.subheader("Top Songs by Decades")
        c9, c10= st.columns(2)
        c11, c12= st.columns(2)

        with c9:
             st.plotly_chart(plot_top_songs_2020s(df))

        with c10:
             st.plotly_chart(plot_top_songs_2010s(df))

        with c11:
             st.plotly_chart(plot_top_songs_2000s(df))

        with c12:
             st.plotly_chart(plot_top_songs_pre_2000s(df))
    
with tab2:
        st.header("Artists")
        c1, c2= st.columns(2)
        c3, c4= st.columns(2)
        c5, c6= st.columns(2)

        with c1:
            st.plotly_chart(artists_with_most_songs(df))

        with c2:
            st.plotly_chart(plot_top_artists_streams(df))

        with c3:
            st.plotly_chart(plot_top_artists_total_streams(df))

        with c4:
            st.plotly_chart(plot_top_artists_total_streams_without_tiktok(df))
        
        with c5:
             st.plotly_chart(plot_artists_with_one_song_pie(df))

        #with c6:
        #     st.plotly_chart(plot_top_50_artists_pie(df))


with tab3:
        st.header("All Platform Stats")
        st.subheader("Spotfiy")
                
        c1, c2= st.columns(2)
        c3, c4= st.columns(2)
        c5, c6= st.columns(2)
        
        with c1:
             st.plotly_chart(plot_top_songs_by_platform(df, 'Spotify Streams'))

        with c2:
             st.plotly_chart(plot_top_songs_by_platform(df, 'Spotify Playlist Count'))

        with c3:
             st.plotly_chart(spotify_streams_over_time(df))

        with c4:
             st.plotly_chart(plot_popularity_vs_streams(df))

        
        st.subheader("YouTube")
        c7, c8= st.columns(2)
        c9, c10= st.columns(2)

        with c7:
             st.plotly_chart(plot_top_songs_by_platform(df, 'YouTube Views'))

        with c8:
             st.plotly_chart(plot_top_songs_by_platform(df, 'YouTube Playlist Reach'))

        with c9:
             st.plotly_chart(plot_yearly_stream_growth_youtube(df))


        st.subheader("TikTok")
        c11, c12= st.columns(2)
        c19, c20= st.columns(2)

        with c11:
            st.plotly_chart(plot_top_songs_by_platform(df, 'TikTok Views'))

        with c12:
            st.plotly_chart(plot_top_songs_by_platform(df, 'TikTok Posts'))

        with c19:
            st.plotly_chart(plot_top_songs_by_platform(df, 'TikTok Likes'))

        with c20:
            st.plotly_chart(plot_tiktok_correlation_heatmap(df))

    
        st.subheader("Apple")

        c21, c22= st.columns(2)
        c23, c24= st.columns(2)
        c30, c31= st.columns(2)

        with c21:
            st.plotly_chart(plot_top_songs_by_platform(df, 'Apple Music Playlist Count'))

        with c22:
            st.plotly_chart(plot_top_songs_by_platform(df, 'AirPlay Spins'))

        with c23:
            st.plotly_chart(plot_top_songs_by_platform(df, 'Shazam Counts'))

        with c24:
            st.plotly_chart(plot_apple_music_correlation_heatmap(df))

        with c30:
            st.plotly_chart(plot_yearly_stream_growth_apple(df))

        st.subheader("Other Platforms")
        c13, c14= st.columns(2)
        c15, c16= st.columns(2)
        c17, c18= st.columns(2)

        with c13:
            st.plotly_chart(plot_top_songs_by_platform(df, 'Pandora Streams'))

        with c14:
            st.plotly_chart(plot_top_songs_by_platform(df, 'Soundcloud Streams'))

        with c15:
            st.plotly_chart(plot_top_songs_by_platform(df, 'SiriusXM Spins'))


with tab4:
        st.header("Cross-Platform Comparisons")
        
        c1, c7= st.columns(2)
        c2,c3,c4 = st.columns(3)
        c5,c6 = st.columns(2)
        #c8, c9= st.columns(2)
        c25, c26= st.columns(2)

        with c1:
             st.plotly_chart(plot_proportion_of_streams_by_platform(df))

        with c2:
             st.plotly_chart(plot_scatter(df, 'Spotify Streams', 'YouTube Views'))

        with c3:
            st.plotly_chart(plot_scatter(df, 'Spotify Streams', 'TikTok Views'))

        with c4:
            st.plotly_chart(plot_scatter(df, 'Spotify Streams', 'AirPlay Spins'))

        with c5:
            st.plotly_chart(plot_total_streams_by_platform(df))

        with c6:
            st.plotly_chart(plot_average_streams_per_platform(df))

        with c7:
            st.plotly_chart(plot_platform_correlation_heatmap(df))

        #with c8:
        #    st.plotly_chart(plot_streams_vs_playlists(df))
#
        #with c9:
        #    st.plotly_chart(plot_spotify_vs_other_streams(df))

        with c25:
            st.plotly_chart(plot_sunburst_streams(df,'Taylor Swift'))

        with c26:
            st.plotly_chart(plot_sunburst_streams(df,'Diljit Dosanjh'))