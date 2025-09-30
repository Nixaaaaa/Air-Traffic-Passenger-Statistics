class DataSummary:
    """
    The DataSummary class generates basic statistics and insights about the data.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def summary_statistics(self):
        """
        Provides basic summary statistics such as mean, median, max, min, and standard deviation for passenger count.
        """
        summary = self.df['Passenger Count'].describe()
        return summary

    def traffic_by_airline(self):
        """
        Returns total traffic by each airline.
        """
        return self.df.groupby('Operating Airline')['Passenger Count'].sum().reset_index()

    def monthly_traffic_summary(self):
        """
        Returns total traffic by month.
        """
        return self.df.groupby('Month')['Passenger Count'].sum().reset_index()

    def year_on_year_growth(self):
        """
        Calculates and returns year-on-year growth of passenger traffic.
        """
        year_data = self.df.groupby('Year')['Passenger Count'].sum().reset_index()
        year_data['Growth'] = year_data['Passenger Count'].pct_change() * 100  # Percent change
        return year_data