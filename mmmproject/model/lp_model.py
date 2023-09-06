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


'''creating a check if the date that was provided by the user is a holiday,
a weekend, month of Jan or July and therefore creating new features'''

# holiday feature
class AddHolidaysTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # This transformer doesn't need to learn any parameters during fitting,
        # so we simply return self.
        return self

    def transform(self, X):
        """Creates a new column with row value = 1 if the day is a Friday or Saturday and 0 if not."""
        df = X.copy()  # Create a copy of the input DataFrame to avoid modifying it directly
        de_holiday_list = []
        for holiday in holidays.Germany(years=[2021,2022,2023]).items():
            de_holiday_list.append(holiday)
        de_holidays_df = pd.DataFrame(de_holiday_list, columns=["date", "holiday"])
        de_holidays_df['date'] = pd.to_datetime(de_holidays_df['date'])
        de_holidays_df.set_index('date', inplace=True)

        at_holiday_list = []
        for holiday in holidays.Austria(years=[2021,2022,2023]).items():
            at_holiday_list.append(holiday)
        at_holidays_df = pd.DataFrame(at_holiday_list, columns=["date", "holiday"])
        at_holidays_df['date'] = pd.to_datetime(at_holidays_df['date'])
        at_holidays_df.set_index('date', inplace=True)

        # add DE holidays to df
        merged_df = df.merge(de_holidays_df, how='left', left_index=True, right_index=True)
        merged_df['de_holiday'] = merged_df.index.isin(de_holidays_df.index).astype(int)
        merged_df.drop(columns=['holiday'], inplace=True)

        # add AT holidays to df
        at_holidays_df['at_holiday'] = 1 # add a 1 column to austrian holidays dataframe to help us merge with DE holidays
        merged_df = merged_df.merge(at_holidays_df[['at_holiday']], how='left', left_index=True, right_index=True)
        merged_df.head() # creates two columns (at_holiday_x, at_holiday_y), we only need one
        merged_df['at_holiday'].fillna(0, inplace=True) # replace NaN (no holiday) with 0
        merged_df['at_holiday'] = merged_df['at_holiday'].astype(int) # convert 1 and 0 to integers

        # combine columns
        merged_df['holiday'] = (merged_df['at_holiday'] | merged_df['de_holiday']).astype(int)
        merged_df = merged_df.drop(columns = ['de_holiday', 'at_holiday']) # drop individual DE and AT rows

        return merged_df[['holiday']]#.reset_index(drop=True)


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

#month feature
class AddMonthsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # This transformer doesn't need to learn any parameters during fitting,
        # so we simply return self.
        return self

    def transform(self, X):
        df = X.copy()  # Create a copy of the input DataFrame to avoid modifying it directly
        df = (df
        .pipe(add_time_features, month=True)
        )

        months_in_a_year = 12

        df['sin_MonthYear'] = np.sin(2*np.pi*(df['month'])/months_in_a_year)
        df['cos_MonthYear'] = np.cos(2*np.pi*(df['month'])/months_in_a_year)
        df.drop(columns=['month'], inplace=True)

        return df[['sin_MonthYear', 'cos_MonthYear']]


def find_optimal_budget(TOTAL_DAILY_BUDGET, Date):
    df=pd.DataFrame([pd.to_datetime(Date)])
    df.set_index(0, inplace=True)
    df['day']=Date
    df['day']=pd.to_datetime(df['day'])

    #treansforming the date df

    time_features = ColumnTransformer(
        [
        ('holidays_pipe', Pipeline([
                ('add_holidays', AddHolidaysTransformer())
        ]), ['day']),
        ('weekends_pipe', Pipeline([
                ('add_weekends', AddWeekendsTransformer())
        ]), ['day']),
        ('months_pipe', Pipeline([
                ('add_months', AddMonthsTransformer())
        ]), ['day'])])

    transformed_df = time_features.fit_transform(df)
    transformed_df = pd.DataFrame(transformed_df, columns = ['holiday', 'weekends', 'sin', 'cos'])
    transformed_df

    # input of total budget
    TOTAL_DAILY_BUDGET= TOTAL_DAILY_BUDGET

    # model cvxpy

    # Variables
    google   = cp.Variable(pos=True)
    facebook = cp.Variable(pos=True)
    tiktok  = cp.Variable(pos=True)

    # Constraint
    constraint = [google + facebook + tiktok <= TOTAL_DAILY_BUDGET, google>=TOTAL_DAILY_BUDGET*0.04769543069031596, facebook>=TOTAL_DAILY_BUDGET*0.16612285992471154, tiktok>=TOTAL_DAILY_BUDGET*0.0361817093849725]

    betas=[-164.052961,-372.686127,265.076699,-23.341808,1.144179,5.504117,1.483814]
    intercept=238.56530283612096
    # Objective
    obj= cp.Maximize(intercept+betas[0] * transformed_df['holiday'][0] +betas[1] * transformed_df['weekends'][0] +betas[2] *transformed_df['sin'][0]+ betas[3] *transformed_df['cos'][0]+ betas[4] *(facebook)+betas[5] *(google)+betas[5] *(tiktok))

    # Solve
    prob = cp.Problem(obj, constraint)
    prob.solve(solver='ECOS', verbose=False)

    # Print solution
    status=prob.status
    value_Total_sales=prob.value
    value_google_spend=google.value
    value_facebook_spend=facebook.value
    value_tiktok_spend=tiktok.value

    return status, value_Total_sales, value_google_spend, value_facebook_spend, value_tiktok_spend
