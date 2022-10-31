import time
array0 = ["16.379760,102.845843", "16.379708,102.845834",
          "16.379706,102.845772", "16.379744,102.845774"]
array1 = ["16.412454,102.829174",
          "16.413205,102.829218", "16.413204,102.828986"]
array2 = ["16.413213,102.828875", "16.413200,102.829212",
          "16.412959,102.829216", "16.412916,102.829471"]
array3 = ["16.413213,102.828875", "16.413200,102.829212",
          "16.413508,102.829294", "16.413474,102.829434"]
array4 = ["16.412821,102.829207",
          "16.412996,102.829230", "16.412947,102.829475"]
array5 = ["16.413644,102.828873", "16.413511,102.829431"]
array6 = ["16.413644,102.828873",
          "16.413536,102.829268", "16.413328,102.829249"]
array7 = ["16.411176,102.828912", "16.411245,102.828928",
          "16.411204,102.829184", "16.411280,102.829204"]
array8 = ["16.411161,102.828898",
          "16.410906,102.828855", "16.410928,102.828746"]
array9 = ["16.411162,102.828910",
          "16.410911,102.828861", "16.410927,102.828745"]


def changespot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng):
    lat_spot = lat - past_lat
    lng_spot = lng - past_lng
    old_mark_lat = old_mark_lat + lat_spot
    old_mark_lng = old_mark_lng + lng_spot
    mark_lat = mark_lat + lat_spot
    mark_lng = mark_lng + lng_spot
    new_mark_lat = new_mark_lat + lat_spot
    new_mark_lng = new_mark_lng + lng_spot
    print("mark_lat = "+str(mark_lat)+" + " + str(lat_spot)+" past_lat "+str(past_lat))
    print("mark_lng = "+str(mark_lng)+" + " + str(lng_spot)+" past_lng "+str(past_lng))
    print("change_spot")
    return ((float(old_mark_lat)), (float(old_mark_lng)), (float(mark_lat)), (float(mark_lng)), (float(new_mark_lat)), (float(new_mark_lng)))


def check_spot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng):
    if (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003):
        print("turn")
        return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng
        
    
        
    elif (mark_lng - 0.000026 < old_mark_lng - 0.000026 and mark_lng + 0.000026 < old_mark_lng + 0.000026 and (old_mark_lat < mark_lat or old_mark_lat > mark_lat)):
        print('Wp01 \n'+str(lat)+"\n"+str(lng))
        print(old_mark_lng + 0.000026)
        print(mark_lng - 0.000026)
        if (lng < mark_lng - 0.000026 or old_mark_lng + 0.000026 > lng):
            print('Wp1')
            old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng = changespot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng)
            return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng
        elif ( old_mark_lng + 0.000026 > lng > mark_lng - 0.000026 ):
            print(old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng)
            out_line(lat, lng, mark_lat, mark_lng, old_mark_lat, old_mark_lng)
            return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng
    elif (mark_lng - 0.000026 > old_mark_lng - 0.000026 and mark_lng + 0.000026 > old_mark_lng + 0.000026 and (old_mark_lat < mark_lat or old_mark_lat > mark_lat)):
        if (lng < mark_lng + 0.000025 or lng > old_mark_lng - 0.000025):
            old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng = changespot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng)
            return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng
        else:
            print('Warp2')
    elif (mark_lat - 0.000026 < old_mark_lat - 0.000026 and mark_lat + 0.000026 < old_mark_lat + 0.000026  and (old_mark_lng < mark_lng or old_mark_lng > mark_lng)):
        if (lat < mark_lat - 0.000026 or lat > old_mark_lat + 0.000026 ):
            old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng = changespot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng)
            return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng
        else:
            print('Warp3') 
    elif (mark_lat - 0.000026 > old_mark_lat - 0.000026 and mark_lat + 0.000026 > old_mark_lat + 0.000026  and (old_mark_lng < mark_lng or old_mark_lng > mark_lng)):
        if (lat < mark_lat + 0.000026 or lat > old_mark_lat - 0.000026):
            old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng = changespot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng)
            return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng
        else:
            print('Warp4')
    else:
        print('Warp')
        return old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng


