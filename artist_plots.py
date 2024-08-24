import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import pandas as pd
from plotly.offline import iplot
from plotly.subplots import make_subplots


def artists_with_most_songs(df, column='Artist', top_n=10, title='Top 10 Artists with Most Songs', width=750, height=450):
    
    df_artist = df[column].value_counts().reset_index()
    df_artist.columns = [column, 'Count']
    df_artist = df_artist.head(top_n)
    
    fig = px.bar(
        df_artist, 
        x=column, 
        y='Count', 
        title=title,
        color=column,
        color_discrete_sequence=px.colors.qualitative.Plotly  
    )
    
    fig.update_layout(
        width=width, 
        height=height,
        xaxis_title=f'{column} Name',
        yaxis_title='Number of Songs'
    )
    fig.update_traces(
        hovertemplate='Number of Songs: %{y}<extra></extra>'
    )
    fig.update_layout(showlegend=False)
    
    return fig

def plot_top_artists_streams(df):
    # Grouping by artist and sum of Spotify streams
    df_artist_streams = df.groupby('Artist')['Spotify Streams'].sum().reset_index()
    df_artist_streams = df_artist_streams.sort_values(by='Spotify Streams', ascending=False).head(10)
    
    fig = px.bar(
        df_artist_streams, 
        x='Artist', 
        y='Spotify Streams', 
        title='Top 10 Artists with Most Spotify Streams',
        color='Artist',
        color_discrete_sequence=px.colors.qualitative.Vivid 
    )
    
    fig.update_layout(
        width=750, 
        height=450,
        xaxis_title='Artist Name',
        yaxis_title='Total Streams'
    )
    fig.update_traces(
        hovertemplate='Total Streams: %{y}<extra></extra>'
    )
    fig.update_layout(showlegend=False)
    
    
    return fig


def plot_top_artists_total_streams(df):
    platform_streams = ['Spotify Streams', 'YouTube Views','TikTok Views', 'Pandora Streams','Soundcloud Streams','Shazam Counts']
    df['Total Streams'] = df[platform_streams].sum(axis=1)
    top_artists_total_streams = df.groupby('Artist')['Total Streams'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_artists_total_streams, x='Total Streams', y='Artist', orientation='h', title='Top 10 Most Streamed Artists Across All Platforms',color='Artist')
    fig.update_layout(showlegend=False)
    return fig

def plot_top_artists_total_streams_without_tiktok(df):
    platform_streams = ['Spotify Streams', 'YouTube Views','Pandora Streams','Soundcloud Streams','Shazam Counts']
    df['Total Streams'] = df[platform_streams].sum(axis=1)
    top_artists_total_streams = df.groupby('Artist')['Total Streams'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_artists_total_streams, x='Total Streams', y='Artist', orientation='h', title='Top 10 Most Streamed Artists Across All Platforms minus tiktok',color='Artist')
    fig.update_layout(showlegend=False)
    return fig

def plot_top_50_artists_pie(df):
    artists = df['Artist'].value_counts()
    top_50_sum = artists[:50].sum()
    total_songs = len(artists)
    other_artists_count = len(artists) - 50
    
    fig = px.pie(values=[top_50_sum, total_songs - top_50_sum], 
                 names=['Top 50 artists', f'Other {other_artists_count} artists'], 
                 title="How many songs do the top 50 artists have?",
                 color_discrete_sequence=['#4287f5', '#f54287']
                ).update_traces(textinfo='value')
    
    return fig

def plot_artists_with_one_song_pie(df):
    artists = df['Artist'].value_counts()
    artists_with_one_song = artists.loc[lambda x: x == 1]
    
    fig = px.pie(values=[len(artists_with_one_song), len(artists) - len(artists_with_one_song)],
                 names=['1 song', '>1 songs'], 
                 title="Artists with 1 top hit VS Artists with >1 top hit",
                 color_discrete_sequence=['#4287f5', '#f54287']
                ).update_traces(textinfo='label')
    
    return fig
