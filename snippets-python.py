Snippets - Python

#################
PANDAS
#################

BASICS

# Work-flow for cleaning data that are given to you as separate test and train sets (e.g. on Kaggle) - put test and train datsets together, then split
train_labels = train.pop('SalePrice')
features = pd.concat([train, test], keys=['train', 'test'])
# Once cleaned, use this to split again: 
train_features = features.loc['train'].drop('Id', axis=1).select_dtypes(include=[np.number]).values
test_features = features.loc['test'].drop('Id', axis=1).select_dtypes(include=[np.number]).values

# concat tables and reset index to run over the seam: 
pd.concat(['train', 'test'], ignore_index = True)


##################
data = pandas.read_csv(file, sep='\t', quoting=csv.QUOTE_NONE,
                           names=["label", "message"])
data.groupby('label').describe()
# This gives sumamry stats, like doing df %>% group_by(blah) %>% summarise() in R


# Count the uniques for each column for a given dataframe
def df_uniques(df):
    print('Col name,', 'Number of nulls,', 'Number of unique values')
    #print(df.name())
    for col in df:
        print(col, df[col].shape[0] - df[col].count(), df[col].unique().shape[0])
    print('\n')
    return

# This does the same but gives a sorted list (ordered by number of nulls):
def df_uniques(df):
    print('Col name,', 'Number of nulls,', 'Number of unique values', '% of nulls')
    list_of_features = []
    for col in df:
        l = [col, df[col].shape[0] - df[col].count(), df[col].unique().shape[0], '%.3f' %((df[col].shape[0] - df[col].count()) / df[col].shape[0])]
        list_of_features.append(l)
    # Sort by the number of NULLs: 
    list_of_features = sorted(list_of_features, key = lambda x: x[1], reverse = True)
    return list_of_features

# To call the above, for only a few columns:
df_uniques(df[['col_a', 'col_b']])

# List of columns with nulls in:
[col for col in df.columns if df[col].isnull().any()]

# Rows with any nulls
df.loc[:, df.isnull().any()]

# Rows with nulls everywhere (returned as a new df)
nans = df.loc[df.isnull().all(1)]

# Comparing list of headers of test and train datasets (i.e. find which fields are absent in test set, and hence which are the target fields)
headers_test = list(test)
headers_train = list(train)
[field for field in headers_test if field not in headers_train]

# Drop duplicates
def df_drop_duplicates(df):
    rows_init = df.shape[0]
    df = df.drop_duplicates()
    rows_unique = df.shape[0]
    duplicates_removed = rows_init - rows_unique
    print(duplicates_removed, 'duplicates removed, ', rows_unique, ' rows remaining')
    return df

# Drop NAs - drop rows where Latitude and/or Longitude are NULL
stations.dropna(subset=['Latitude', 'Longitude'], how='all', inplace = True)


# Frequencies of unique values of a single column: 
data['Title'].value_counts()

# return a series from a single column:
train['Title']
# return a df from a single column: 
train[['Title']]

# Make several changes at once in a data column (example: replace NESW with +-, useful for latlon coords): 
def updatestring(string):
    import re
    rdict = rdict = {'N ': '+','S ': '-','E ': '+','W ': '-'}
    robj = re.compile('|'.join(rdict.keys()))
    replaced = robj.sub(lambda x: rdict[x.group(0)], string)
    return replaced
# then: 
df['latlon'] = df['latlon'].apply((lambda x: updatestring(x)))

######### Dates

# Set a column as a date:
df['date'] = pd.to_datetime(df['date'])

###### percentages
# If we have a field that has xx.x%, remove this symbol:
df['int_rate'] = df['int_rate'].str.extract('(\d+.\d)')

## Fill NAs with modeal value
most_freq = df[col].dropna().mode()[0]
df[col].fillna(most_freq)

# Fill every column with the modal value
df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))


#################
Numpy
#################

### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features

# Filter an array
outlier_bonus = data[data > 1e7][1]



#################
Dictionaries
#################

# Filter a dictionary
#  based on value criteria - e.g. bonus is a given value
data_dict_filter = {k:v for (k,v) in data_dict.items() if v['bonus'] == outlier_bonus}

# based on key criteria - e.g. key begins with 'E'
data_dict_filter = {k:v for (k,v) in data_dict.items() if str(k)[:1] == 'E'}


#################
Lists
#################

# find index of smallest value of a list - http://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
import numpy as np
index_min = np.argmin(values)
# or:
index_min = min(xrange(len(values)), key=values.__getitem__)
