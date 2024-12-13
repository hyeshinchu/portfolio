import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Project", page_icon="📚", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
   menu()

   st.header("🎨 Project",divider='rainbow')

   # page functions ----------------------------------------------------------------
   def Project_component(header, content):
      st.subheader(header, divider='grey')
      st.write(content)

   # P9 ----------------------------------------------------------------
   Project_component(Project[1][0], Project[1][1])

   with st.expander("Detail"):
      st.write("To launch a virtual try-on service, I have conducted market research, defined key features of an web application, created user journey and interface layouts. Also, I developed an internal tool and a pipeline to create training and test dataset for the AI architecture.")
      try:
         img = Image.open("src/vto_demo.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P8 ----------------------------------------------------------------
   Project_component(Project[2][0], Project[2][1])

   with st.expander("Detail"):
      st.write("By launching an AI avatar profile service, user acquisition rate has been increased by 92% and achieved 75% reach rate. I designed 900 prompt templates for figure and background, respectively. I performed thematic analysis to quantify and interpret responses")
      try:
         img = Image.open("src/avatar_profile.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P7 ----------------------------------------------------------------
   Project_component(Project[3][0], Project[3][1])

   with st.expander("Detail"):
      st.write("By creating a synthetic data pipeline, I enhanced training procedure of human pose recognition and facial expression generation architectures. The data generation pipeline has built training datasets worth $360,000.")
      try:
         img = Image.open("src/synthetic.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P6 ----------------------------------------------------------------
   Project_component(Project[4][0], Project[4][1])

   with st.expander("Detail"):
      st.write("I established qualitative and quantitative methods to evaluate the performance of 3D avatar facial expression architectures. I developed and executed qualitative studies, including surveys and focus group interviews with animation modelers.")
      try:
         img = Image.open("src/facial.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P5 ----------------------------------------------------------------
   Project_component(Project[5][0], Project[5][1])

   with st.expander("Detail"):
      st.write("I led a research project to understand how people perceive AI-generated music. I designed and conducted quantitative and qualitative experiments with 120 participants. Also, I performed statistical analyses, including ANOVA and t-tests, to interpret experiment data.")
      try:
         img = Image.open("src/p5_1.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P4 --------------------------------------------------------------
   Project_component(Project[6][0], Project[6][1])
   
   with st.expander("Detail"):
      st.write("I executed qualitative research to identify user pain points and behavior patterns.")
      try:
         img = Image.open("src/p4.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P3 -------------------------------------------------------------- 
   Project_component(Project[7][0], Project[7][1])

   with st.expander("Detail"):
      st.write("To identify the features of a visual analytics system, I executed some case studies to inverstigate user journey.")
      try:
         img = Image.open("src/p3.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P2 -----------------------------------------------------------
   Project_component(Project[8][0], Project[8][1])

   with st.expander("Detail"):
      st.write("I conducted user surveys and interviews, to identify user pain points and understand their behavior patterns. Then, I investigated the experiment result by thematic analysis.")
      try:
         img = Image.open("src/p2.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")
    
    # P1  -----------------------------------------------------------------------------
   Project_component(Project[9][0], Project[9][1])
   
   with st.expander("Detail"):
      st.write("I researched some existing studies to select forecasting architectures and dataset for the evaluation. I participated in writing research paper.")
      try:
         img = Image.open("src/p1.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

