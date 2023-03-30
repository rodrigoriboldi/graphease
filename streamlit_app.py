##################################################
# GRAPHEASE
# MADE WITH LOVE BY RODRIGO MARTINI RIBOLDI
##################################################


import streamlit as st

from sklearn import datasets
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

st.header('GraphEase')
st.write('A simple Python graph builder tool')
st.write('')
st.write('')

##################################################
# SIDEBAR CONFIGURATION 
##################################################
graph_type = st.sidebar.selectbox("Select Graph Type",
                                  ('scatter', 'barplot', 'linechart'))


##################################################
# READ DATA
##################################################

df = pd.DataFrame()

try:
    uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
    uploaded_df = pd.read_csv(uploaded_file, sep = ';')

    df = df.append(uploaded_df)

except:
    if df.empty:
        st.write('No dataset was been uploaded. Using sample "tips" dataset.')
        df = sns.load_dataset("tips")


df_columns = df.columns


##################################################
# TABS
##################################################
tab1, tab2, tab3, tab4 = st.tabs(["Basic", "Title and captions", "Axes", "Colors"])


##############################
# Basic plot objects tab
##############################
with tab1:
    st.header('Basic plot objects')
    
    
    X = st.selectbox('X axis',
                     df_columns)
    
    Y = st.selectbox('Y axis',
                     df_columns,
                     index = 1)
    
    
    enable_color = st.checkbox('Enable colors',
                                value = False)
    
    
    if enable_color == True:
        color = st.selectbox('Color',
                             df_columns,
                             index = 2)
        
        
    advanced_mode = st.checkbox('Enable advanced mode',
                                value = False)    
    st.caption('Advanced mode will disable the options below and enable more customizable options.')
    
    
    if advanced_mode == False:
    
        title_simple = st.text_input('Set title')

        col1, col2 = st.columns(2)
        with col1:    
            style = st.selectbox('Graph style',
                                 ('white', 'whitegrid', 'dark', 'darkgrid'))

        with col2:
            context = st.selectbox('Graph context',
                                   ('notebook', 'paper', 'poster', 'talk'))
    
    else:
        st.empty()
        
    
    
##############################
# Title and labels
##############################
with tab2:
    st.header('Titles and labels config')
    st.empty()
    
    with st.expander('Title config'):
    
        title = st.text_input('Title')

        col1, col2 = st.columns(2)
        with col1:
            title_size = st.number_input('Title size',
                                         value = 36)

            title_fontweight = st.selectbox('Title fontweight',
                                            ('normal', 'bold', 'heavy', 'light', 'ultralight'))

            title_horizontalalignment = st.selectbox('Title horizontal alignment',
                                                     ('center', 'right', 'left'))

            title_color = st.text_input('Title color',
                                        value = 'black')
            
            title_position_x = st.number_input('Title position X',
                                               value = 0.5,
                                               min_value = -1.00,
                                               max_value = 2.00)
            
            title_rotation = st.text_input('Title rotation',
                                           value = '0')
            title_rotation = int(title_rotation)

        with col2:
            title_font_family = st.selectbox('Title font family',
                                             ('sans-serif', 'serif', 'cursive', 'fantasy', 'monospace'))

            title_fontstyle = st.selectbox('Title fontstyle',
                                           ('normal', 'italic', 'oblique'))


            title_verticalalignment = st.selectbox('Title vertical alignment',
                                                   ('center', 'top', 'bottom', 'baseline'))
            
            title_alpha = st.number_input('Title transparency',
                                          value = 1.00,
                                          min_value = 0.00,
                                          max_value = 1.00,
                                          step = 0.01)
            
            title_position_y = st.number_input('Title position Y',
                                               value = 1.05,
                                               min_value = -2.00,
                                               max_value = 2.00)
            
            title_pad = st.number_input('Title pad',
                                        value = 0,
                                        min_value = -100,
                                        max_value = 100)
    
    with st.expander('Legend config'):
        enable_legend_config = st.checkbox('Enable legend config',
                                           value = False)
        
        if enable_legend_config == True:
            col1, col2 = st.columns(2)
            with col1:
                legend_title = st.text_input('Legend title',
                                             value = '')
                
                legend_outside = st.checkbox('Legend outside plot',
                                             value = False)
        
            with col2:
                legend_location = st.selectbox('Legend location',
                                               ('best', 'upper right', 'upper left', 'lower left',
                                                'lower right', 'right', 'center left',
                                                'center right', 'lower center', 'upper center',
                                                'center'))
        
        

