import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("🏠_Mainpage.py", label="Introduction", icon="🏠")
    #bar2.page_link("pages/1_📚_Experience.py", label= "Experience", icon="📚")
    bar2.page_link("pages/1_📚_Project.py", label= "Project", icon="📚")
    bar3.page_link("pages/2_🎨_Publication.py", label="Publication", icon="🎨")
    bar4.page_link("pages/3_🌏_CV.py", label="CV", icon="🌏")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Welcome! I am Hyeshin Chu, AI Product Manager in NAVER SNOW Corporation. 
                
                Currently, I'm figuring out how we can utilize generative AI technologies to enhance user experience and improve interaction between them.
                I believe in the intersectionality of quantitative and qualitative subjects, that neither approach alone can lead one to the absolute truth.
              """,
        'name':'Hyeshin Chu', 
        'study':'Graduate School of AI, UNIST',
        'location':'Seoul, Republic of Korea',
        'interest':'AI, Human-Computer Interaction, Responsible AI',
        'skills':['Python', 'MySQL', 'Github','Streamlit','OpenAI API', 'Figma', 'Qualitative Research', 'Quantitative Research','Survey','Focus Group Interview','Thematic Analysis','Experiment Design','LaTex'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]
Project = { 1:['Virtual Try-on',
              """
                  Launching a virtual try-on service
              """],
              2:['AI Avatar Profile',
                  """
                Launching an AI avatar profile generation service
                """],
              3:['Synthetic Data Pipeline for AI Architectures',
                """
                Creating a pipeline for human pose and facial expression recognition models
                """],
              4:['User Satisfaction on 3D Avatar Facial Expression',
                """
                Conducting a qualitative research on how people perceive 3D avatar facial expression feature
                """],
              5:['Human Perception on AI-generated Music',  
                """
                Proposing qualitative evaluation metrics to assess human satisfaction on AI-generated music
                """],
              6: ['Learning to Remember Patterns: Pattern Matching Memory Networks for Traffic Forecasting',
                """
                Proposing a forecasting architecture under complex spatio-temporal condition
                """], 
              7: ['A Visual Analytics System for Improving Attention-based Traffic Forecasting Models',
                """
                Designing a system that allow users to explore how AI architectures make prediction
                """],  
              8: ['Wait, Let’s Think about Your Purchase Again: A Study on Interventions for Supporting Self-Controlled Online Purchases',
                """
                Investigating users' impulse buying behaviors and self-control strategies
                """],
              9: ['An Empirical Experiment on Deep Learning Models for Predicting Traffic Data',
                """
                Analyzing the performance of traffic forecasting architectures 
                """]       
            }

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Publication = { 1:['An Empirical Study on How People Perceive AI-generated Music',
              """
                  *CIKM 2022: ACM International Conference on Information and Knowledge Management (27.51\% acceptance rate)* \\
                  **Hyeshin Chu**, Joohee Kim, Seongouk Kim, Hongkyu Lim, Hyunwook Lee, Seungmin Jin, Jongeun Lee, Taehwan Kim, Sungahn Ko 
              """],
              2:['Learning to Remember Patterns: Pattern Matching Memory Networks for Traffic Forecasting',
                  """
                *ICLR 2022: The International Conference on Learning Representations (32.26\% acceptance rate)* \\
                Hyunwook Lee, Seungmin Jin, **Hyeshin Chu**, Hongkyu Lim, Sungahn Ko
                """],
              3:['A Visual Analytics System for Improving Attention-based Traffic Forecasting Models',
                """
                *TVCG 2023: IEEE Transactions on Visualization and Computer Graphics (25\% acceptance rate)* \\
                Seungmin Jin, Hyunwook Lee, Cheonbok Park, **Hyeshin Chu**, Yunwon Tae, Jaegul Choo, Sungahn Ko
                """],
              4:['Wait, Let’s Think about Your Purchase Again: A Study on Interventions for Supporting Self-Controlled Online Purchases',
                """
                *WWW 2021: The ACM Web Conference (23\% acceptance rate)* \\
                Yunha Han, Hwiyeon Kim, **Hyeshin Chu**, Joohee Kim, Hyunwook Lee, Seunghyeong Choe, Dooyoung Jung, Dongil Chung, Bumchul Kwon, Sungahn Ko
                """],
              5:['An Empirical Experiment on Deep Learning Models for Predicting Traffic Data',  
                """
                *ICDE 2021: IEEE International Conference on Data Engineering (19\% acceptance rate)* \\
                Hyunwook Lee, Cheonbok Park, Seungmin Jin, **Hyeshin Chu**, Jaegul Choo, Sungahn Ko
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "82-10-9776-0511"
email = "hyeshinchu@gmail.com"
linkedin_link = "https://www.linkedin.com/in/hyeshinchu/"
github_link = "https://github.com/Rsirp0c?tab=repositories"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

#figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"
youtube_link_p5 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/LCGGLhLNZCY?si=at_wDtLZBmZsP38E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'

paper_link_p5 = "https://dl.acm.org/doi/pdf/10.1145/3511808.3557235"
paper_link_p4 = "https://arxiv.org/pdf/2110.10380.pdf"
paper_link_p3 = "https://arxiv.org/pdf/2208.04350.pdf"
paper_link_p2 = "https://dl.acm.org/doi/pdf/10.1145/3442381.3450021"
paper_link_p1 = "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9458663"


StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
