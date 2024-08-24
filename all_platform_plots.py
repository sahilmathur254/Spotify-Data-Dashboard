import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd

#use Spotify Streams, YouTube Views, TikTok Views, Deezer Streams, Pandora Streams, Soundcloud Streams
def plot_histogram(df, column):
    fig = px.histogram(df, x=column, title='Distribution of ' + column + ' Streams')
    fig.update_layout(width=800, height=400)
    fig.update_xaxes(title=column)
    fig.update_yaxes(title='Count')
    return fig


#use Spotify Streams, YouTube Views, TikTok Views, Deezer Streams, Pandora Streams, Soundcloud Streams
def plot_top_songs_by_platform(df, platforms_streams):
    df_top10 = df.sort_values(by=platforms_streams, ascending=False).head(10)
    fig = px.bar(df_top10, x='Track', y=platforms_streams, title=f'Top songs by {platforms_streams}',color='Track', color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_layout(width=750, height=450)
    fig.update_xaxes(title='Song Name')
    fig.update_yaxes(title=f'Number of {platforms_streams}')
    fig.update_traces(hovertemplate=f'Number of {platforms_streams}: %{{y}}')
    fig.update_layout(showlegend=False)
    return fig

#Spotify
def plot_popularity_vs_streams(df):
    fig = px.scatter(
        df, 
        x='Spotify Popularity', 
        y='Spotify Streams', 
        title='Spotify Popularity vs. Streams',
        hover_data={
            'Track': True, 
            'Artist': True, 
            'Spotify Popularity': True, 
            'Spotify Streams': True
        }
    )
    
    fig.update_xaxes(title='Spotify Popularity')
    fig.update_yaxes(title='Spotify Streams')
    
    return fig


def spotify_streams_over_time(df):
    df['Year'] = pd.DatetimeIndex(df['Release Date']).year

    yearly_streams = df.groupby('Year')['Spotify Streams'].sum().reset_index()

    bar_trace = go.Bar(
        x=yearly_streams['Year'], 
        y=yearly_streams['Spotify Streams'], 
        name='Yearly Streams', 
        marker=dict(color='lightblue'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Streams:</b> %{y}<extra></extra>'
    )
    line_trace = go.Scatter(
        x=yearly_streams['Year'], 
        y=yearly_streams['Spotify Streams'], 
        mode='lines+markers', 
        name='Stream Growth Over Time',
        line=dict(color='darkblue'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Streams:</b> %{y}<extra></extra>'
    )

    fig = go.Figure(data=[bar_trace, line_trace])

    fig.update_layout(
        title='Spotify Yearly Stream Growth & Stream Trends Over Time',
        xaxis_title='Year',
        yaxis_title='Spotify Streams',
        width=800,
        height=500
    )
    fig.update_layout(showlegend=False)
    fig.update_layout(width=750, height=450)

    return fig

#YouTube

def plot_yearly_stream_growth_youtube(df):
    df['Year'] = pd.DatetimeIndex(df['Release Date']).year

    yearly_streams = df.groupby('Year')['YouTube Views'].sum().reset_index()

    bar_trace = go.Bar(
        x=yearly_streams['Year'], 
        y=yearly_streams['YouTube Views'], 
        name='Yearly Streams', 
        marker=dict(color='lightblue'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Streams:</b> %{y}<extra></extra>'
    )

    line_trace = go.Scatter(
        x=yearly_streams['Year'], 
        y=yearly_streams['YouTube Views'], 
        mode='lines+markers', 
        name='Stream Growth Over Time',
        line=dict(color='darkblue'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Streams:</b> %{y}<extra></extra>'
    )

    fig = go.Figure(data=[bar_trace, line_trace])

    fig.update_layout(
        title='YouTube Yearly Stream Growth & Stream Trends Over Time',
        xaxis_title='Year',
        yaxis_title='YouTube Views',
        width=800,
        height=500
    )
    fig.update_layout(showlegend=False)
    fig.update_layout(width=750, height=450)

    return fig


#TikTok

def plot_tiktok_correlation_heatmap(df):
    tiktok_metrics = df[['TikTok Views', 'TikTok Likes', 'TikTok Posts']]
    corr_matrix = tiktok_metrics.corr()

    fig = px.imshow(corr_matrix, text_auto=True, 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Correlation Heatmap of TikTok Metrics')
    #fig.update_layout(width=800, height=600)
    return fig


#Apple

def plot_apple_music_correlation_heatmap(df):
    apple_music_metrics = df[['Apple Music Playlist Count', 'AirPlay Spins', 'Shazam Counts']]
    corr_matrix = apple_music_metrics.corr()

    fig = px.imshow(corr_matrix, text_auto=True, 
                    color_continuous_scale=px.colors.sequential.Blues,
                    title='Correlation Heatmap of Apple Music Metrics')

    return fig


def plot_yearly_stream_growth_apple(df):
    df['Year'] = pd.DatetimeIndex(df['Release Date']).year

    yearly_streams = df.groupby('Year')['AirPlay Spins'].sum().reset_index()

    bar_trace = go.Bar(
        x=yearly_streams['Year'], 
        y=yearly_streams['AirPlay Spins'], 
        name='Yearly Streams', 
        marker=dict(color='lightblue'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Streams:</b> %{y}<extra></extra>'
    )

    line_trace = go.Scatter(
        x=yearly_streams['Year'], 
        y=yearly_streams['AirPlay Spins'], 
        mode='lines+markers', 
        name='Stream Growth Over Time',
        line=dict(color='darkblue'),
        hovertemplate='<b>Year:</b> %{x}<br><b>Streams:</b> %{y}<extra></extra>'
    )

    fig = go.Figure(data=[bar_trace, line_trace])

    fig.update_layout(
        title='Apple/AirPlay Yearly Stream Growth & Stream Trends Over Time',
        xaxis_title='Year',
        yaxis_title='AirPlay Spins',
        width=800,
        height=500
    )
    fig.update_layout(showlegend=False)
    fig.update_layout(width=750, height=450)

    return fig