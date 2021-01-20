import csv
def save_to_file (lis,num):
    default_row=["SECRETARIAT","PARTICIPATING MEMBERS","OBSERVING MEMBERS"]
    file= open(f"{num}.csv",mode="w",encoding='utf8')
    writer=csv.writer(file)
    writer.writerow(default_row)
    for obj in lis:
        writer.writerow(obj)
    return