# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = pd.read_csv('mvr_synthetic_data.csv')

# COMMAND ----------

df

# COMMAND ----------

number_plates = list(df.NumberPlate.values)

# COMMAND ----------

import pandas as pd
import random
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)

data = []

for number_plate in number_plates:
    for _ in range(random.randint(1, 10)):  # generate between 1 and 10 dates
        random_number_of_days = random.randint(1, 365*3)  # up to 3 years ahead
        random_date = start_date + timedelta(days=random_number_of_days)
        row = {'number_plate': number_plate, 'date': random_date}
        data.append(row)

df_crash = pd.DataFrame(data)

# COMMAND ----------

df_crash['primary_contributor'] = [random.choice(['Yes', 'No']) for x in range(len(df_crash))]

# COMMAND ----------

df_crash['crash_severity'] = [random.choice(['non-fatal','severe', 'extremely']) for x in range(len(df_crash))]

# COMMAND ----------

df_crash

# COMMAND ----------

df_crash.to_csv('crash.csv', index=False)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


