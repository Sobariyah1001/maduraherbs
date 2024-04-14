import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Dashboard", 'Data', 'Method', 'Forecast'], 
        icons=['house', 'files','calculator','code'], menu_icon="cast", default_index=0)
    selected

# Manual item selection
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None

# Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")

# Add CSS directly to the body element
st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(to bottom right, #ff0099, #493240);
        background-size: cover;
        height: 100vh;
        margin: 0;
        padding: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add your content
st.write("haaaaaiiii")
