import streamlit as st
import seaborn as sns
import plotly.express as px

#st.title("Explore the Insights of Car Crashes Data")

#df=sns.load_dataset("car_crashes")
#st.dataframe(df)

#total accidents by State
#fig = px.bar(df, x='abbrev', y='total',
#             title = 'Total accidents by State',
#             labels = {'abbrev':'State','total':'Total Accidents'},
#             color='total',template='plotly_dark')

#st.plotly_chart(fig)



st.title("Explore the insight of titanic Data")

df=sns.load_dataset("titanic")


#gender filter
gender=st.sidebar.multiselect("Gender",
                              options = df['sex'].unique(),
                              default=df['sex'].unique())


#class filter
class_filter=st.sidebar.multiselect("Class",
                              options = df['class'].unique(),
                              default=df['class'].unique())


#age filter
min_age,max_age=st.sidebar.slider("Age",
                              min_value=int(df['age'].min()),
                              max_value=int(df['age'].max()),
                              value=(int(df['age'].min()),int(df['age'].max()))
)


filtered_df=df[
              (df['sex'].isin(gender)) &
               (df['class'].isin(class_filter)) &
               (df['age']>=min_age) &
               (df['age']<=max_age)

               ]

st.dataframe(filtered_df)




#total survived by class
fig=px.bar(df,x='class',y='survived',
           title = 'Total survivied by Class',
           labels = {'class':'Class','survived':'Total survived'},
           color='survived',template='plotly_dark'
           )
st.plotly_chart(fig)

#Age distribution
fig=px.histogram(df,x='age',
                 title='Age distribution',
                 labels={'age':'Age'},
                 color_discrete_sequence=['#F39C12'],
                template = 'plotly_dark'
                )


st.plotly_chart(fig)


#cd Dashboard
#streamlit run home.py


#pie chart for class distribution
fig = px.pie(df,names='class',
             title='Class Ditribution',
             color_discrete_sequence=px.colors.sequential.RdBu,
             template='plotly_dark' 
                  )


st.plotly_chart(fig)