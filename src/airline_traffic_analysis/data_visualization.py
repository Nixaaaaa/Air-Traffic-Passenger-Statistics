import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    """
    The DataVisualizer class provides functions to create various visualizations
    for the given airline traffic DataFrame.
    
    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataset containing airline passenger traffic data.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def plot_passenger_count_over_time(self):
        """
        Plot passenger count over time using a line plot.

        X-axis: Activity Period (time)
        Y-axis: Passenger Count
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=self.df, x='Activity Period', y='Passenger Count')
        plt.title('Passenger Count Over Time')
        plt.xlabel('Date')
        plt.ylabel('Passenger Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_passenger_count_by_airline(self, top_n=10):
        """
        Plot a bar chart showing the total passenger count by airline.
        
        Parameters
        ----------
        top_n : int, optional (default=10)
            Number of top airlines to display, sorted by passenger count.
        """
        # Group by airline and sum passenger counts
        airline_passenger_counts = (
            self.df.groupby('Operating Airline')['Passenger Count']
            .sum()
            .reset_index()
        )

        # Select top N airlines
        top_airlines = airline_passenger_counts.nlargest(top_n, 'Passenger Count')

        # Create bar plot
        plt.figure(figsize=(12, 6))
        sns.barplot(data=top_airlines, x='Operating Airline', y='Passenger Count')
        plt.title(f'Total Passenger Count by Airline (Top {top_n} Airlines)')
        plt.xlabel('Operating Airline')
        plt.ylabel('Total Passenger Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_monthly_traffic_trend(self):
        """
        Plot monthly passenger traffic trends over multiple years.
        
        X-axis: Month
        Y-axis: Passenger Count
        Hue: Year (different line per year)
        """
        # Aggregate traffic by year and month
        monthly_traffic = (
            self.df.groupby(['Year', 'Month'])['Passenger Count']
            .sum()
            .reset_index()
        )

        # Line plot for trends
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=monthly_traffic, x='Month', y='Passenger Count', hue='Year', marker='o')
        plt.title('Monthly Traffic Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Passenger Count')
        plt.tight_layout()
        plt.show()

    def plot_year_month_heatmap(self):
        """
        Create a heatmap of passenger traffic by Year and Month.

        X-axis: Month
        Y-axis: Year
        Values: Total passenger count
        """
        # Create pivot table (Year vs Month, with passenger sums)
        traffic_pivot = self.df.pivot_table(
            index='Year', columns='Month', values='Passenger Count', aggfunc='sum'
        )

        # Heatmap visualization
        plt.figure(figsize=(14, 8))
        sns.heatmap(
            traffic_pivot, annot=True, cmap='YlGnBu', fmt='g',
            linewidths=0.5, annot_kws={"size": 10}
        )
        plt.title('Yearly Traffic Heatmap by Month')
        plt.xlabel('Month')
        plt.ylabel('Year')
        plt.tight_layout()
        plt.show()