def out_line(lat, lng, mark_lat, mark_lng, old_mark_lat, old_mark_lng):
    if (mark_lng - 0.000026 < old_mark_lng - 0.000026 and mark_lng + 0.000026 < old_mark_lng + 0.000026 and old_mark_lat > mark_lat ):
        if (mark_lng - 0.000026 < lng < mark_lng + 0.000026):
            print("forward")
            return ()
        elif (lng > mark_lng + 0.000026 and (old_mark_lng + 0.000026 > lng > mark_lng - 0.000026 or old_mark_lng - 0.000026 > lng > mark_lng + 0.000026)):
            print("s_way_r")
            return ()
    elif (mark_lng - 0.000026 < old_mark_lng - 0.000026 and mark_lng + 0.000026 < old_mark_lng  + 0.000026 and old_mark_lat < mark_lat ):
        if (mark_lng - 0.000026 < lng < mark_lng + 0.000026 and (old_mark_lng + 0.000026 > lng > mark_lng - 0.000026 or old_mark_lng - 0.000026 > lng > mark_lng + 0.000026)):
            print("forward")
            return ()
        elif (lng > mark_lng + 0.000026):
            print("n_way_l")
            return ()
    elif (mark_lng - 0.000026 < old_mark_lng - 0.000026 and mark_lng + 0.000026 < old_mark_lng + 0.000026 and old_mark_lat > mark_lat ):
        if (mark_lng - 0.000026 < lng < mark_lng + 0.000026 and (old_mark_lng + 0.000026 > lng > mark_lng - 0.000026 or old_mark_lng - 0.000026 > lng > mark_lng + 0.000026)):
            print("forward ")
            return ()
        elif (lng < mark_lng - 0.000026 and (old_mark_lng + 0.000026 > lng > mark_lng - 0.000026 or old_mark_lng - 0.000026 > lng > mark_lng + 0.000026)):
            print("s_way_l")
            return ()
    elif (mark_lng - 0.000026 < old_mark_lng - 0.000026 and mark_lng + 0.000026 < old_mark_lng  + 0.000026 and old_mark_lat < mark_lat ):
        if (mark_lng - 0.000026 < lng < mark_lng + 0.000026):
            print("forward")
            return ()
        elif (lng < mark_lng - 0.000026 and (old_mark_lng + 0.000026 > lng > mark_lng - 0.000026 or old_mark_lng - 0.000026 > lng > mark_lng + 0.000026)):
            print("n_way_r")
            return ()
    elif (mark_lat - 0.000026 <old_mark_lat - 0.000026 and mark_lat + 0.000026<old_mark_lat + 0.000026 and old_mark_lng > mark_lng ):
        if (mark_lat - 0.000026 < lat < mark_lat + 0.000026):
            print("forward")
            return ()
        elif (lat > mark_lat + 0.000026 and (old_mark_lat + 0.000026 > lat > mark_lat - 0.000026 or old_mark_lat - 0.000026 > lat > mark_lat + 0.000026)):
            print("e_way_l")
            return ()
    elif (mark_lat - 0.000026 <old_mark_lat - 0.000026 and mark_lat + 0.000026<old_mark_lat  + 0.000026 and old_mark_lng < mark_lng):
        if (mark_lat - 0.000026 < lat < mark_lat + 0.000026):
            print("forward")
            return ()
        elif (lat > mark_lat + 0.000026 and (old_mark_lat + 0.000026 > lat > mark_lat - 0.000026 or old_mark_lat - 0.000026 > lat > mark_lat + 0.000026)):
            print("w_way_r")
            return ()
    elif (mark_lat - 0.000026 < old_mark_lat - 0.000026 and mark_lat + 0.000026 < old_mark_lat + 0.000026 and old_mark_lng < mark_lng ):
        if (mark_lat - 0.000026 < lat < mark_lat + 0.000026):
            print("forward")
            return ()
        elif (lat < mark_lat + 0.000026 and (old_mark_lat + 0.000026 > lat > mark_lat - 0.000026 or old_mark_lat - 0.000026 > lat > mark_lat + 0.000026)):
            print("e_way_r")
            return ()
    elif (mark_lat - 0.000026 < old_mark_lat - 0.000026 and mark_lat + 0.000026 <old_mark_lat  + 0.000026 and old_mark_lng < mark_lng):
        if (mark_lat - 0.000026 < lat < mark_lat + 0.000026):
            print("forward")
            return ()
        elif (lat < mark_lat + 0.000026 and (old_mark_lat + 0.000026 > lat > mark_lat - 0.000026 or old_mark_lat - 0.000026 > lat > mark_lat + 0.000026)):
            print("w_way_l")
            return ()
    


