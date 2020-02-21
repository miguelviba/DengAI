def sep_df_bycity(df):
    """ DataFrame -> 2 Separate Dataframes

    Return two separate DataFrames from Df containing the data associated with the two different cities (sj and iq)

    """

    df_sj = df.loc[df['city'] == 'sj']
    df_iq = df.loc[df['city'] == 'iq']

    return df_sj, df_iq
