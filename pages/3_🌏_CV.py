import streamlit as st 
from constant import *
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(page_title="CV", page_icon="🌏",initial_sidebar_state="collapsed",layout="wide") #
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()
    
    st.header("🌏 Curriculum Vitae", divider='rainbow')

    # PDF 파일 경로 확인
    pdf_path = "src/resume.pdf"
    if not os.path.exists(pdf_path):
        st.error("PDF 파일이 존재하지 않습니다. 경로를 확인하세요.")
    else:
        # PDF 파일을 base64로 인코딩하여 표시
        def show_pdf(file_path):
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        # PDF 파일 표시
        show_pdf(pdf_path)

        # 다운로드 버튼 추가
        with open(pdf_path, "rb") as file:
            btn = st.download_button(
                label="Download CV",
                data=file,
                file_name="resume_hyeshinchu.pdf",
                mime="application/pdf"
            )          
