# StreamlitApp
import streamlit as st

def main():
    st.title("Streamlit Cheat Sheet")

    # Section: Text and Titles
    st.header("Text and Titles")
    st.write("Streamlit provides various commands for displaying text and titles:")
    st.code("st.title('Title')")
    st.code("st.header('Header')")
    st.code("st.subheader('Subheader')")
    st.code("st.write('Text')")
    
    # Section: Markdown
    st.header("Markdown")
    st.write("You can use Markdown for rich text formatting:")
    st.code("st.markdown('**Bold** *Italic* [Link](https://www.example.com)')")
    
    # Section: Data Display
    st.header("Data Display")
    st.write("Commands for displaying data:")
    st.code("st.dataframe(data)")
    st.code("st.table(data)")
    st.code("st.json(data)")
    
    # Section: Interactive Widgets
    st.header("Interactive Widgets")
    st.write("Streamlit allows you to create interactive widgets:")
    st.code("st.text_input('Enter text:', 'Default Value')")
    st.code("st.selectbox('Select option:', ['Option 1', 'Option 2', 'Option 3'])")
    st.code("st.slider('Select a value:', 0, 100, 50)")
    
    # Section: Buttons
    st.header("Buttons")
    st.write("Create buttons with st.button:")
    st.code("if st.button('Click me'):")
    st.code("    st.write('Button clicked!')")

    # Section: Progress Bar
    st.header("Progress Bar")
    st.write("Display a progress bar:")
    st.code("progress_bar = st.progress(0)")
    st.code("for i in range(100):")
    st.code("    progress_bar.progress(i + 1)")

if __name__ == "__main__":
    main()

