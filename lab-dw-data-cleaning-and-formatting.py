# place for all functions
import pandas as pd

def column_names(df):
    df.columns = [columns.lower().replace(" ", "_") for columns in df.columns]
    return df

def renaming(df):
    df["st"] = df["st"].replace({"WA":"Washington","Cali": "California", "AZ": "Arizona"})
    df["gender"] = df["gender"].replace({"Male": "M", "Femal": "F", "female": "F"})
    df["education"] = df["education"].replace({"Bacherlors": "Bachelor"})
    df["vehicle_class"] = df["vehicle_class"].replace({"Luxury SUV": "Luxury", "Sports Car": "Luxury", "Luxury Car": "Luxury"})
    return df

def data_types(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"])
    df.dropna(subset="number_of_open_complaints", inplace=True)
    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(str)
    df["number_of_open_complaints"] = [i[2:3] for i in df["number_of_open_complaints"]]
    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(int)
    return df

def drop_null(df):
    df.drop(columns="gender", inplace=True)
    df["customer_lifetime_value"] = df["customer_lifetime_value"].fillna(df["customer_lifetime_value"].mean())
    return df

def all_functions(df):
    result = column_names(df)
    result = renaming(result)
    result = data_types(result)
    result = drop_null(result)
    return result


