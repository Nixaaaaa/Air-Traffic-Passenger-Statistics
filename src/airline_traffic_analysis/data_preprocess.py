import pandas as pd

class DataPreProcessor:
    """
    This class handles preprocessing tasks like:
    - Converting 'Activity Period' to a proper date format.
    - Handling missing values.
    - Removing duplicates.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()

    def convert_date_columns(self):
        """
        Convert 'Activity Period' column (YYYYMM format) to a proper datetime object and format as YYYY-MM.
        """
        # Convert 'Activity Period' (YYYYMM format) to string and then to datetime (first day of the month)
        self.df['Activity Period'] = pd.to_datetime(self.df['Activity Period'].astype(str) + '01', format='%Y%m%d')

        # If conversion is unsuccessful, we can handle invalid dates
        invalid_dates = self.df[self.df['Activity Period'].isna()]
        if not invalid_dates.empty:
            print("Rows with invalid 'Activity Period' dates:")
            print(invalid_dates)

        # Format the date as 'YYYY-MM'
        self.df['Formatted_Activity_Period'] = self.df['Activity Period'].dt.strftime('%Y-%m')

        return self.df

    def handle_missing_values(self):
        """
        Handle missing values by filling with the previous valid values.
        """
        self.df.fillna(method='ffill',inplace=True)
        return self.df

    def remove_duplicates(self):
        """
        Remove duplicate rows from the dataframe.
        """
        self.df.drop_duplicates(inplace=True)
        return self.df

    def filter_airlines(self, airlines_list=None, max_records=3000):
        """
        Filter dataset by specific airlines and limit number of records.
        """
        if airlines_list:
            self.df = self.df[self.df['Operating Airline'].isin(airlines_list)]
        
        self.df = self.df.head(max_records)
        
        return self.df

    def preprocess(self, airlines_list=None, max_records=4000):
        """
        Runs the full preprocessing pipeline.
        """
        self.df = self.filter_airlines(airlines_list=airlines_list, max_records=max_records)
        self.df = self.convert_date_columns()
        self.df = self.handle_missing_values()
        self.df = self.remove_duplicates()
        # self.df = self.add_additional_features()

        return self.df