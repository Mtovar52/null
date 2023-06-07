from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:*Mao719*@localhost:3306/books')

meta_data = MetaData()