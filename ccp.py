import pandas as pd

corona_df['new_data'] = pd.to_datetime(corona_df['date'])
corona_df.set_index('new_date', inplace=True)

print(corona_df)