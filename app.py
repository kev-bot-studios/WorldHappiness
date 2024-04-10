# Standard Imports
import pandas as pd
from dash import Dash, html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output



###################################
### Load Data and Get Variables ###
###################################

data_dir = '''/Users/kevincory/Documents/Graduate Classes/\
6289 - DB Mgmt Using Python/Project/Analysis/'''
data_fname = 'happiness_regression_data.csv'
df = pd.read_csv(data_dir + data_fname, index_col = 0)
df = df.rename(columns = {'HappinessIndex': 'Happiness Score'})
country_options = df.Country.unique()
reg_features = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
pivot_features = reg_features + ['Country', 'Year', 'Happiness Score']
df1 =  df[pivot_features].melt(id_vars = ['Country', 'Year']).copy()
decomp_features = ['Economy_contribution', 'Family_contribution', 'Health_contribution', 'Freedom_contribution',
                   'Trust_contribution', 'Generosity_contribution', 'Resid']
pivot_features2 = decomp_features + ['Country', 'Year']
df2 =  df[pivot_features2].melt(id_vars = ['Country', 'Year']).copy()
df3 = df.groupby(['Year', 'Region']).agg({'Happiness Score': 'mean'}).reset_index().copy()
min_year = df['Year'].min()
max_year = df['Year'].max()


app = Dash(__name__)

colors = {
    'background': "#F4BB44",
    'background2': '#FFE033',
    'background3': '#FF33BB',
    'text': '#000000',
    'chart': "#42C4F7",
    'text2': '#fff'
}


color_map_scores = {'Economy_contribution': 'rgb(246,215,70)',
                    'Family_contribution': 'rgb(235,150,60)',
                    'Health_contribution': 'rgb(229,92,48)',
                    'Freedom_contribution': 'rgb(170,60,70)',
                    'Trust_contribution': 'rgb(132,32,107)',
                    'Generosity_contribution': 'rgb(188,23,125)',
                    'Resid': 'rgb(151,29,120)'}

color_map_line = {'Economy': 'rgb(246,215,70)',
                  'Family': 'rgb(235,150,60)',
                  'Health': 'rgb(229,92,48)',
                  'Freedom': 'rgb(170,60,70)',
                  'Trust': 'rgb(132,32,107)',
                  'Generosity': 'rgb(188,23,125)',
                  'Happiness Score': 'rgb(151,29,120)'}

color_scatter = {'Australia And New Zealand': 'rgb(246,215,70)',
                 'North America': 'rgb(235,150,60)',
                 'Western Europe': 'rgb(229,92,48)',
                 'Latin America And Caribbean': 'rgb(170,60,70)',
                 'Eastern Asia': 'rgb(132,32,107)',
                 'Middle East And Northern Africa': 'rgb(188,23,125)',
                 'Southeastern Asia': 'rgb(151,29,120)',
                 'Central And Eastern Europe': 'rgb(131,25,100)',
                 'Southern Asia': 'rgb(70,15,70)',
                 'Sub-Saharan Africa': 'rgb(20,11,52)'}

##################
### App Layout ###
##################

fig1 = px.choropleth(df[['Country', 'Happiness Score']], 
                    locations = 'Country', color='Happiness Score',
                    locationmode='country names',
                    hover_name = 'Country',
                    title = '<b>Happiness Scores Around the World<b>')

fig2 = px.bar(df1, x='Year', y='value', color='variable', title = '<b>Happiness Score Over Time<b>',
               labels={'value':'Score'}, color_discrete_map=color_map_line, barmode='group')

fig3 = px.bar(df2, x="Year", y="value", color="variable", title="<b>Happiness Score Decomposition<b>",
              labels={'value':'Contribution to Score'}, color_discrete_map=color_map_scores)

fig4 = px.scatter(df, x = 'Economy', y = 'Happiness Score', color = 'Region',
                  size = 'Health', color_discrete_map = color_scatter,
                  hover_name = 'Country')

fig5 = px.bar(df3, x = 'Year', y = 'Happiness Score', title = '<b>Happiness Score Over Time by Region<b>',
              color ='Region', color_discrete_map = color_scatter, barmode = 'group')


