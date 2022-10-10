from os import environ
from typing import List

from app.db import engine
from bin.db_seeder import DB_TABLE_NAME


def create_view(view_name: str, selectors: List[str], group_by: List[str]) -> None:
    """Creates a view.

    Args:
        :param view_name: View name to be created
        :type view_name: str
        :param selectors: Columns and aggregate functions selectors.
        :type selectors: List[str]
        :param group_by: Columns to be grouped by
        :type group_by: List[str]
    """
    selectors_str = ', '.join(selectors)
    grouped_by_str = ', '.join(group_by)

    try:
        print(
            f"--Creating {view_name} view with selectors: {selectors} and grouped_by: {group_by}..")
        with engine.connect() as conn:
            conn.execute(f"CREATE VIEW {view_name} as SELECT {selectors_str}"
                         f" FROM {environ['DB_NAME']}.{DB_TABLE_NAME} GROUP BY {grouped_by_str};")

        print(f"--Successfully created {view_name} view.")
    except Exception as e:
        print(f'Failed to create {view_name} view, error msg: ', str(e))


if __name__ == "__main__":
    create_view(view_name='models_count_per_make', selectors=[
                'make', 'count(model)'], group_by=['make'])
    create_view(view_name='max_and_min_value_per_make', selectors=[
                'make', 'max(value)', 'min(value)'], group_by=['make'])
    create_view(view_name='max_and_min_value_per_model_and_make', selectors=[
                'model', 'make', 'max(value)', 'min(value)'], group_by=['model', 'make'])
