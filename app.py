import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Watch Analysis')

df = pd.read_csv('D:\Career\Data Science\CX\Deployment\Streamlit\Cleaned_LuxuryWatches.csv')

st.title('Watch Analysis')

st.sidebar.title('Menu')

options = st.sidebar.selectbox('Options',['Overall Analysis','Brand'])

def load_overall_analysis():
    st.subheader('Overall Analysis')

    overall_option1 = st.selectbox('Area',['Brand-Model','Material','Build','Appearance','Function'])

    if overall_option1 == 'Brand-Model':
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            # No of Brands
            no_brands = df['Brand'].value_counts()
            st.dataframe(no_brands)

        with col2:
            # Pie chart for No of brands
            brand_pie = df['Brand'].value_counts().head(5)

            fig1, ax1 = plt.subplots()
            ax1.pie(brand_pie,labels=brand_pie.index,autopct='%0.01f')
            st.pyplot(fig1)
            st.metric('Total Brands',df['Brand'].unique().shape[0])


        with col3:
            # Count for each Model
            no_models = df['Model'].value_counts()
            st.dataframe(no_models)

        with col4:
            # Pie chart for No of Models
            model_pie = df['Model'].value_counts().head(10)

            fig2, ax2 = plt.subplots()
            ax2.pie(model_pie,labels=model_pie.index,autopct='%0.01f')
            st.pyplot(fig2)
            st.metric('Total Model',df['Model'].unique().shape[0])

    elif overall_option1 == 'Material':
        st.title('Material Analysis')
        
        col5,col6 = st.columns(2)
        with col5:
            st.subheader('Case Type Counts')
            df['Case type'] = df['Case Material'].apply(lambda x : 'gold' if 'gold' in x.lower() 
                                        else ('steel' if 'steel' in x.lower() 
                                            else ('titanium' if 'titanium' in x.lower() 
                                                    else ('ceramic' if 'ceramic' in x.lower() 
                                                        else ('fiber' if 'fiber' in x.lower() 
                                                                else ('bronze' if 'bronze' in x.lower() else np.nan))))))   

            st.table(df['Case type'].value_counts()) 


        with col6:
            st.subheader('Strap Material Counts')
            st.table(df['Strap Material'].value_counts()) 
        
        col7,col8 = st.columns(2)
        with col7:
            st.write('Min Max Price based on Case Type')
            st.table(df.groupby('Case type')['Price(INR)'].agg(['min','max']).round())
        
        with col8:
            st.write('Min Max Price based on Strap Material')
            st.table(df.groupby('Strap Material')['Price(INR)'].agg(['min','max']).round())

    elif overall_option1 == 'Build':
       
        st.title('Build Analysis')

        col9,col10 =st.columns(2)

        with col9:
            st.write('Case Diameter(mm) Analysis')
            st.table(df['Case Diameter (mm)'].value_counts().sort_values(ascending=False).round().head(10))

        with col10:
            st.write('Case Diameter Graph')
            fig3,ax3 = plt.subplots()
            ax3.hist(df['Band Width (mm)'])
            
            st.pyplot(fig3)

        col11,col12 =st.columns(2)
    
        with col11:
            st.write('Case Thickness(mm)  Analysis')
            st.table(df['Case Thickness (mm)'].value_counts().sort_values(ascending=False).round().head(15))

        with col12:
            st.write('Case Thickness Graph')
            fig4,ax4 = plt.subplots()
            ax4.hist(df['Case Thickness (mm)'])

            st.pyplot(fig4)

        col13,col14 =st.columns(2)
    
        with col13:
            st.write('Band Width(mm)  Analysis')
            st.table(df['Band Width (mm)'].value_counts().sort_values(ascending=False).round().head(15))

        with col14:
            st.write('Band Width Graph')
            fig5,ax5 = plt.subplots()
            ax5.hist(df['Band Width (mm)'][df['Band Width (mm)'].value_counts()],bins=15)

            st.pyplot(fig5)
    
    elif overall_option1 == 'Appearance':
        st.subheader('Appearance')
        col15,col16 = st.columns(2)
        with col15:
            st.write('Dial Color')
            st.table(df['Dial Color'].value_counts())
            fig6,ax6 = plt.subplots()
            ax6.pie(df['Dial Color'].value_counts(),labels=df['Dial Color'].value_counts().index,autopct='%0.01f')          
        

            st.pyplot(fig6)

        with col16:
            st.write('Crystal Material')
            st.table(df['Crystal Material'].value_counts())
            fig7,ax7 = plt.subplots()
            ax7.pie(df['Crystal Material'].value_counts(),labels=df['Crystal Material'].value_counts().index,autopct='%0.01f')          
        

            st.pyplot(fig7)

    elif overall_option1 == 'Function':
        col17,col18,col19,col20 = st.columns(4)
        with col17:
            st.write('Movement Type')
            st.table(df['Movement Type'].value_counts())
            fig8,ax8 = plt.subplots()
            ax8.pie(df['Movement Type'].value_counts(),labels=df['Movement Type'].value_counts().index,autopct='%0.01f')            

            st.pyplot(fig8)

        with col18:
            st.write('Water Resistance')
            st.table(df['Water Resistance meters'].value_counts())
            fig9,ax9 = plt.subplots()
            ax9.pie(df['Water Resistance meters'].value_counts(),labels=df['Water Resistance meters'].value_counts().index,autopct='%0.01f')            

            st.pyplot(fig9)

        with col19:
            st.write('Complications')
            st.table(df['Complications'].value_counts().head(10))
            fig10,ax10 = plt.subplots()
            ax10.pie(df['Complications'].value_counts(),labels=df['Complications'].value_counts().index,autopct='%0.01f')            

            st.pyplot(fig10)

        with col20:
            st.write('Power Reserve hours')
            st.table(df['Power Reserve hours'].value_counts().head(15))
            fig11,ax11 = plt.subplots()
            ax11.pie(df['Power Reserve hours'].value_counts(),labels=df['Power Reserve hours'].value_counts().index,autopct='%0.01f')            

            st.pyplot(fig11)      

def load_brand_analysis(brand_sel,model_sel):
    st.subheader('Brand Analysis')

    brand_options = st.sidebar.selectbox('Brand Option',['Price','Overall','Build',])
    
    brand_model = df[df['Brand'].str.contains(brand_sel) & df['Model'].str.contains(model_sel)].head() 
    st.dataframe(brand_model[['Brand','Model','Price(INR)']])
    
    # elif brand_options == 'Overall':
    #     brand_model = df[df['Brand'].str.contains(brand_sel) & df['Model'].str.contains(model_sel)].head() 
    #     st.dataframe(brand_model['Price(INR)'].mean())

if options == 'Overall Analysis':
    load_overall_analysis()

elif options == 'Brand':
    selected_brand = st.sidebar.selectbox('Select Brand', sorted(df['Brand'].unique()))
    filtered_models = df[df['Brand'] == selected_brand]['Model']
    selected_model = st.sidebar.selectbox('Select Model', sorted(df[df['Brand'] == selected_brand]['Model'].unique()))
    btn1 = st.sidebar.button('Select Brand')
    if btn1: 
        load_brand_analysis(selected_brand, selected_model)




