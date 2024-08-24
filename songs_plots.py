import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import pandas as pd





def plot_released_year_distribution(df):
    df['Release Year'] = pd.DatetimeIndex(df['Release Date']).year
    df_year = df['Release Year'].value_counts().reset_index()
    df_year.columns = ['Year', 'Count']
    df_year = df_year.head(10).sort_values(by='Year')
    fig = px.bar(df_year, x='Year', y='Count', title='Top 10 Years with Most Songs')
    fig.update_xaxes(title='Year', type='category')
    fig.update_layout(width=750, height=450)
    fig.update_yaxes(title='Number of Songs')
    fig.update_traces(hovertemplate='Number of Songs: %{y}')
    return fig


def plot_top_songs_by_platform(df, platforms_streams):
    df_top10 = df.sort_values(by=platforms_streams, ascending=False).head(10)
    fig = px.bar(df_top10, x='Track', y=platforms_streams, title=f'Top 10 songs by {platforms_streams}')
    fig.update_layout(width=800, height=400)
    fig.update_xaxes(title='Song Name')
    fig.update_yaxes(title=f'Number of {platforms_streams}')
    fig.update_traces(hovertemplate=f'Number of {platforms_streams}: %{{y}}')
    return fig

def plot_explicit_tracks(df):
 # Converting Release Date to datetime and extract the year
    df['Release Date'] = pd.to_datetime(df['Release Date'])
    df['Year'] = df['Release Date'].dt.year

    # Mapping the Explicit Track column to Yes and No
    df['Explicit'] = df['Explicit Track'].map({1: 'Yes', 0: 'No'})

    # Grouping the data by Year and Explicit columns
    explicit_by_year = df.groupby(['Year', 'Explicit']).size().reset_index(name='Count')

    fig = px.bar(explicit_by_year, x='Year', y='Count', color='Explicit', 
                 title='Distribution of Explicit Tracks by Year',
                 labels={'Count': 'Number of Tracks'},
                 color_discrete_sequence=px.colors.sequential.RdBu)
    return fig

def plot_explicit_vs_non_explicit(df):
    explicit_counts = df['Explicit Track'].value_counts().reset_index()
    explicit_counts.columns = ['Explicit Track', 'Count']
    explicit_counts['Explicit Track'] = explicit_counts['Explicit Track'].map({1: 'Yes', 0: 'No'})
    fig = px.pie(explicit_counts, values='Count', names='Explicit Track', title='Songs with Explicit Lyrics vs Songs without Explicit Lyrics')
    fig.update_traces(marker=dict(colors=['#FF9999', '#66B2FF']))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def plot_distribution_of_release_dates(df):
    fig = px.histogram(df, x='Year', nbins=20, title='Distribution of Release Dates')
    return fig

def plot_top_spotify_songs(df, top_n=10):
    # Sorting the DataFrame by 'Spotify Popularity' in descending order and select the top N songs
    top_songs = df.sort_values(by='Spotify Popularity', ascending=False).head(top_n)
    
    if 'Release Year' not in df.columns:
        df['Release Year'] = pd.to_datetime(df['Release Date']).dt.year
    
    fig = px.line(top_songs, 
                  x='Track', 
                  y='Spotify Popularity', 
                  hover_data=['Artist', 'Release Year'], 
                  custom_data=['Track', 'Artist', 'Spotify Popularity', 'Release Year'], 
                  color_discrete_sequence=['green'], 
                  markers=True, 
                  title=f'<b>Top {top_n} songs on Spotify based on Popularity</b>')
    
    fig.update_traces(
        hovertemplate=(
            '<b>Track:</b> %{customdata[0]}<br>' +
            '<b>Artist:</b> %{customdata[1]}<br>' +
            '<b>Release Year:</b> %{customdata[3]}<br>' +
            '<b>Spotify Popularity:</b> %{y}'
        )
    )

    return fig
def plot_popularity_by_explicit_content(df):
    fig = px.box(df, 
                 x='Explicit', 
                 y='Spotify Popularity', 
                 color='Explicit',
                 color_discrete_sequence=['cyan', 'magenta'], 
                 title='<b>Popularity Based on Explicit Content</b>')
    return fig

