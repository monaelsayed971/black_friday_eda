## import libraries

import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib as mlp                    
import matplotlib.pyplot as plt
import plotly .express as px 
#import datasispipt as ds
import streamlit as st 
import plotly.graph_objs as go
#from pandas_profiling import ProfileReport
#ProfileReport(df_data,title='black friday',html={'style':{'full_width':True}})
image_path = "walmart_black_friday.png"

st.image(image_path, caption='Walmart Black Friday Sale', width=1000)
sns.set(rc={'figure.figsize': [9, 9]}, font_scale=1.2)
df_data= pd.read_csv('df_clean.csv')
df_clean=df_data.copy()
df_clean.head()
st.title("Black friday EDA")
st.dataframe(df_clean.head())
option = st.selectbox("UNIVARIANT",['Age','Purchase','City_Category','Occupation','Gender','Marital_Status','Product_Category_2','Product_Category_3','Product_Category_1'])
if option=='Occupation':
    fig1 = px.bar(df_clean['Occupation'].value_counts(),
             x=df_clean['Occupation'].value_counts().index,
             y=df_clean['Occupation'].value_counts().values,
             labels={'x': 'Occupation', 'y': 'Count'},
             title='Occupation Value Counts')
    st.plotly_chart(fig1)
elif   option=='Purchase': 
    fig2 = px.bar(df_clean['Purchase'].value_counts(), 
                  x=df_clean['Purchase'].value_counts().index, 
                  y=df_clean['Purchase'].value_counts().values, 
                  labels={'x': 'Purchase', 'y': 'Count'},
                  title='Purchase Value Counts')
    st.plotly_chart(fig2)
    st.write('can observe the distribution of purchase amounts This information can be useful in understanding customer behavior and preferences, as well as identifying potential areas for improvement in your sales and marketing strategies.')
elif option=='Product_Category_1':
    fig3 = px.bar(df_clean['Product_Category_1'].value_counts(),
             x=df_clean['Product_Category_1'].value_counts().index,
             y=df_clean['Product_Category_1'].value_counts().values,
             labels={'x': 'Product_Category_1', 'y': 'Count'},
             title='Product_Category_1 Value Counts')
    st.plotly_chart(fig3)
elif option =='Product_Category_2':
    fig4 = px.bar(df_clean['Product_Category_2'].value_counts(),
             x=df_clean['Product_Category_2'].value_counts().index,
             y=df_clean['Product_Category_2'].value_counts().values,
             labels={'x': 'Product_Category_2', 'y': 'Count'},
             title='Product_Category_2 Value Counts')
    st.plotly_chart(fig4)
elif option == 'Product_Category_3':
    fig5 = px.bar(df_clean['Product_Category_3'].value_counts(),
             x=df_clean['Product_Category_3'].value_counts().index,
             y=df_clean['Product_Category_3'].value_counts().values,
             labels={'x': 'Product_Category_3', 'y': 'Count'},
             title='Product_Category_3 Value Counts')
    st.plotly_chart(fig5)
elif option =='Marital_Status':
    fig6 = px.bar(df_clean['Marital_Status'].value_counts(),
             x=df_clean['Marital_Status'].value_counts().index,
             y=df_clean['Marital_Status'].value_counts().values,
             labels={'x': 'Marital Status', 'y': 'Count'},
             title='Marital Status Value Counts')
    st.plotly_chart(fig6)
    st.write(' married and has higher count as compared to singles.')
elif option =='City_Category':
    fig7 = px.bar(df_clean['City_Category'].value_counts(),
             x=df_clean['City_Category'].value_counts().index,
             y=df_clean['City_Category'].value_counts().values,
             labels={'x': 'City Category', 'y': 'Count'},
             title='City Category Value Counts')
    st.plotly_chart(fig7)
    st.write('city categories have the highest number of customers is B and which city categories have the lowest number of customers A . This information can be useful in understanding customer behavior and preferences. For example, you may find that customers from certain city categories are more likely to purchase')
elif option =='Gender':
    fig8 = px.bar(df_clean['Gender'].value_counts(),
             x=df_clean['Gender'].value_counts().index,
             y=df_clean['Gender'].value_counts().values,
             labels={'x': 'Gender', 'y': 'Count'},
             title='Gender Value Counts')
    st.plotly_chart(fig8)
    st.write('')
