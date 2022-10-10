import pandas as pd

from app.db import engine

CSV_FILE_NAME = "dataset.csv"
DB_TABLE_NAME = "Buyers"


def seeding_database() -> None:
    """
    Seeds the database using a csv file.
    """
    try:
        print("--Started seeding the database..")
        dataframe = pd.read_csv(f"{CSV_FILE_NAME}",
                                sep=',',
                                quotechar='\'',
                                encoding='utf8')  # To read the CSV file
        # To export all the data from the CSV to the DB
        dataframe.to_sql(DB_TABLE_NAME, con=engine, index=False, if_exists='replace')
        print(f"--Successfully seeded the database using the {CSV_FILE_NAME}")
    except Exception as e:
        print('Seeding failed, error msg: ', str(e))


if __name__ == "__main__":
    seeding_database()
