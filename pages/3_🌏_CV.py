import streamlit as st 
import os
import base64
from PyPDF2 import PdfReader  # PDF 파일을 읽기 위한 라이브러리

st.set_page_config(page_title="CV", page_icon="🌏", initial_sidebar_state="collapsed", layout="wide")
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    #menu()
    def menu():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Go to", ["🏠 Introduction", "📚 Project", "🎨 Publication", "🌏 CV"])
    
    if selection == "🏠 Introduction":
        st.experimental_set_query_params(page="Introduction")
    elif selection == "📚 Project":
        st.experimental_set_query_params(page="Project")
    elif selection == "🎨 Publication":
        st.experimental_set_query_params(page="Publication")
    elif selection == "🌏 CV":
        st.experimental_set_query_params(page="CV")
    
    st.header("🌏 CV", divider='rainbow')

    # PDF 파일 경로 확인
    pdf_path = "src/resume.pdf"
    if not os.path.exists(pdf_path):
        st.error("PDF 파일이 존재하지 않습니다. 경로를 확인하세요.")
    else:
        # PDF 파일 내용을 읽고 표시하는 함수
        def read_pdf(file_path):
            with open(file_path, "rb") as f:
                pdf_reader = PdfReader(f)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"  # 각 페이지의 텍스트를 추출
            return text

        # PDF 파일 내용 표시
        pdf_text = read_pdf(pdf_path)
        st.text_area("Resume Content", value=pdf_text, height=800)  # PDF 내용을 텍스트 영역에 표시

        # 다운로드 버튼 추가
        with open(pdf_path, "rb") as file:
            btn = st.download_button(
                label="Download CV",
                data=file,
                file_name="resume_hyeshinchu.pdf",
                mime="application/pdf"
            )