def plot_top_10_songs_playlist_counts(df):

    # List of playlist count columns
    platforms_playlist_counts = ['Spotify Playlist Count', 'Apple Music Playlist Count', 
                                 'Deezer Playlist Count', 'Amazon Playlist Count',
                                 'Pandora Track Stations']

    # total playlist count across all platforms for each track
    df['Total Playlist Counts'] = df[platforms_playlist_counts].sum(axis=1)

    # top 10 tracks with the highest total playlist counts
    top_10_songs = df.nlargest(10, 'Total Playlist Counts')[['Track', 'Artist', 'Total Playlist Counts']]

    fig = px.bar(top_10_songs, x='Total Playlist Counts', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs in Most Playlists Overall',
                 labels={'Total Playlist Counts': 'Total Playlist Counts', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.sequential.RdBu)
    
    fig.update_layout(showlegend=False)

    return fig

def plot_top_10_songs_streams(df):
    # List of stream count columns
    platforms_streams = ['Spotify Streams', 'YouTube Views', 'TikTok Views', 
                         'AirPlay Spins', 'SiriusXM Spins', 'Pandora Streams', 
                         'Soundcloud Streams', 'Shazam Counts']

    #total streams across all platforms for each track
    df['Total Streams'] = df[platforms_streams].sum(axis=1)

    # top 10 tracks with the highest total streams
    top_10_songs = df.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]

    fig = px.bar(top_10_songs, x='Total Streams', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs by Total Streams Across All Platforms',
                 labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.sequential.Viridis)

    fig.update_layout(showlegend=False)

    return fig


def plot_top_10_songs_streams_minus_tiktok(df):
    # List of stream count columns
    platforms_streams = ['Spotify Streams', 'YouTube Views', 
                         'AirPlay Spins', 'SiriusXM Spins', 'Pandora Streams', 
                         'Soundcloud Streams', 'Shazam Counts']

    # total streams across all platforms for each track
    df['Total Streams'] = df[platforms_streams].sum(axis=1)

    # top 10 tracks with the highest total streams
    top_10_songs = df.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]

    fig = px.bar(top_10_songs, x='Total Streams', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs by Total Streams Across All Platforms minus TikTok',
                 labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.qualitative.Plotly)


    fig.update_layout(showlegend=False)

    return fig


def plot_top_songs_by_decade(df):

    # Defining the decades
    decades = {
        '2020s': (2020, 2024),
        '2010s': (2010, 2019),
        '2000s': (2000, 2009),
        'Pre-2000s': (0, 1999)
    }

    # Plot for each decade
    for decade_name, (start_year, end_year) in decades.items():
        # Filtering the data for the current decade
        df_decade = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

        # top 10 tracks with the highest total streams for the current decade
        top_10_songs_decade = df_decade.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]

        fig = px.bar(top_10_songs_decade, x='Total Streams', y='Track', 
                     orientation='h', color='Artist',
                     title=f'Top 10 Songs by Total Streams in the {decade_name}',
                     labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                     color_discrete_sequence=px.colors.qualitative.Dark24)

        fig.update_layout(showlegend=False)

        return fig


def plot_top_songs_2020s(df):
    df_2020s = df[(df['Year'] >= 2020) & (df['Year'] <= 2024)]
    top_10_songs_2020s = df_2020s.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]
    
    fig = px.bar(top_10_songs_2020s, x='Total Streams', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs by Total Streams in the 2020s',
                 labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.qualitative.Dark24)
    
    fig.update_layout(showlegend=False)
    return fig

def plot_top_songs_2010s(df):
    df_2010s = df[(df['Year'] >= 2010) & (df['Year'] <= 2019)]
    top_10_songs_2010s = df_2010s.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]
    
    fig = px.bar(top_10_songs_2010s, x='Total Streams', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs by Total Streams in the 2010s',
                 labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.qualitative.Dark24)
    
    fig.update_layout(showlegend=False)
    return fig


def plot_top_songs_2000s(df):
    df_2000s = df[(df['Year'] >= 2000) & (df['Year'] <= 2009)]
    top_10_songs_2000s = df_2000s.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]
    
    fig = px.bar(top_10_songs_2000s, x='Total Streams', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs by Total Streams in the 2000s',
                 labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.qualitative.Dark24)
    
    fig.update_layout(showlegend=False)
    return fig


def plot_top_songs_pre_2000s(df):
    df_pre_2000s = df[(df['Year'] >= 0) & (df['Year'] <= 1999)]
    top_10_songs_pre_2000s = df_pre_2000s.nlargest(10, 'Total Streams')[['Track', 'Artist', 'Total Streams']]
    
    fig = px.bar(top_10_songs_pre_2000s, x='Total Streams', y='Track', 
                 orientation='h', color='Artist',
                 title='Top 10 Songs by Total Streams in the Pre-2000s',
                 labels={'Total Streams': 'Total Streams', 'Track': 'Song'},
                 color_discrete_sequence=px.colors.qualitative.Dark24)
    
    fig.update_layout(showlegend=False)
    return fig
