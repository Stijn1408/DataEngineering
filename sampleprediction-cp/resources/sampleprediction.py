def sample_plot(df):
    """Take a random sample with size n"""
    data_sample = df.sample(axis = 0, n = 5)
    return data_sample
