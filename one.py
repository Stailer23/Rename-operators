import glob

def start(rtu,old_name, new_name):
    g = glob.glob(rtu+'\**\*.inf')
    for folder in g:
        with open(folder, 'r') as f:
            old_data = f.read()
        if old_name in old_data:
            new_data = old_data.replace(old_name, new_name)

            with open(folder, 'w') as f:
                f.write(new_data)
        else: continue


