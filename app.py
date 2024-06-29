import streamlit as st
import streamlit_antd_components as sac
from modules.apple import Apple
from modules.google import Android, Finance
from modules.samsung import Samsung


st.set_page_config(
    page_title="Antd components in Streamlit",
    layout='centered',
    page_icon='🤷'
)


def Home():
    st.header('Antd components in Streamlit')

    st.markdown('''A streamlit application that uses antd components.''')


with st.sidebar:
    menu_item = sac.menu(
        index=0,  # refers to the Home
        open_all=False,
        items=[
            sac.MenuItem('Home', icon='house-fill'),

            sac.MenuItem(
                'Products',
                icon='box-fill',
                children=[
                    sac.MenuItem('Apple', icon='apple'),

                    sac.MenuItem(
                        'Google',
                        icon='google',
                        children=[
                            sac.MenuItem('Android', icon='android2'),
                            sac.MenuItem('Finance', icon='bank'),
                        ],
                    ),

                    sac.MenuItem('Samsung', icon='phone-flip'),
                ]
            ),
        ],        
    )

match menu_item:
    case 'Home':
        Home()

    case 'Apple':
        Apple()
    
    case 'Android':
        Android()
    
    case 'Finance':
        Finance()

    case 'Samsung':
        Samsung()