elif option=='Age':
    fig9 = px.bar(df_clean['Age'].value_counts(),
             x=df_clean['Age'].value_counts().index,
             y=df_clean['Age'].value_counts().values,
             labels={'x': 'Age', 'y': 'Count'},
             title='Age Value Counts')
    st.plotly_chart(fig9)
    st.write('distribution of customers across different age groups.  which age groups have the highest number of customers(26-35) and which age groups have the lowest number (0-17) This information can be useful in understanding customer behavior and preferences.may find that certain age groups are more likely to purchase certain products or services')
     
    
    
    
    
    
    
    
option = st.selectbox("BIVARIATE",['Age','Occupation','Gender','cities','Marital_Status','Product_Category_1'])
if option=='Age':
        age_dict = {'0-17': 1, '18-25': 2, '26-35': 3, '36-45': 4, '46-50': 5, '51-55': 6, '55+': 7}
        df_clean['AgeNum'] = df_clean['Age'].map(age_dict)
        df_clean['Age'] = pd.Categorical(df_clean['AgeNum'], categories=age_dict, ordered=True)
        fig, ax = plt.subplots()
        sns.regplot(x='AgeNum', y='Purchase', data=df_clean, ax=ax)
        ax.set_title('Relationship Between Age and Purchase Amount')
        ax.set_xlabel('Age')
        ax.set_ylabel('Purchase Amount')
        st.pyplot(fig) 
        st.write('The correlation coefficient is a measure of the strength and direction of the relationship between two variables, and ranges from -1 to 1. In this case, the correlation coefficient is relatively weak and positive, suggesting that there is a positive but not very strong correlation between age and purchase amount.')
elif option=='Gender':
    gender_totals = df_clean.groupby('Gender')['Purchase'].sum() 
    data = go.Bar(x=gender_totals.index, y=gender_totals.values, marker=dict(color=['blue', 'pink'])) 
    layout = go.Layout(title='total purchase amount for each gender',xaxis=dict(title='Gender'), yaxis=dict(title='Purchase Amount')) 
    fig = go.Figure(data=[data], layout=layout)
    st.plotly_chart(fig)
    st.write('These visualizations suggest that there are differences in purchase behavior between male and female customers, with male customers tending to spend more money than female')
elif option=='Occupation':
    occupation_totals = df_clean.groupby('Occupation')['Purchase'].sum()
    data = go.Bar(x=occupation_totals.index, y=occupation_totals.values)
    layout = go.Layout(title='Total Purchase Amount by Occupation', xaxis=dict(title='Occupation'), yaxis=dict(title='Purchase Amount'))
    fig = go.Figure(data=[data], layout=layout)
    st.plotly_chart(fig)
    st.write('plot shows that customers in certain occupations, such as occupation 4 and 0, tend to spend more money overall than customers in other occupations.')
elif option=='cities': 
     city_totals = df_clean.groupby('City_Category')['Purchase'].sum()
     fig1, ax1 = plt.subplots(figsize=(8, 6)) 
     city_totals.plot(kind='bar', ax=ax1)
     ax1.set_title('Total Purchase Amount by City')
     ax1.set_xlabel('City')
     ax1.set_ylabel('Purchase Amount')
     st.pyplot(fig1)
     st.write('plot shows that customers from city category B tend to spend more money overall than customers from city categories A and C.')
elif option=='Marital_Status'  : 
    grouped_data = df_clean.groupby("Marital_Status")["Purchase"].mean().reset_index() 
    fig = px.bar(grouped_data, x="Marital_Status", y="Purchase", title="Average Purchase Amount by Marital Status")
    st.plotly_chart(fig) 
elif option=='Product_Category_1':
    grouped_data = df_clean.groupby("Product_Category_1")["Purchase"].mean().reset_index() 
    fig = px.bar(grouped_data, x="Product_Category_1", y="Purchase", title="Average Purchase Amount by Product_Category_1")
    st.plotly_chart(fig) 
    
    
    
colors = ['coral', 'skyblue', 'lightgreen']
avg_purchase = df_clean.groupby('City_Category')['Purchase'].mean()

# Create the pie chart with a custom color map
fig, ax = plt.subplots()
ax.pie(avg_purchase, colors=colors, autopct='%1.1f%%')

