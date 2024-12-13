import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from constant import *
from streamlit_player import st_player

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Publication", page_icon="🎨", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
   menu()

   st.header("🎨 Publication",divider='rainbow')

   # page functions ----------------------------------------------------------------
   def Publication_component(header, content):
      st.subheader(header, divider='grey')
      st.write(content)

   # P5 ----------------------------------------------------------------
   Publication_component(Publication[1][0], Publication[1][1])

   col1, col2 = st.columns([2, 1])
   with col1:
      st.link_button("Full Paper", "https://dl.acm.org/doi/10.1145/3511808.3557235")

   with col2:
      if st.button("Presentation"):
         st.video("https://www.youtube.com/watch?v=LCGGLhLNZCY")

   #st.image("src/p5_1.png", width=800)
   with st.expander("Abstract"):
      st.write("Music creation is difficult because one must express one's creativity while following strict rules. The advancement of deep learning technologies has diversified the methods to automate complex processes and express creativity in music composition. However, prior research has not paid much attention to exploring the audiences' subjective satisfaction to improve music generation models. In this paper, we evaluate human satisfaction with the state-of-the-art automatic symbolic music generation models using deep learning. In doing so, we define a taxonomy for music generation models and suggest nine subjective evaluation metrics. Through an evaluation study, we obtained more than 700 evaluations from 100 participants, using the suggested metrics. Our evaluation study reveals that the token representation method and models' characteristics affect subjective satisfaction. Through our qualitative analysis, we deepen our understanding of AI-generated music and suggested evaluation metrics. Lastly, we present lessons learned and discuss future research directions of deep learning models for music creation.")
      try:
         img = Image.open("src/p5_1.png")
         st.image(img)
      except Exception as e:
         st.error(f"Error loading image: {e}")

   # P4 --------------------------------------------------------------
   Publication_component(Publication[2][0], Publication[2][1])

   st.link_button("Full Paper", "https://arxiv.org/pdf/2110.10380.pdf")
   
   with st.expander("Abtract"):
      st.write("Traffic forecasting is a challenging problem due to complex road networks and sudden speed changes caused by various events on roads. Several models have been proposed to solve this challenging problem, with a focus on learning the spatio-temporal dependencies of roads. In this work, we propose a new perspective for converting the forecasting problem into a pattern-matching task, assuming that large traffic data can be represented by a set of patterns. To evaluate the validity of this new perspective, we design a novel traffic forecasting model called Pattern-Matching Memory Networks (PM-MemNet), which learns to match input data to representative patterns with a key-value memory structure. We first extract and cluster representative traffic patterns that serve as keys in the memory. Then, by matching the extracted keys and inputs, PM-MemNet acquires the necessary information on existing traffic patterns from the memory and uses it for forecasting. To model the spatio-temporal correlation of traffic, we proposed a novel memory architecture, GCMem, which integrates attention and graph convolution. The experimental results indicate that PM-MemNet is more accurate than state-of-the-art models, such as Graph WaveNet, with higher responsiveness. We also present a qualitative analysis describing how PM-MemNet works and achieves higher accuracy when road speed changes rapidly.")
      st.image("src/p4.png", use_container_width=True)

   # P3 -------------------------------------------------------------- 
   Publication_component(Publication[3][0], Publication[3][1])

   st.link_button("Full Paper", "https://www.computer.org/csdl/journal/tg/2023/01/09903281/1GZolp3W1mE")

   with st.expander("Abstract"):
      st.write("With deep learning (DL) outperforming conventional methods for different tasks, much effort has been devoted to utilizing DL in various domains. Researchers and developers in the traffic domain have also designed and improved DL models for forecasting tasks such as estimation of traffic speed and time of arrival. However, there exist many challenges in analyzing DL models due to the black-box property of DL models and complexity of traffic data (i.e., spatio-temporal dependencies). Collaborating with domain experts, we design a visual analytics system, AttnAnalyzer, that enables users to explore how DL models make predictions by allowing effective spatio-temporal dependency analysis. The system incorporates dynamic time warping (DTW) and Granger causality tests for computational spatio-temporal dependency analysis while providing map, table, line chart, and pixel views to assist user to perform dependency and model behavior analysis. For the evaluation, we present three case studies showing how AttnAnalyzer can effectively explore model behaviors and improve model performance in two different road networks. We also provide domain expert feedback.")
      st.image("src/p3.png", use_container_width=True)

   # P2 -----------------------------------------------------------
   Publication_component(Publication[4][0], Publication[4][1])

   st.link_button("Full Paper", "https://dl.acm.org/doi/abs/10.1145/3442381.3450021")

   with st.expander("Abstract"):
      st.write("As online marketplaces adopt new technologies to encourage consumers’ purchases (e.g., one-click purchases), the number of consumers who impulsively buy products also increases. Although some interventions have been introduced for consumers’ self-controlled purchases, there have been few studies that evaluate the effectiveness of the techniques in the real environment. In this paper, we conducted an online survey with 118 consumers in their 20s to investigate their impulse buying behaviors and self-control strategies. Based on the survey results and literature surveys, we developed interventions that can assist consumers in controlling their online purchase habits, including Reflection, Distraction, Desire Reduction, and Salient Cost. For evaluation, we enrolled 107 participants in a user study on a real-world e-commerce site. The results indicate that all interventions were effective in reducing impulse buying urges, with variations in user experiences. Our findings and design implications are discussed.")
      st.image("src/p2.png", use_container_width=True)
    
    # P1  -----------------------------------------------------------------------------
   Publication_component(Publication[5][0], Publication[5][1])

   st.link_button("Full Paper", "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9458663")
   
   with st.expander("Abstract"):
      st.write("To tackle ever-increasing city traffic congestion problems, researchers have proposed deep learning models to aid decision-makers in the traffic control domain. Although the proposed models have been remarkably improved in recent years, there are still questions that need to be answered before deploying models. For example, it is difficult to figure out which models provide state-of-the-art performance, as recently proposed models have often been evaluated with different datasets and experiment environments. It is also difficult to determine which models would work when traffic conditions change abruptly (e.g., rush hour). In this work, we conduct two experiments to answer the two questions. In the first experiment, we conduct an experiment with the state-of-the-art models and the identical public datasets to compare model performance under a consistent experiment environment. We then extract a set of temporal regions in the datasets, whose speeds change abruptly and use these regions to explore model performance with difficult intervals. The experiment results indicate that Graph-WaveNet and GMAN show better performance in general. We also find that prediction models tend to have varying performances with data and intervals, which calls for in-depth analysis of models on difficult intervals for real-world deployment.")
      st.image("src/p1.png", use_container_width=True)

