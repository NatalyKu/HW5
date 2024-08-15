import pandas as pd

def parse_log_line(line: str) -> dict:
    dict_line= {
        'date' : line.split()[0],
        'time': line.split()[1],
        'level': line.split()[2],
        'message':' '.join(line.split()[3:])
            }
    return dict_line

def load_loggs(file_path: str) -> list:
    try:
        with open (file_path, 'r') as logg_file:
            list_logg=[]
            for line in logg_file:
                list_logg.append(parse_log_line(line))
    except FileNotFoundError:
        print (f'Your path {file_path} is wrong')
        
    return list_logg 
 
file_path = input('Write your file path:') 
level = 'INFO'

def filter_logs_by_level(logs: list, level: str) -> list:
    log_level = []
    
    for i in logs_all:
        if i['level'] == level:
            log_level.append(i)
    return log_level

logs_all = load_loggs(file_path)
logs_by_level = filter_logs_by_level(logs_all, level) 

def count_logs_by_level(logs: list) -> dict:
    count_dict = {}
    for i in logs:
        level = i.get('level')
        if level in count_dict:
            count_dict[level] +=1
        else:
            count_dict[level]=1
    
    return count_dict

counts = count_logs_by_level(logs_all)


def display_log_counts(counts: dict, level = None):
    df = pd.DataFrame.from_dict(counts, orient = 'index', columns=['count'] )
    level = input("Choose level:")

    print(f"Деталі логів для рівня:")  
    level_list= filter_logs_by_level(logs_all, level)
    for i in level_list:
        level_string_list =(''. join(i['date'])+ ' '+ ''. join(i['time'])+ ' - '+''. join(i['message']))
        print(level_string_list)
    return df 

print(display_log_counts(counts))