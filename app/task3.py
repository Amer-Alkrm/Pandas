import pandas as pd

from bin.db_seeder import CSV_FILE_NAME


def apply_operations() -> None:
    """Applies multiple operations on the dataset provided.
    """
    print(f"--Applying different operations on the {CSV_FILE_NAME}..")
    dataframe = pd.read_csv(f"{CSV_FILE_NAME}")  # To read the CSV file

    print("Converting sold_at datetime to (Y-m-d H:m:s) format.")
    dataframe['sold_at'] = pd.to_datetime(dataframe['sold_at']).dt.strftime('%Y-%m-%d %H:%m:%s')
    dataframe['sold_at'].head(5)

    print("Display data in the following groupings: ")
    display_data_groups(dataframe)

    print("Removing all models with value less than 11,000")
    print(dataframe[dataframe['value'] < 11000])

    print("Sorting models by make and value")
    print(dataframe.sort_values(by=['make', 'value'])[['model']])

    print("Dropping make column")
    print(dataframe.drop(['make'], axis=1))

    dataframe_new = pd.DataFrame([dataframe.make, dataframe.model]).transpose()
    print(pd.concat([dataframe, dataframe_new]))


def display_data_groups(df: pd.DataFrame) -> None:
    print("Models count per make.")
    print(df.groupby('make').count()['model'])
    print("Highest value of each model.")
    print(df.groupby('model').max()['value'])
    print("Lowest value of per make.")
    print(df.groupby('make').min()['value'])
    print("Highest model value.")
    highest_value = df['value'].agg('max')
    print(df.loc[df['value'] == highest_value]['model'])
    print("Average model price per make.")
    print(df.groupby('make').mean()['value'])


if __name__ == "__main__":
    apply_operations()