ax.set_title('Average Purchase by City Category')
ax.set_ylabel('')
ax.legend(labels=df_clean['City_Category'].unique(), loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
st.pyplot(fig)


a = df_clean.groupby('Age')['Age'].agg('count')
fig, ax = plt.subplots()
ax.set_title('Age count')
palette_color = sns.color_palette('bright')
ax.pie(a, colors=palette_color, labels=a.index, radius=1.2, autopct='%1.1f%%')

# use st.pyplot() to display the plot in the Streamlit app
st.pyplot(fig)




        
        
st.title('what is the 5 top categories that have been purchased ?') 
category_purchases = df_clean.groupby('Product_Category_1')['Purchase'].sum()
category_purchases_sorted = category_purchases.sort_values(ascending=False)
top_categories = category_purchases_sorted.head(5).index.tolist()
df_top_categories = df_clean[df_clean['Product_Category_1'].isin(top_categories)]
category_counts = df_top_categories.groupby('Product_Category_1')['Purchase'].count() 
data = go.Bar(x=category_counts.index, y=category_counts.values) 
layout = go.Layout( xaxis=dict(title='Product Category'), yaxis=dict(title='Purchase Count')) 
fig = go.Figure(data=[data], layout=layout)
st.plotly_chart(fig)


# Group the data by city category, gender, and marital status
purchase_matrial_city_catogries = df_clean.groupby(['City_Category', 'Gender', 'Marital_Status']).agg({'Purchase': 'mean', 'Product_ID': 'nunique'}).reset_index()
data = [
    go.Bar(name='Average Purchase', x=purchase_matrial_city_catogries['City_Category'] + ' - ' + purchase_matrial_city_catogries['Gender'] + ' - ' + purchase_matrial_city_catogries['Marital_Status'].astype(str), y=purchase_matrial_city_catogries['Purchase'], marker=dict(color='#FF69B4')),  # orange
    go.Bar(name='Number of Unique Products', x=purchase_matrial_city_catogries['City_Category'] + ' - ' + purchase_matrial_city_catogries['Gender'] + ' - ' + purchase_matrial_city_catogries['Marital_Status'].astype(str), y=purchase_matrial_city_catogries['Product_ID'], marker=dict(color='#4169E1'))  # blue
]
layout = go.Layout(title='Average Purchase and Number of Unique Products by City Category, Gender, and Marital Status',
                   xaxis=dict(title='City Category, Gender, and Marital Status'),
                   yaxis=dict(title='Value'))
fig = go.Figure(data=data, layout=layout)
fig.update_layout(barmode='group', legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1), height=400, width=600)
st.plotly_chart(fig)





temp = df_clean.groupby(['Age', 'Gender', 'Marital_Status'])['Purchase'].mean().reset_index()\
    .sort_values(by=['Age', 'Purchase'], ascending=[1,1])
fig = px.bar(temp, x='Age', y='Purchase', color='Gender', facet_col='Marital_Status',
             barmode='group', title='Mean of Purchase')
fig.update_yaxes(range=[7000, 10000])
st.plotly_chart(fig)



relationship_between_occupation_purchase = df_clean.groupby(['Age', 'City_Category', 'Occupation'])['Purchase'].mean().reset_index()
fig = px.scatter(relationship_between_occupation_purchase, x='Occupation', y='Purchase', color='Age', hover_data=['City_Category'])
fig.update_layout(title='Relationship Between Occupation and Purchase by Age and City Category',
                  xaxis_title='Occupation',
                  yaxis_title='Average Purchase')
st.plotly_chart(fig)



user_data = df_clean.groupby('User_ID').agg({'Product_ID': 'count', 'Purchase': 'sum'}).reset_index()
fig = px.scatter(user_data, x='Product_ID', y='Purchase', 
                 labels={'Product_ID': 'Number of Products Purchased', 'Purchase': 'Total Purchase Amount'},
                 title='Total Purchase Amount vs. Number of Products Purchased')
st.plotly_chart(fig)







def fn():
    summary_text = '- There are differences in purchase behavior between male and female customers, with male customers tending to spend more money overall.\n- Certain product categories are more popular among female customers, while male customers also have popular products.\n- Customers in occupation groups 4 and 0 tend to spend more money overall than customers in other occupations.\n- There is a slight difference in the average purchase amount between different cities, with customers from city category B having the highest average purchase amount.\n- Younger age groups tend to spend less overall: Across most product categories, younger age groups (e.g., 0-17 and 18-25) tend to have lower purchase amounts than older age groups.\n- Purchase amount generally increases with age for product categories 1, 2, and 3.\n- Product category 1 has the highest overall purchase amount.\n- Young adults (18-25) in city category A tend to spend more when their occupation is 0 or 4, while middle-aged adults (36-45) in city category C tend to spend more when their occupation is 1 or 7.\n- In most age groups (besides ages 46-50), married male customers have a slightly higher mean purchase than unmarried customers.'
    return summary_text

# use st.beta_expander() to create a collapsible section for the summary text
with st.expander("Click to view summary"):
    # display the summary text when the expander is opened
    st.markdown(fn())

