import streamlit as st
import streamlit_antd_components as sac
from modules.apple import Apple
from modules.google import Android, Finance
from modules.samsung import Samsung
from modules.account import Account
from modules.version import __version__


st.set_page_config(
    page_title="Antd components in Streamlit",
    layout='centered',
    page_icon='🤷',
    menu_items={
        'about': f'''**A sample streamlit App that uses Antd components.**  
        *Version {__version__}*'''
    }
)


def Home():
    st.header('Antd components in Streamlit')

    st.markdown('''A streamlit application that uses antd components.''')


def main():
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

                sac.MenuItem('Account', icon='credit-card-2-front-fill'),

            ],        
        )


    menu_actions = {
        'Home': Home,
        'Apple': Apple,
        'Android': Android,
        'Finance': Finance,
        'Samsung': Samsung,
        'Account': Account
    }

    if menu_item in menu_actions:
        menu_actions[menu_item]()


if __name__ == '__main__':
    main()

