import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    
    # find all banned users
    not_banned = users[users['banned'] == 'No']

    # remove all banned
    trips = trips[trips['client_id'].isin(not_banned['users_id'])]
    trips = trips[trips['driver_id'].isin(not_banned['users_id'])]
    
    # keep date range and group by
    trips = trips[trips['request_at'].between("2013-10-01", "2013-10-03")]

    # Check if there even is data
    if users.empty or trips.empty or not_banned.empty:
        return pd.DataFrame(columns=['Day','Cancellation Rate'])

    # totals
    trips.loc[trips['status'].str.contains('cancelled'),'status'] = 'cancelled'
    trips = (trips
        .value_counts(subset=['status', 'request_at'])
        .reset_index()
        .pivot_table(
            columns='status', 
            values='count', 
            index='request_at', 
            fill_value=0)
        .reset_index())

    for col in ['cancelled', 'completed']:
        if col not in trips.columns:
            trips[col] = 0.0

    # cancellation rate
    trips['Cancellation Rate'] = (trips['cancelled'] / (trips['cancelled'] + trips['completed'])).round(2)

    return trips.rename(columns={'request_at': 'Day'}, inplace=False)[['Day', 'Cancellation Rate']]