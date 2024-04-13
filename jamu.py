import streamlit as st

# Fungsi untuk membuat menu di bagian atas
def top_menu():
    st.sidebar.title("Menu")

    selected_menu = st.sidebar.selectbox("Select Menu", ["Menu 1", "Menu 2"])

    if selected_menu == "Menu 1":
        menu_1()
    elif selected_menu == "Menu 2":
        menu_2()

# Fungsi untuk menu 1
def menu_1():
    st.markdown("### Menu 1")
    st.markdown("- [Home](#Home)")
    st.markdown("- [About](#About)")
    st.markdown("- [Contact](#Contact)")

# Fungsi untuk menu 2
def menu_2():
    st.markdown("### Menu 2")
    st.markdown("- [FAQ](#FAQ)")
    st.markdown("- [Services](#Services)")
    st.markdown("- [Blog](#Blog)")

# Fungsi untuk halaman Home
def home():
    st.title("Home")
    st.write("Welcome to the Home Page")

# Fungsi untuk halaman About
def about():
    st.title("About")
    st.write("This is the About Page")

# Fungsi untuk halaman Contact
def contact():
    st.title("Contact")
    st.write("Contact us at example@example.com")

# Tampilan utama
def main():
    st.sidebar.title("Jamu Madura")

    top_menu()  # Menampilkan menu di bagian atas

    # Content
    st.title("Main Content")  # Judul konten utama

    menu = """
    ### Home
    [About](#About)
    [Contact](#Contact)
    """
    st.markdown(menu, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
