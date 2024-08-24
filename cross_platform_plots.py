import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import pandas as pd


def plot_scatter(df, x_column, y_column):
    fig = px.scatter(
        df, 
        x=x_column, 
        y=y_column, 
        title='Scatter Plot of ' + x_column + ' vs. ' + y_column,
        hover_data={
            'Track': True, 
            'Artist': True, 
            x_column: True, 
            y_column: True
        }
    )
    
    fig.update_layout(
        width=600, 
        height=400
    )
    fig.update_xaxes(title=x_column)
    fig.update_yaxes(title=y_column)
    fig.update_traces(marker=dict(size=12, opacity=0.8))
    
    return fig

def plot_proportion_of_streams_by_platform(df):
    platform_streams = ['Spotify Streams', 'YouTube Views','TikTok Views', 'Soundcloud Streams', 'Pandora Streams']
    total_streams_by_platform = df[platform_streams].sum().reset_index()
    total_streams_by_platform.columns = ['Platform', 'Total Streams']
    fig = px.pie(total_streams_by_platform, values='Total Streams', names='Platform', title='Proportion of Streams by Platform', color_discrete_sequence=px.colors.sequential.RdBu)

    return fig


def plot_total_streams_by_platform(df):

    # Total streams by platform
    platform_streams = {
        'Spotify': df['Spotify Streams'].sum(),
        'YouTube': df['YouTube Views'].sum(),
        'TikTok': df['TikTok Views'].sum(),
        'AirPlay': df['AirPlay Spins'].sum(),
        'SiriusXM': df['SiriusXM Spins'].sum(),
        'Pandora': df['Pandora Streams'].sum(),
        'Soundcloud': df['Soundcloud Streams'].sum(),
        'Shazam': df['Shazam Counts'].sum()
    }

    platform_df = pd.DataFrame(list(platform_streams.items()), columns=['Platform', 'Total Streams'])

    fig = px.bar(platform_df, x='Platform', y='Total Streams', 
                 title='Total Streams by Platform',
                 labels={'Total Streams': 'Total Streams', 'Platform': 'Platform'},
                 color='Platform')
    
    return fig


def plot_average_streams_per_platform(df):

    # Average streams by platform
    platform_streams_avg = {
        'Spotify': df['Spotify Streams'].mean(),
        'YouTube': df['YouTube Views'].mean(),
        'TikTok': df['TikTok Views'].mean(),
        'AirPlay': df['AirPlay Spins'].mean(),
        'SiriusXM': df['SiriusXM Spins'].mean(),
        'Pandora': df['Pandora Streams'].mean(),
        'Soundcloud': df['Soundcloud Streams'].mean(),
        'Shazam': df['Shazam Counts'].mean()
    }

    platform_avg_df = pd.DataFrame(list(platform_streams_avg.items()), columns=['Platform', 'Average Streams'])
    fig = px.bar(platform_avg_df, x='Platform', y='Average Streams', 
                 title='Average Streams per Platform',
                 labels={'Average Streams': 'Average Streams', 'Platform': 'Platform'},
                 color='Platform')

    return fig

def plot_platform_correlation_heatmap(df):
    platforms_streams = ['Spotify Streams', 'YouTube Views', 'TikTok Views', 
                         'AirPlay Spins', 'SiriusXM Spins', 'Pandora Streams', 
                         'Soundcloud Streams', 'Shazam Counts']

    # correlation matrix
    correlation_matrix = df[platforms_streams].corr()

    # heatmap
    fig = px.imshow(correlation_matrix, text_auto=True, 
                    title='Correlation Heatmap Between Platforms',
                    labels={'color': 'Correlation'})
    
    
    fig.update_layout(width=800, height=600)

    return fig

def plot_streams_vs_playlists(df):

    platforms_streams = ['Spotify Streams', 'YouTube Views', 'TikTok Views', 
                         'AirPlay Spins', 'SiriusXM Spins', 'Pandora Streams', 
                         'Soundcloud Streams', 'Shazam Counts']

    platforms_popularity = ['Spotify Playlist Count', 'Apple Music Playlist Count', 
                            'Deezer Playlist Count', 'Amazon Playlist Count', 'Pandora Track Stations']

    # Total streams and playlist counts for each track
    df['Total Streams'] = df[platforms_streams].sum(axis=1)
    df['Total Playlist Count'] = df[platforms_popularity].sum(axis=1)

    # Scatter plot of total streams vs total playlist counts
    fig = px.scatter(df, x='Total Playlist Count', y='Total Streams', 
                     title='Comparison of Total Streams vs Total Playlist Counts',
                     labels={'Total Playlist Count': 'Total Playlist Count', 'Total Streams': 'Total Streams'},
                     color='Artist', hover_data=['Track'])
    fig.update_layout(width=800, height=600)
    fig.update_layout(showlegend=False)

    return fig


def plot_spotify_vs_other_streams(df):
    platforms_other_streams = ['YouTube Views', 'TikTok Views', 
                               'AirPlay Spins', 'SiriusXM Spins', 
                               'Pandora Streams', 'Soundcloud Streams', 'Shazam Counts']
    
    df['Other Platforms Streams'] = df[platforms_other_streams].sum(axis=1)

    fig = px.scatter(df, x='Spotify Streams', y='Other Platforms Streams', color='Artist', 
                     hover_data=['Track'],
                     title='Spotify Streams vs. Other Platforms Streams',
                     labels={'Spotify Streams': 'Spotify Streams', 'Other Platforms Streams': 'Streams on Other Platforms'},
                     color_continuous_scale=px.colors.sequential.Bluered)

    fig.update_layout(width=800, height=600)
    fig.update_layout(showlegend=False)

    return fig

def plot_sunburst_streams(df, artist_name):
    platforms_streams = ['Spotify Streams', 'YouTube Views', 'TikTok Views',
                         'AirPlay Spins', 'SiriusXM Spins', 
                         'Pandora Streams', 'Soundcloud Streams', 'Shazam Counts']

    artist_data = df[df['Artist'] == artist_name][['Track', 'Artist'] + platforms_streams]
    artist_data_melted = artist_data.melt(id_vars=['Track'], value_vars=platforms_streams, 
                                          var_name='Platform', value_name='Streams')

    fig = px.sunburst(artist_data_melted, path=['Platform', 'Track'], values='Streams',
                      title=f'Streams Breakdown for {artist_name} Across Platforms',
                      color='Platform', 
                      color_discrete_sequence=px.colors.qualitative.Bold)
    
    fig.update_layout(width=800, height=600)
    
    return fig