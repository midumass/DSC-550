from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import plotly.figure_factory as ff
import numpy as np

#brdf = pd.read_csv('birth-rate.csv')
crdf = pd.read_csv('crimerates-by-state-2005.csv')
#brydf = pd.read_csv('birth-rates-yearly.csv')
#ledf = pd.read_csv('life-expectancy.csv')

crdf = crdf[crdf.state != 'United States']

# =============================================================================
# brmelt = pd.melt(brdf, id_vars=['Country'])
# brmelt = brmelt.rename(columns = {'Country':'country',
#                                   'variable':'year',
#                                   'value':'rate'})
# brmelt08 = brmelt[brmelt.year == '2008']
# 
# bm8l = list(brmelt08['country'].values) 
# 
# lebrdf = ledf[ledf['country'].isin(bm8l)]
# 
# lebrdf = pd.merge(lebrdf, brmelt08, on='country')\
# .drop(['year_x', 'year_y'], axis = 1)\
# .dropna()\
# .reset_index(drop = True)
# =============================================================================

# =============================================================================
# fig = px.scatter(lebrdf, x = 'expectancy', y = 'rate')
# 
# fig.update_layout(
#         title = go.layout.Title(
#                 text = 'Birth Rate vs. Life Expectancy in 2008',
#                 font = dict(
#                         size = 18,
#                         color = '#7F7F7F'),
#                 x = .5,
#                 xref = 'paper'),
#         xaxis = go.layout.XAxis(
#                 title = go.layout.xaxis.Title(
#                         text = 'Life Expectancy',
#                         font = dict(
#                                 size = 12,
#                                 color = '#7F7F7F'))),
#         yaxis = go.layout.YAxis(
#                 title = go.layout.yaxis.Title(
#                         text = 'Birth Rate',
#                         font = dict(
#                                 size = 12,
#                                 color = '#7F7F7F'))))
# 
# plot(fig)
# =============================================================================

# =============================================================================
# fig = px.scatter(crdf,
#                  x = 'murder',
#                  y = 'forcible_rape',
#                  color = 'population',
#                  size = 'population')
# 
# fig.update_layout(
#         title = go.layout.Title(
#                 text = 'Rape vs. Murder rates in the US by State',
#                 font = dict(
#                         size = 18,
#                         color = '#7F7F7F'),
#                 x = .5,
#                 xref = 'paper'),
#         xaxis = go.layout.XAxis(
#                 title = go.layout.xaxis.Title(
#                         text = 'Murder Rate',
#                         font = dict(
#                                 size = 12,
#                                 color = '#7F7F7F'))),
#         yaxis = go.layout.YAxis(
#                 title = go.layout.yaxis.Title(
#                         text = 'Rape',
#                         font = dict(
#                                 size = 12,
#                                 color = '#7F7F7F'))))
# 
# plot(fig)
# =============================================================================

#x1 = np.random.randn(200) - 1
#x2 = np.random.randn(200)
#x3 = np.random.randn(200) + 1
#
#hist_data = [x1, x2, x3]
#
#group_labels = ['Group 1', 'Group 2', 'Group 3']
#colors = ['#333F44', '#37AA9C', '#94F3E4']
#
# Create distplot with curve_type set to 'normal'
# fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

rates = pd.DataFrame({'murder':crdf['murder'], 
                      'rape':crdf['forcible_rape'], 
                      'robbery':crdf['robbery']})

fig = ff.create_distplot([rates[c] for c in rates.columns], 
                         rates.columns, 
                         show_hist = False)

fig.update_layout(title_text='Density of rape, murder and robbery')
plot(fig)
 

# =============================================================================
# df = pd.DataFrame({'2012': np.random.randn(200),
#                    '2013': np.random.randn(200)+1})
# fig = ff.create_distplot([df[c] for c in df.columns], df.columns, bin_size=.25)
# plot(fig)
# =============================================================================
