# STANDARD LIBRARIES
import os

# THIRD PARTY LIBRARIES
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# LOCAL LIBRARIES
import env


def get_zillow_data(use_cache=True):
    '''
    This function acquires the zillow database in SQL. The function requires the
    use of a personalized .env file that contains the user, password, and host credentials.
    It acquires the bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, 
    yearbuilt, taxamount, and fips from the zillow database for all 'Single Family Residential' 
    properties. It identifies the Single Family Residential Properties by filtering 
    for for only those with the '261' propertylandusetypeid that matches the propertylandusetypeid 
    identifying as single-family residential homes in the propertylandusetype table. 
    It returns a dataframe and caches the dataframe 
    (saving it to a .csv file, titled: 'zillow_values.csv'), 
    for faster processing after initial acquisition. The resulting dataframe 
    contains all the selected columns. 
    '''
    
    filename = 'zillow_values.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/zillow'
    query ='''
    SELECT bedroomcnt AS bedrooms, 
        bathroomcnt AS bathrooms, 
        calculatedfinishedsquarefeet AS square_feet, 
        taxvaluedollarcnt AS assessed_value, 
        yearbuilt AS year_built, 
        taxamount AS tax_amount, 
        fips AS state_county_code,
        regionidcounty AS county_id
    FROM properties_2017
    JOIN predictions_2017 USING (parcelid)
    JOIN propertylandusetype USING(propertylandusetypeid)
    WHERE propertylandusedesc IN ("Single Family Residential",                       
                                  "Inferred Single Family Residential")
                                  AND predictions_2017.transactiondate LIKE '2017%%'
    
    
    '''
            

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df