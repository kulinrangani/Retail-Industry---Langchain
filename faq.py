from langchain_openai import OpenAI
from langchain_community.utilities import SQLDatabase

llm = OpenAI(model="gpt-4o-mini",temperature=0, verbose=True)
# res = llm.invoke("What is Langchain?")

db_user = "root"
db_password = ""
db_host = "localhost"
db_name = "cool_tshirts"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)
print(db.table_info)

from langchain_experimental.sql import  SQLDatabaseChain

sql_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
qns1 = sql_chain("How many tshirts do we have left for nike in extra small size for black color?")