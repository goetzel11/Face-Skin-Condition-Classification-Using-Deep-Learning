import streamlit as st
import EDA, PREDICT

with st.sidebar:
    st.title('Page Navigation')
    page = st.selectbox('Pilih Halaman',
                        ['EDA', 'PREDICT'])
    
if page == 'EDA':
    EDA.run()
else:
    PREDICT.run()