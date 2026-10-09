#%% load lib
import pandas as pd


#%% load data
# 1. load original dataset
df = pd.read_csv('survey_data_updated.csv')

columns_to_split = ['LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith',
                 'PlatformHaveWorkedWith', 'WebframeHaveWorkedWith',
                 'LanguageWantToWorkWith', 'DatabaseWantToWorkWith',
                 'PlatformWantToWorkWith', 'WebframeWantToWorkWith']

# keep only useful columns
columns_to_keep = ['ResponseId',
                 'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith',
                 'PlatformHaveWorkedWith', 'WebframeHaveWorkedWith',
                 'LanguageWantToWorkWith', 'DatabaseWantToWorkWith',
                 'PlatformWantToWorkWith', 'WebframeWantToWorkWith']

df = df[columns_to_keep].copy()
#%%
# 2. define source column -> prefix and output type label
col_config = {
    'LanguageHaveWorkedWith': ('language_worked', 'lang_worked'),
    'DatabaseHaveWorkedWith': ('database_worked', 'database_worked'),
    'PlatformHaveWorkedWith': ('platform_worked', 'platform_worked'),
    'WebframeHaveWorkedWith': ('webframe__worked', 'webframe__worked'),
    'LanguageWantToWorkWith': ('language_want', 'lang_want'),
    'DatabaseWantToWorkWith': ('database_want', 'database_want'),
    'PlatformWantToWorkWith': ('platform_want', 'platform_want'),
    'WebframeWantToWorkWith': ('webframe_want', 'webframe_want')
}

# 3. split each column into multiple columns and add them to df
for orig_col, (prefix, _) in col_config.items():

    split_cols = df[orig_col].astype(str).str.split(';', expand=True)
    # remove whitespaces
    split_cols = split_cols.map(lambda x: x.strip() if isinstance(x, str) else x)
    # rename columns: language_1, language_2, ...
    split_cols.columns = [f'{prefix}_{i + 1}' for i in range(split_cols.shape[1])]
    
    # append the new columns into df
    df = pd.concat([df, split_cols], axis=1)

#%%
# 4. count across the new columns to produce the top 10 summary table
results = []

for _, (prefix, cat_type) in col_config.items():
    # filter all columns created with this prefix
    matched_cols = [c for c in df.columns if c.startswith(f'{prefix}_')]
    
    # flatten the columns into a 1D array
    counts = (
        pd.Series(df[matched_cols].values.ravel())
        .dropna()
        .astype(str)
        .str.strip()
        .loc[lambda s: (s != '') & (s != 'nan') & (s != 'None')]
        .value_counts()
        .head(10)
        .reset_index()
    )
    
    # format to required columns
    counts.columns = ['name', 'count']
    counts['type'] = cat_type
    results.append(counts)

# final combined result
final_df = pd.concat(results, ignore_index=True)

#%%
# save result
final_df.to_csv('cleaned_data.csv', index=False)
print("Done!")