##############################
# Axes config
##############################
with tab3:
    st.header('Axes config')
    st.empty()
    
    with st.expander('X labels config'):
        
        x_label = st.text_input('X label',
                                value = X)
        
        col1, col2 = st.columns(2)
        with col1:
            x_label_size = st.number_input('X label size',
                                           value = 24)

            x_label_fontweight = st.selectbox('X label fontweight',
                                            ('normal', 'bold', 'heavy', 'light', 'ultralight'))

            x_label_horizontalalignment = st.selectbox('X label horizontal alignment',
                                                     ('center', 'right', 'left'))

            x_label_color = st.text_input('X label Color',
                                        value = 'black')
            
            x_label_position_x = st.number_input('X label position X',
                                               value = 0.5,
                                               min_value = -2.00,
                                               max_value = 2.00)            
            

        with col2:
            x_label_font_family = st.selectbox('X label font family',
                                             ('sans-serif', 'serif', 'cursive', 'fantasy', 'monospace'))

            x_label_fontstyle = st.selectbox('X label fontstyle',
                                           ('normal', 'italic', 'oblique'))


            x_label_verticalalignment = st.selectbox('X label vertical alignment',
                                                   ('center', 'top', 'bottom', 'baseline'),
                                                    index = 1)
            
            x_label_alpha = st.number_input('X label transparency',
                                            value = 1.00,
                                            min_value = 0.00,
                                            max_value = 1.00,
                                            step = 0.01)
            
            x_label_rotation = st.text_input('X label rotation',
                                           value = '0')
            x_label_rotation = int(x_label_rotation)
    
    with st.expander('X ticks config'):
    
        col1, col2 = st.columns(2)
        with col1:
            x_ticks_size = st.number_input('X ticks size',
                                               value = 16)

            x_ticks_fontweight = st.selectbox('X ticks fontweight',
                                              ('normal', 'bold', 'heavy', 'light', 'ultralight'))

            x_ticks_color = st.text_input('X ticks Color',
                                          value = 'black')
            
            x_low_limit = st.number_input('X lower limit value',
                                          value = 0)            
                                   
            
            x_high_limit = st.number_input('X higher limit value',
                                           value = 0)            
            st.caption('Set both values to 0 to disable')


        with col2:
            x_ticks_rotation = st.text_input('X ticks rotation',
                                             value = '0')
            x_ticks_rotation = int(x_ticks_rotation)


            x_ticks_font_family = st.selectbox('X ticks font family',
                                               ('sans-serif', 'serif', 'cursive', 'fantasy', 'monospace'))

            x_ticks_fontstyle = st.selectbox('X ticks fontstyle',
                                             ('normal', 'italic', 'oblique'))
            
            x_ticks_alpha = st.number_input('X ticks transparency',
                                            value = 1.00,
                                            min_value = 0.00,
                                            max_value = 1.00,
                                            step = 0.01)
            
    with st.expander('Y labels config'):

        y_label = st.text_input('Y label',
                                value = Y)
        
        col1, col2 = st.columns(2)
        with col1:
            y_label_size = st.number_input('Y label size',
                                           value = 24)

            y_label_fontweight = st.selectbox('Y label fontweight',
                                            ('normal', 'bold', 'heavy', 'light', 'ultralight'))

            y_label_horizontalalignment = st.selectbox('Y label horizontal alignment',
                                                     ('center', 'right', 'left'))

            y_label_color = st.text_input('Y label Color',
                                        value = 'black')
            
            y_label_position_y = st.number_input('Y label position y',
                                               value = 0.5,
                                               min_value = -2.00,
                                               max_value = 2.00)

        with col2:
            y_label_font_family = st.selectbox('Y label font family',
                                             ('sans-serif', 'serif', 'cursive', 'fantasy', 'monospace'))

            y_label_fontstyle = st.selectbox('Y label fontstyle',
                                           ('normal', 'italic', 'oblique'))


            y_label_verticalalignment = st.selectbox('Y label vertical alignment',
                                                   ('center', 'top', 'bottom', 'baseline'),
                                                     index = 2)
            
            y_label_alpha = st.number_input('Y label transparency',
                                            value = 1.00,
                                            min_value = 0.00,
                                            max_value = 1.00,
                                            step = 0.01)
            
            y_label_rotation = st.text_input('Y label rotation',
                                           value = '90')
            y_label_rotation = int(y_label_rotation)
            
            
    with st.expander('Y ticks config'):
    
        col1, col2 = st.columns(2)
        with col1:
            y_ticks_size = st.number_input('Y ticks size',
                                               value = 16)

            y_ticks_fontweight = st.selectbox('Y ticks fontweight',
                                              ('normal', 'bold', 'heavy', 'light', 'ultralight'))

            y_ticks_color = st.text_input('Y ticks Color',
                                          value = 'black')
            
            y_low_limit = st.number_input('Y lower limit value',
                                          value = 0)            
                                   
            
            y_high_limit = st.number_input('Y higher limit value',
                                           value = 0)            
            st.caption('Set both values to 0 to disable')           



        with col2:
            y_ticks_rotation = st.text_input('Y ticks rotation',
                                             value = '90')
            y_ticks_rotation = int(x_ticks_rotation)


            y_ticks_font_family = st.selectbox('Y ticks font family',
                                               ('sans-serif', 'serif', 'cursive', 'fantasy', 'monospace'))

            y_ticks_fontstyle = st.selectbox('Y ticks fontstyle',
                                             ('normal', 'italic', 'oblique'))
            
            y_ticks_alpha = st.number_input('Y ticks transparency',
                                            value = 1.00,
                                            min_value = 0.00,
                                            max_value = 1.00,
                                            step = 0.01)
            
            

