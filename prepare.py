from imports import *
import acquire

def wrangle_zillow(df):
    '''
    This function takes in a dataframe, sets a dictionary variable that will be used
    to convert data types, drops all rows with null values within the dataframe, then reassigns
    the datatypes to be more functional for exploring and modeling; making state_county_code an object,
    as it will not be used in arithmetic, and converts year_built to an int instead of a float in 
    anticipation of applying arithmetic operations using it. It then creates binned categorical columns 
    for home_sizes using square_feet, total_rooms using bedrooms and bathrooms,  bedroom_bins  and 
    bathroom_bins grouping bedrooms and bathrooms individually into small, medium, large and extra-large categories.
    '''
    
    convert_dict = {'state_county_code': object,
                'year_built': int
               }
     
    # drop county_id column as it is not needed due to state_county_code column
    df = df.drop(['county_id'], axis=1)
    
    # drop rows with nulls
    df = df.dropna(axis = 0)
    
    # convert datatypes
    df = df.astype(convert_dict)
    
    # Make categorical column for location based upon the name of the county that belongs to the cooresponding state_county_code (fips code)
    df['county_code_bin'] = pd.cut(df.state_county_code, bins=[0, 6037.0, 6059.0, 6111.0], 
                             labels = ['Los Angeles County', 'Orange County',
                             'Ventura County'])
   
    # Make dummy columns for state_county_code using the binned column for processin gin modeling later. 
    dummy_df = pd.get_dummies(df[['county_code_bin']], dummy_na=False, drop_first=[True])
    
    # Add dummy columns to dataframe
    df = pd.concat([df, dummy_df], axis=1)

    # Make categorical column for square_feet.
    df['home_sizes'] = pd.cut(df.square_feet, bins=[0, 1800, 4000, 6000, 25000], 
                             labels = ['Small: 0 - 1799sqft',
                             'Medium: 1800 - 3999sqft', 'Large: 4000 - 5999sqft', 'Extra-Large: 6000 - 25000sqft'])
    
    # Make categorical column for total_rooms, combining number of bedrooms and bathrooms.
    df['total_rooms'] = df['bedrooms'] + df['bathrooms']
    
    # Make categorical column for bedrooms.
    df['bedroom_bins'] = pd.cut(df.bedrooms, bins=[0, 2, 4, 6, 15], 
                             labels = ['Small: 0-2 bedrooms',
                             'Medium: 3-4 bedrooms', 'Large: 5-6 bedrooms', 'Extra-Large: 7-15 bedrooms'])
    
    # Make categorical column for square_feet.
    df['bathroom_bins'] = pd.cut(df.bathrooms, bins=[0, 2, 4, 6, 15], 
                             labels = ['Small: 0-2 bathrooms',
                             'Medium: 3-4 bathrooms', 'Large: 5-6 bathrooms', 'Extra-Large: 8-15 bathrooms'])

    
    return df




def split_data(df):
    '''
    This function drops the customer_id column and then splits a dataframe into 
    train, validate, and test in order to explore the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
   
    train_val, test = train_test_split(df, train_size=0.8,random_state=123)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=123)
    
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
    
   
    return train, validate, test