def active(array):
    cnt = 0
    print(array)
    array_past = array[0].split(",")
    past_lat = (float(array_past[0]))
    past_lng = (float(array_past[1]))
    mark_c = open("save.txt", "r+")
    gps = mark_c.read()
    markC_array = gps.split("\n")
    for mark in array:
        array_mark = mark.split(",")
        mark_lat = (float(array_mark[0]))
        mark_lng = (float(array_mark[1]))
        if (mark == array[0]):
            old_array_mark = array[0].split(",")
        elif (mark != array[0]):
            old_array_mark = array[cnt-1].split(",")
        old_mark_lat = (float(old_array_mark[0]))
        old_mark_lng = (float(old_array_mark[1]))
        old_lat = (float(old_array_mark[0]))
        old_lng = (float(old_array_mark[1]))
        if (mark == array[-1]):
            new_array_mark = array[-1].split(",")
        elif (mark != array[-1]):
            new_array_mark = array[cnt+1].split(",")
        new_mark_lat = (float(new_array_mark[0]))
        new_mark_lng = (float(new_array_mark[1]))
        new_lat = (float(array_mark[0]))
        new_lng = (float(array_mark[1]))
        for y in markC_array:
            time.sleep(0.1)
            gps_s = y.split(":")
            lat = (float(gps_s[0]))
            lng = (float(gps_s[1]))
            print("past = "+str(past_lat)+" "+str(past_lng))
            old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng = check_spot(lat, lng, old_mark_lat, old_mark_lng, mark_lat, mark_lng, new_mark_lat, new_mark_lng, past_lat, past_lng)
            print("old_mark = "+str(old_mark_lat)+" "+str(old_mark_lng))
            print("mark = "+str(mark_lat)+" "+str(mark_lng))
            print("past = "+str(past_lat)+" "+str(past_lng))
            if (mark != array[0]):
                print(str(lat)+"    "+str(lng))
                if (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and mark == array[-1]):
                    # stop
                    print(str(cnt)+" true")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lat < lat and old_mark_lng - 0.00015 <= lng <= old_mark_lng + 0.00015 and new_mark_lng > lng and new_mark_lat - 0.00015 <= lat <= new_mark_lat + 0.00015 and old_lat < new_lat and new_lng - 0.00005 <= old_lng <= new_lng + 0.00005):
                    # GO_N_Right
                    print(str(cnt)+" working NR")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lat < lat and old_mark_lng - 0.00015 <= lng <= old_mark_lng + 0.00015 and new_mark_lng < lng and new_mark_lat - 0.00015 <= lat <= new_mark_lat + 0.00015 and old_lat < new_lat and new_lng - 0.00005 <= old_lng <= new_lng + 0.00005):
                    # GO_N_Left
                    print(str(cnt)+" working NL")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lat > lat and old_mark_lng - 0.00015 <= lng <= old_mark_lng + 0.00015 and new_mark_lng < lng and new_mark_lat - 0.00015 <= lat <= new_mark_lat + 0.00015 and old_lat > new_lat and new_lng - 0.00005 <= old_lng <= new_lng + 0.00005):
                    # GO_S_Right
                    print(str(cnt)+" working SR")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lat > lat and old_mark_lng - 0.00015 <= lng <= old_mark_lng + 0.00015 and new_mark_lng > lng and new_mark_lat - 0.00015 <= lat <= new_mark_lat + 0.00015 and old_lat > new_lat and new_lng - 0.00005 <= old_lng <= new_lng + 0.00005):
                    # GO_S_Left
                    print(str(cnt)+" working SL")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lng < lng and old_mark_lat - 0.00015 <= lat <= old_mark_lat + 0.00015 and new_mark_lat < lat and new_mark_lng - 0.00015 <= lng <= new_mark_lng + 0.00015 and old_lng < new_lng and new_lat - 0.00005 <= old_lat <= new_lat + 0.00005):
                    # GO_E_Right
                    print(str(cnt)+" working ER")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lng < lng and old_mark_lat - 0.00015 <= lat <= old_mark_lat + 0.00015 and new_mark_lat > lat and new_mark_lng - 0.00015 <= lng <= new_mark_lng + 0.00015 and old_lng < new_lng and new_lat - 0.00005 <= old_lat <= new_lat + 0.00005):
                    # GO_E_Left
                    print(str(cnt)+" working EL")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lng > lng and old_mark_lat - 0.00015 <= lat <= old_mark_lat + 0.00015 and new_mark_lat > lat and new_mark_lng - 0.00015 <= lng <= new_mark_lng + 0.00015 and old_lng > new_lng and new_lat - 0.00005 <= old_lat <= new_lat + 0.00005):
                    # GO_W_Right
                    print(str(cnt)+" working WR")
                    break
                elif (mark_lng-0.00003 <= lng <= mark_lng+0.00003 and mark_lat-0.00003 <= lat <= mark_lat+0.00003 and old_mark_lng > lng and old_mark_lat - 0.00015 <= lat <= old_mark_lat + 0.00015 and new_mark_lat < lat and new_mark_lng - 0.00015 <= lng <= new_mark_lng + 0.00015 and old_lng > new_lng and new_lat - 0.00005 <= old_lat <= new_lat + 0.00005):
                    # GO_W_Left
                    print(str(cnt)+" working WL")
                    break
                else:
                    print(str(cnt)+" working")
                    
                    pass
            elif mark == array[0]:
                gpsvalue = "Latitude=" + str(lat) + "  and Longitude=" + str(lng)
                print(gpsvalue)
                if (mark_lng-0.00015 <= lng <= mark_lng+0.00015 and mark_lat-0.00015 <= lat <= mark_lat+0.00015):
                    past_lat = (float(array_mark[0]))
                    past_lng = (float(array_mark[1]))
                    break
                else:
                    pass
            past_lat = lat
            past_lng = lng
        mark_c.close()
        cnt += 1
        print(cnt)
    return ()


while True:
    home = input("home :")
    if (home == "1"):
        array = array9
        active(array)
