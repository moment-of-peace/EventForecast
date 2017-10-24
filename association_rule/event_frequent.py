import os, sys

origin_dir = 'del_201304now/'
new_dir = 'freq_event_state/'
files = os.listdir(origin_dir)
state_dir = {}
country_dir = {}
for file in files:
    with open(origin_dir + file) as f:
        event_dir = {}
        for line in f:
            tmp_content = line.split('\t')
            code = tmp_content[4]
            location = tmp_content[14]
            tmp_loc = location.split(',')
            length = len(tmp_loc)
            state = ''
            if length == 3:
                state = tmp_loc[1]
            elif length == 2:
                state = tmp_loc[0]
            else:
                continue
            country = tmp_loc[length-1]
            if country not in country_dir:
                country_dir[country] = {}
            if state in country_dir[country]:
                tmp_dir = country_dir[country][state]
                if code in tmp_dir:
                    tmp_dir[code] += 1
                else:
                    tmp_dir[code] = 1
            else:
                country_dir[country][state] = {}
                country_dir[country][state][code] = 1
    for country_name,countries in country_dir.items():
        for state_name, states in countries.items():
            dir_path = '%s%s/%s/'%(new_dir, country_name, state_name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            with open(dir_path+file, 'a') as writer:
                for event, freq in states.items():
                    writer.write(event+': '+str(freq)+'\n')
