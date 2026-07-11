row_data=[
{"Name":"A","Marks":85},
{"Name":"B","Marks":None},
{"Name":"C","Marks":90}
    ]

data_warehouse=row_data
clean_data=[]
for record in data_warehouse:
    if record["Marks"] is not None:
        clean_data.append(record)


print("ELT Transformed data :",clean_data)
