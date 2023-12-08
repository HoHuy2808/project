# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
import userandpassword as uap
url = URL(
    user=uap.username,
    password=uap.password,
    account="sh27034.ap-southeast-1",
    schema='TEST_PUBLIC_HH',
    warehouse='DATA_LAKE',
    role='ACCOUNTADMIN'
)
engine = create_engine(url)
connection = engine.connect()
query = '''select * from DATA_LAKE.TEST_PUBLIC_HH.ANALYST'''
data = pd.read_sql(query, connection)