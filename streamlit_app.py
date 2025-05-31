import streamlit as st
import pandas as pd
import plotly.express as px 

# Set the page configuration

password = st.text_input ("Hey enter your password here.", type= "password")
if password == "Jordan25":
     

    #Sidebar
    st.sidebar.title("FP&A Software Selection")

    page = ['Home','FP&A Software Selection Overview','AI Comparison','Final Thoughts']
    st.sidebar.write("Select an option from the dropdown menu to navigate through the app.")
    page = st.sidebar.selectbox("Select a page:", page)
else:
    st.title("Access Denied")
    st.write("Please enter the correct password to access the app.")
    st.stop()

   

    #Display Pages   
if page == 'Home':
        st.title("📊 FP&A Software Selection")
        st.image('./Impellam NA logo.png', caption="Impellam Group Logo.") 
        st.write("The FP&A Software Selection Project provides helpful insights about the benefits and challenges of utilizing AI capabilties for the FP&A NA department of Impellam Group.")
        st.write("This project aims to compare two AI FP&A softwares: Datarails and Adaptive Insights.") 
        st.write("The goal is to provide a cgit omprehensive overview of their capabilities, benefits, and challenges in the context of financial planning and analysis.")
        st.write("The project will include an overview of the software selection process, a comparison of the two AI solutions, and final thoughts on the best fit for the FP&A department at Impellam Group. The project will also explore how these AI solutions can enhance financial data analysis, improve reporting efficiency, and support strategic decision-making within the organization.")
        st.write("The project will be presented in a Streamlit app format, allowing for interactive exploration of the software features and capabilities. Users will be able to navigate through different sections, view comparisons, and gain insights into the benefits and challenges of each solution.")
        

elif page =='FP&A Software Selection Overview':
        st.title("FP&A Software Selection Overview")
        st.image("./Impellam NA logo.png")
        st.write("Welcome to the Home Page of my steamlit for the FP&A Software Selection Project. The purpose of this app is to compare the benefits and challenges of two AI FP&A softwares: Datarails and Adaptive Insights!")
        st.write("Impellam has a strategic business need to improve speed  on decisions, provide advanced forecasting models, reduce manual efforts across static excel files and enhance enterprise reporting across multiple finance functions.")
        st.write("To solve this need, Finance selected a tool that can meet all internal deliverables and be utilized by a broader audience than current tools. These deliverables include Margin & Revenue scenario modeling, internal cost modeling, Annual budgeting processes, detailed updates for monthly forecasting , enhanced internal reporting, self service reporting and budget management.")
        

elif page == 'AI Comparison':
            st.title("AI Comparison")
            st.write("This page provides tailored insights about the benfits and challenges of Datarails and Adaptive Inisghts for the FP&A department Impellam group.")
        

elif page == 'Final Thoughts':
            st.title("Final Thoughts")
            st.write("Both Datarails and Adaptive Insights offer powerful features for financial analysis, but they differ in terms of ease of use, integration capabilities, and advanced functionalities. Based on the options, Adaptive Inisghts is a clear choice for Impellam Group based on it's advanced capabilities in the following areas: Generative AI, Conversational AI, Report Generation, Variance Analysis, Integration with Tools, Drill-Down Capabilitiy, and Rapid Delivery.")
            st.image("./AI software_comparison logo.jpg")
if page == 'AI Comparison':
        # Create tabs for the AI Comparison section
        st.sidebar.write("AI Comparison")
        st.sidebar.write("This page provides tailored insights about the benefits and challenges of Datarails and Adaptive Insights for the FP&A department at Impellam Group.")
        st.sidebar.write("Select a tab to view the comparison details.")
        # Create tabs for the AI Comparison section
        tab1, tab2, tab3 = st.tabs(["Purpose of AI Comparison","Datarails", "Adaptive Insights"])
        with tab1:
            st.title("Purpose of AI Comparison")
            st.write("The purpose of this page is to compare two FP&A software solutions, Datarails and Adaptive Insights, in the context of the strategic business need outlined by the FP&A department at Impellam Group. The comparison will focus on their capabilities in handling financial data, ease of use, and integration with existing systems.")
            st.image('./AI software_comparison logo.jpg', caption="AI Comparison Overview")

        with tab2:
            st.title("Datarails")
            st.write("Datarails is a financial planning and analysis software that provides Data Integration, Reporting, and Analytics Capabilities. It allows users to Connect Various Data Sources, Automate Reporting Processes, and Gain Insights into Financial Performance.")
            st.image('./chat bot_datarails.png', caption="Datarails AI Functionality")
            st.write("Datarails can be used to analyze the Impellam data by Integrating it with Financial Data, Automating the Generation of Reports, and providing Visualizations of Key Metrics. However, it may have limitations in terms of it's limited capabilities in generative AI, conversational AI, and advanced reporting features.")

        with tab3:
            st.title("Adaptive Insights")
            st.write("Adaptive Insights is a cloud-based financial planning and analysis software that offers budgeting, forecasting, and reporting capabilities. It provides a user-friendly interface for creating financial models and analyzing data.")
            st.image('./adaptive_AI capab_1.jpg', caption="Adaptive Insights AI Functionality")
            st.write("Adaptive Insights will be used to analyze the Impellam financial data by creating Value-Centric Financial Models, Quality Data Management, Extensible Innovation, and Responsible AI.")
            st.image('./adaptive_AI capab_2.jpg')
            st.write(" Adaptive Insights offers the following AI capabilities included wiht our current subscription: Workday Assistant, Preditctive Forecasting, Anomoly Detection, and Intelligence Variance Analysis.")
            st.image('./adaptive_predictive_forecast.jpg')
            st.write("The image above is an example of the predictive forecasting dashboard.")


