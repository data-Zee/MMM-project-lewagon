# imports
import pandas as pd
import cvxpy as cp
import numpy as  np
from mamimo.time_utils import add_time_features
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
import pandas as pd
import holidays
import os
import pickle
from datetime import datetime
from mmmproject.model.params import *
from mmmproject.model.registry import minmax_fb, minmax_gg, minmax_tt



'''creating a check if the date that was provided by the user is a holiday,
a weekend, month of Jan or July and therefore creating new features'''
# weekend feature

class AddWeekendsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # This transformer doesn't need to learn any parameters during fitting,
        # so we simply return self.
        return self

    def transform(self, X):
        """Creates a new column with row value = 1 if the day is a Friday or Saturday and 0 if not."""
        df = X.copy()  # Create a copy of the input DataFrame to avoid modifying it directly
        weekday_values = df.index.weekday
        df['fri_sat'] = ((weekday_values == 4) | (weekday_values == 5)).astype(int)
        return df[['fri_sat']]


def find_optimal_budget(TOTAL_DAILY_BUDGET, Date):
    df=pd.DataFrame([pd.to_datetime(Date)])
    df.set_index(0, inplace=True)
    df['day']=Date
    df['day']=pd.to_datetime(df['day'])

    #treansforming the date df

    transformed_df = AddWeekendsTransformer().fit_transform(df)
    transformed_df.columns = ['weekends']


    # model cvxpy

    # Variables
    facebook_var = cp.Variable(pos=True)
    google_var   = cp.Variable(pos=True)
    tiktok_var  = cp.Variable(pos=True)


    # Constraint
    constraint = [google_var + facebook_var + tiktok_var <= TOTAL_DAILY_BUDGET, google_var>=TOTAL_DAILY_BUDGET*0.04769543069031596, facebook_var>=TOTAL_DAILY_BUDGET*0.16612285992471154, tiktok_var>=TOTAL_DAILY_BUDGET*0.0361817093849725]


    # Objective
    obj= cp.Maximize(intercept+ weekend* transformed_df['weekends'][0]+facebook *minmax_fb(facebook_var) + google *minmax_gg(google_var)+ tiktok*minmax_tt(tiktok_var))

    # Solve
    prob = cp.Problem(obj, constraint)
    prob.solve(solver='OSQP', verbose=False)
    # Print solution
    status=prob.status
    value_Total_clicks=prob.value
    value_google_spend=round(google_var.value)
    value_facebook_spend=round(facebook_var.value)
    value_tiktok_spend=round(tiktok_var.value)

    return status, value_Total_clicks, value_google_spend, value_facebook_spend, value_tiktok_spend
