import streamlit as st
import time
import requests
import matplotlib.pyplot as plt
import plotly.graph_objects as go


#Prediction
st.header('Best Fit for Your Advertisements Budget', divider='green')
budget = st.number_input('Insert your budget for advertising')
st.write(f"""The current budget for advertising is: {round(budget,2)}""")

url=''
params={'budget':budget}

if st.button('Best Fit'):
    with st.spinner('Wait for it...'):
        time.sleep(1)
        response=requests.get(url,params).json()
        pred = response['Google Budget','Facebook Budget','Tiktok Budget']
    st.success(f" Google Budget= {pred[0]}!")
    st.success(f" Facebook Budget= {pred[1]} !")
    st.success(f" Tiktok Budget= {pred[2]} !")
    # labels = ['Google', 'Facebook', 'Tiktok']
    # values = [pred[0], pred[1], pred[2]]
    # colors=['#008000','#069AF3','#FF7F50']

    # fig = go.Figure(data=[go.Pie(labels=labels, values=values#, hole=.3
    #                             )])
    # fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
    #                   marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    # st.plotly_chart(fig)


labels = ['Google', 'Facebook', 'Tiktok']
values = [4500, 2500, 1053]
colors=['#008000','#069AF3','#FF7F50']

fig = go.Figure(data=[go.Pie(labels=labels, values=values#, hole=.3
                            )])
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
st.plotly_chart(fig)




# FOR MAIN.PY FILE:
# @app.get("/budgetdivider")
# def query_budget_divider(budget: float):
#     """
#     Returns amount of different advertisements according to input data
#     """
#     dict_feature={"budget":budget}

#     X_predict=
#     y_predict=app.state.model.predict(X_predict)

#     return {'Google Budget':y_predict[0],'Facebook Budget':y_predict[1],'Tiktok Budget':y_predict[2]}