##############################
# Graph colors
##############################
with tab4:
    st.header('Color config')
    st.empty()
    
    with st.expander('Background and face config'):
    
        graph_backgroud = st.text_input('Background color',
                                        value = 'white')
        graph_facecolor = st.text_input('Face color',
                                        value = 'white')
        
    
    with st.expander('Grid config'):
        
        graph_grid = st.selectbox('Enable grid',
                                  (False, True))
        
        if graph_grid == True:
        
            col1, col2 = st.columns(2)
            with col1:

                grid_axis = st.selectbox('Grid axis',
                                         ('both', 'x', 'y'))

                grid_linestyle = st.selectbox('Grid linestyle',
                                              ('-', '--', '-.', ':', ''))

                grid_alpha = st.number_input('Grid alpha',
                                             value = 1.00,
                                             min_value = 0.00,
                                             max_value = 1.00,
                                             step = 0.01)

            with col2:

                grid_which = st.selectbox('Grid style',
                                         ('major', 'minor', 'both'))

                grid_color = st.text_input('Face color',
                                           value = 'gray')

                grid_linewidth = st.number_input('Grid linewidth',
                                                 value = 1.00,
                                                 min_value = 0.01,
                                                 max_value = 100.00,
                                                 step = 0.01)
            
##################################################
# PLOT CREATION
##################################################            
fig = plt.figure(figsize=(16, 9))

if advanced_mode == False:
    sns.set_style(style)
    sns.set_context(context)

    
if enable_color == False:
    color = None
    


if graph_type == 'scatter':
    ax = sns.scatterplot(data=df,
                         x=X,
                         y=Y,
                         hue = color, legend = True)

elif graph_type == 'barplot':
    ax = sns.barplot(data=df,
                     x=X,
                     y=Y,
                     hue = color)

elif graph_type == 'linechart':
    ax = sns.lineplot(data=df,
                      x=X,
                      y=Y,
                      hue = color)

if advanced_mode == False:
    ax.set_title(title_simple)    
else:

    ax.set_title(title,
                 fontsize = title_size,
                 fontweight = title_fontweight,
                 ha = title_horizontalalignment,
                 va = title_verticalalignment,
                 family = title_font_family,
                 style = title_fontstyle,
                 color = title_color,
                 alpha = title_alpha,
                 x = title_position_x,
                 y = title_position_y,
                 pad = title_pad,
                 rotation = title_rotation)


    ax.set_xlabel(x_label,
                  fontsize = x_label_size,
                  fontweight = x_label_fontweight,
                  ha = x_label_horizontalalignment,
                  va = x_label_verticalalignment,
                  family = x_label_font_family,
                  style = x_label_fontstyle,
                  color = x_label_color,
                  alpha = x_label_alpha,
                  x = x_label_position_x,
                  rotation = x_label_rotation)

    plt.xticks(fontsize = x_ticks_size,
               fontweight = x_ticks_fontweight,
               rotation = x_ticks_rotation,
               family = x_ticks_font_family,
               color = x_ticks_color,
               alpha = x_ticks_alpha,
               style = x_ticks_fontstyle)

    if (x_low_limit != 0) | (x_high_limit != 0):
        plt.xlim(x_low_limit, x_high_limit)


    ax.set_ylabel(y_label,
                  fontsize = y_label_size,
                  fontweight = y_label_fontweight,
                  ha = y_label_horizontalalignment,
                  va = y_label_verticalalignment,
                  family = y_label_font_family,
                  style = y_label_fontstyle,
                  color = y_label_color,
                  alpha = y_label_alpha,
                  y = y_label_position_y,
                  rotation = y_label_rotation)

    plt.yticks(fontsize = y_ticks_size,
               fontweight = y_ticks_fontweight,
               rotation = y_ticks_rotation,
               family = y_ticks_font_family,
               color = y_ticks_color,
               alpha = y_ticks_alpha,
               style = y_ticks_fontstyle)


    if (y_low_limit != 0) | (y_high_limit != 0):
        plt.ylim(y_low_limit, y_high_limit)


    ax.set_facecolor(graph_facecolor)
    fig.set_facecolor(graph_backgroud)

    if graph_grid == True:
        plt.grid(visible = graph_grid,
                 which = grid_which,
                 axis = grid_axis,
                 color = grid_color,
                 linestyle = grid_linestyle,
                 linewidth = grid_linewidth,
                 alpha = grid_alpha)
    else:
        plt.grid(0)


if enable_legend_config == True:
    if legend_outside == True:
        plt.legend(title = legend_title,
                   loc = legend_location,
                   bbox_to_anchor=(1, 1))
    else:
        plt.legend(title = legend_title,
                   loc = legend_location)

           

st.header('')
st.pyplot(fig)
st.header('')
st.header('')
st.header('')


st.write('Made with 🧡 on Streamlit by Rodrigo Martini Riboldi')
