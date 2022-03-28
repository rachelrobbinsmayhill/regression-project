from sklearn.model_selection import train_test_split
import acquire

def wrangle_zillow(df):
    '''
    This function takes in a dataframe, sets a dictionary variable that will be used
    to convert data types, drops all rows with null values within the dataframe, then reassigns
    the datatypes to be more functional for exploring and modeling; making fed_code an object,
    as it will not be used in arithmetic, and converts year_built to an int instead of a float in 
    anticipation of applying arithmetic operations using it. 
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
    

    
    return df



def train_validate_test_split(df, target):
    '''
    This function drops the customer_id column and then splits a dataframe into 
    train, validate, and test in order to explore the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
   
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify = df.target)   
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify = train.target)


    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
    
    return train, validate, test

















