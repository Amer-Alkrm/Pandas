from datetime import datetime
from typing import Callable

import pandas as pd
from pandas import DataFrame

from app.db import Session, data_backup, engine, metadata
from bin.db_seeder import CSV_FILE_NAME, DB_TABLE_NAME


def display_helpful_information(csv_file_name: str) -> None:
    """
    Displays helpful information for the provided csv file.
    """
    try:
        print(f"--Displaying helpful information for the {csv_file_name}..")
        dataframe = pd.read_csv(f"{csv_file_name}")  # To read the CSV file
        display_info = [
            {'operation': 'Models count per make',
             'func': lambda df: df.groupby(['make']).count()['model']},
            {'operation': 'Total number of make',
             'func': lambda df: df['make'].count()},
            {'operation': 'Maximum value of a model per make',
             'func': lambda df: df.groupby(['make', 'model']).max()['value']},
            {'operation': 'Count of the model per model',
             'func': lambda df: df.groupby("model").agg("count")}
        ]
        for display in display_info:
            _display_information(df=dataframe, **display)
        print(f"--Information displayed successfully.")

    except Exception as e:
        print('An error occured while displaying information, failure details: ', str(e))


def _display_information(df: DataFrame, operation: str, func: Callable[..., DataFrame]) -> None:
    print(f"----{operation}: ")
    df_result = func(df)
    print(df_result)


def create_backup(table_name: str) -> None:
    """
    Creates a backup for the table.
    """
    print(f"Creating backup for {table_name} table..")
    try:
        with engine.connect() as conn:
            result = conn.execute(f"select * from {table_name}")

            insert_data = []
            for car_data in result:
                data = {**car_data._mapping}
                # execute many data at once for faster insertion.
                data['sold_at'] = datetime.fromisoformat(data['sold_at'])
                insert_data.append(data)

            conn.execute(data_backup.insert(), insert_data)
        print(f"Backup created successfully for {table_name} table.")
    except Exception as e:
        print(
            f"Failed to create backup for {table_name} table, failure details: ", str(e))


def modify_data(table_name: str, number_of_records: int) -> None:
    """
    Randomly modifies value column in the table for a number of records.
    """
    print(
        f"Modifying value column to 55555 for {number_of_records} random records in the {table_name} table...")
    with Session.begin() as conn:
        try:
            conn.execute(
                f"UPDATE {table_name} SET value = 55555 ORDER BY RAND() LIMIT 2251")
            print(f"{number_of_records} records modified successfully!")
        except Exception as e:
            print('An error occured while modifying records, failure details: ', str(e))
            print('Rolling back.')
            conn.rollback()


def update_backup(table_name: str) -> None:
    """
    Updates the backup table by deleting all the records and reinserting them.\
         Incase of a failure, a rollback will happen.
    """
    with Session.begin() as conn:
        try:
            print("Updating the backup table..")
            conn.execute(data_backup.delete())
            result = conn.execute(f"select * from {table_name}")

            insert_data = []
            for car_data in result:
                data = {**car_data._mapping}
                data['sold_at'] = datetime.fromisoformat(data['sold_at'])
                insert_data.append(data)

            conn.execute(data_backup.insert(), insert_data)
            print("The backup table is updated successfully!")
        except Exception as e:
            print("An error occured while updating the backup, failure details: ", str(e))
            print("Rolling back.")
            conn.rollback()


if __name__ == "__main__":
    # Task2 Part1
    display_helpful_information(CSV_FILE_NAME)

    # Task2 Part2
    # To create table
    metadata.create_all(engine)
    create_backup(table_name=DB_TABLE_NAME)
    modify_data(table_name=DB_TABLE_NAME, number_of_records=2251)
    update_backup(table_name=DB_TABLE_NAME)
