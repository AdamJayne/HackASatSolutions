
def parse(c_file):
    with open(c_file) as f:
        file_val = f.readlines()
    print(file_val)
   
    for line in file_val:
        if "Satellite:" in line:
            sat = grab_val(line)

        elif "Latitude:" in line:
            lat = grab_val(line)

        elif "Longitude:" in line:
            lon = grab_val(line)

        elif "Start time GMT:" in line:
            s_time = grab_val(line)

    print(sat, float(lat), float(lon), s_time)

def grab_val(line_str):
    ret = ""
    after_col = False
    for i in line_str:
        if after_col:
            ret = ret + i
        if i == ":":
            after_col = True
       
    ret = ret.replace('\n','')
    ret = ret.strip()
    return ret

if __name__ == "__main__":
    parse('../examples/challenge0.txt')
