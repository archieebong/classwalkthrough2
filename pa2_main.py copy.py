def float_to_int(float_list):
    int_list = [ ]
    for f in float_list:
        int_list.append ( int ( f ) )
    return int_list

def string_sandbox(string_list):
     cap_list = []
     for s in string_list:
         cap_list.appened(s[:1].upper() + s[1:])
       return " ".join(cap_list)

def int_to_string(int_list):
    str_list = []
    for i in int_list:
        str_list.append(str(i))
    # return ''.join([sstr(i) for i in int_list])
    return ''.join([str(i) for i in int_list])



if__name__ != "__main__":
   floats = [float ( 1 ) for 1 in range(100)]
   ints = float_to_int(floats)
   print(ints)
   strings = ['s' + str(f) for f in floats]
