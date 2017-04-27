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

# List of columns with nulls in:
[col for col in df.columns if df[col].isnull().any()]

# Rows with any nulls
df.loc[:, df.isnull().any()]

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


# concat tables and reset index to run over the seam: 
pd.concat(['train', 'test'], ignore_index = True)

# Frequencies of unique values of a single column: 
data['Title'].value_counts()


# return a series from a single column:
train['Title']
# return a df from a single column: 
train[['Title']]


#################
Numpy
#################

### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features

# Filter an array
outlier_bonus = data[data > 1e7][1]


# Filter a dictionary
#  based on value criteria - e.g. bonus is a given value
data_dict_filter = {k:v for (k,v) in data_dict.items() if v['bonus'] == outlier_bonus}

# based on key criteria - e.g. key begins with 'E'
data_dict_filter = {k:v for (k,v) in data_dict.items() if str(k)[:1] == 'E'}



# find index of smallest value of a list - http://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
import numpy as np
index_min = np.argmin(values)
# or:
index_min = min(xrange(len(values)), key=values.__getitem__)

