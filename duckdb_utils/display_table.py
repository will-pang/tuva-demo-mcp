import duckdb
import pandas as pd
import matplotlib.pyplot as plt

conn = duckdb.connect('tuva_project_demo.duckdb')

df = conn.execute("SELECT COUNT(DISTINCT person_id) FROM input_layer.eligibility").df()
print(df)