fig1.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])
fig2.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])
fig3.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])
fig4.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])
fig5.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        
    html.Div(
        
    html.H1(
        children='World Happiness',
        style={
            'textAlign': 'center',
            'color': colors['text'],
        }), style = {'display':'inline-block','width':'100%','textAlign':'center', 'vertical-align':'bottom',
                     "margin-bottom": "0px"}),

    
    
    html.Div(
    
    html.H4(
        children='Trends in global happiness, and it\'s driving factors', 
         style= {'textAlign': 'center',
                 'color': colors['text'],
        }), style = {'display':'inline-block','width':'100%','textAlign':'center', 'vertical-align':'bottom'}),
    
    html.Div(children = [
     
    html.Div(children = [
        
    html.Div(children='''The World Happiness Report is an annual publication that ranks countries by their happiness levels and 
                         explores the factors that contribute to well-being. It is produced by the United Nations Sustainable Development 
                         Solutions Network (SDSN) and first launched in 2012. The report assesses global happiness by using data from 
                         various sources, including surveys, to measure subjective well-being, life satisfaction, and other related factors.
                         The average of happiness scores by geographical regions over time is shown to the right.
                         ''',
             style= {'textAlign': 'left',
                 'color': colors['text'],
                 'margin-bottom': '10px'}),                        
                         
                        
    html.Div(children='''This analysis leverages World Happiness data from 2015 - 2019. First, we can observe global trends in happiness
                         via the choropleth map that shows happiness scores across the world for a particular year, which can be controlled
                         by the slider. The scatter plot provides a deeper dive into the factors contributing to happiness scores, which
                         according to our regression model are primarily Economic Growth (x-axis) and Life Expectancy (size of bubbles).
                         ''',
                         style= {'textAlign': 'left',
                             'color': colors['text'],
                             'margin-bottom': '10px'}),     
                         
    html.Div(children='''In the second set of charts, we can deep dive into the Happiness Score trends for a particular country over time,
                         controlling the selected country with the dropdown menu. The line chart on the right shows the overall happiness scores,
                         along with additionally surveyed factors (Economy (GDP per Capita), Family, Health (Life Expectancy), Freedom, Generosity, 
                         Trust (Government Corruption)]. These factors are used to build a regression model, which we then use to decompose
                         the factor influence on a country's happiness score over time in the stacked bar chart.
                         
                         ''',
             style= {'textAlign': 'left',
                 'color': colors['text']}),
                                                                   
    ], style = {'width': '50%', 'margin-left': '10px', 'margin-top': '125px'}),
                                                                   
    html.Div(
        dcc.Graph(
            id='region_graph2',
            figure=fig5
        ), style ={'width': '50%'}),    
    
                                                                   
    ], style = {'display': 'flex', 'justify-content': 'space-between'}),
    
    html.Label('Choose Year', style = {'color':colors['text']}),
        dcc.Slider(
            df['Year'].min(),
            df['Year'].max(),
            step=None,
            value=df['Year'].min(),
            marks={str(year): str(year) for year in df['Year'].unique()},
            id='year_select'
        ),
    
    
    html.Div(children = [
    
        html.Div(
            dcc.Graph(
                id='country_graph1',
                figure=fig1
            ), style ={'width': '50%','display': 'inline-block'}),
        
        
        html.Div(
            dcc.Graph(
                id='region_graph1',
                figure=fig4,
            ), style ={'width': '50%','display': 'inline-block'}),
        
        html.Label('Choose Country', style = {'color':colors['text']}),
            dcc.Dropdown(
                id = 'country_select',
                options= country_options,
                value='United States',
        ),    
        
    
    ]),
    
    html.Div(children = [

        html.Div(
            dcc.Graph(
                id='country_graph2',
                figure=fig2
            ), style ={'width': '50%','display': 'inline-block'}),
        
        html.Div(
            dcc.Graph(
                id = 'country_graph3',
                figure=fig3
            ), style = {'width': '50%','display': 'inline-block'}), 
    
    ]),

])


#####################
### App Responses ###
#####################

@app.callback(
    Output('country_graph1', 'figure'),
    Output('region_graph1', 'figure'),
    Input('year_select', 'value'))

def update_map_graph(year):
    
    df_year = df[df['Year'] == year].copy()
    fig1 = px.choropleth(df_year[['Country', 'Happiness Score']], 
                    locations = 'Country', color='Happiness Score',
                    locationmode='country names',
                    hover_name="Country", 
                    title = f'<b>Happiness Scores Around the World in {year}<b>')
    
    fig4 = px.scatter(df_year, x = 'Economy', y = 'Happiness Score', color = 'Region',
                      size = 'Health', labels = {'Economy': 'Economy (Economic Production)'},
                      color_discrete_map= color_scatter, hover_name = 'Country')

    fig1.update_layout(title = f'<b>Happiness Scores Around the World in {year}<b>', 
                       plot_bgcolor=colors['background'], 
                       paper_bgcolor=colors['background'], 
                       font_color = colors['text'])

    fig4.update_layout(title = f'<b>Happiness Scores vs Economy (Economic Production) and Health (Life Expectancy) in {year}<b>', 
                       plot_bgcolor=colors['background'], 
                       paper_bgcolor=colors['background'], 
                       font_color = colors['text'])
    
    return fig1, fig4


@app.callback(
    Output('country_graph2', 'figure'),
    Output('country_graph3', 'figure'),
    Input('country_select', 'value'))


def update_country_graph(country):
    
    df1_country = df1[df1['Country'] == country].copy()
    df2_country = df2[df2['Country'] == country].copy()
    fig2 = px.bar(df1_country, x='Year', y='value', color='variable', title = f'<b>Happiness Score over Time [{country}]<b>',
                   labels={'value':'Score'}, color_discrete_map=color_map_line, barmode='group')
    fig3 = px.bar(df2_country, x="Year", y="value", color="variable", title= f'<b>Happiness Score Decomposition [{country}]<b>',
                  labels={'value':'Contribution to Score'},  color_discrete_map=color_map_scores)
    
    fig2.update_layout(title = f'<b>Happiness Scores over Time [{country}]<b>', 
                       plot_bgcolor=colors['background'], 
                       paper_bgcolor=colors['background'], font_color = colors['text'], 
                       legend_title_text = 'Factor')
    
    fig3.update_layout(title = f'<b>Happiness Scores Decomposition [{country}]<b>', 
                       plot_bgcolor=colors['background'], 
                       paper_bgcolor=colors['background'], font_color = colors['text'], 
                       legend_title_text = 'Factor')
    
    return fig2, fig3


################
### App Main ###
################

if __name__ == '__main__':
    app.run(debug=True)

