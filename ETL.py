row_data=[
{"Name":"A","Marks":85},
{"Name":"B","Marks":None},
{"Name":"C","Marks":90}
    ]

clean_data=[]
for record in row_data:
    if record["Marks"] is not None:
        clean_data.append(record)

data_warehouse=clean_data
print("ETL loaded data :",data_warehouse)
