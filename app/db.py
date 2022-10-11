from os import environ

import sqlalchemy as sa
from sqlalchemy import Text, create_engine
from sqlalchemy.orm import sessionmaker

# Database Connection
DATABASE_URL = 'mysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'.format(
    **environ)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)

metadata = sa.MetaData()
metadata.bind = engine

data_backup = sa.Table(
    'data_backup',
    metadata,
    sa.Column('first_name', Text),
    sa.Column('last_name', Text),
    sa.Column('email', Text),
    sa.Column('sold_at', sa.DateTime()),
    sa.Column('make', Text),
    sa.Column('model', Text),
    sa.Column('value', sa.Float),
)
