def sum(data):
    general = 0.0
    required = 0.0
    elective = 0.0
    school_required = 0
    for a in data:
        if(float(a[3].replace("*","")) < 60 ):
            print("不及格的課程:" + a[0] )
            print("分數為" + a[3].strip().replace("*", ""))
            print("課程類型:" + a[1])
            a[3] = "0"

        if(a[1] == "通識"):
            general += float(a[2])
        elif(a[1] == "專業必修"):
            required += float(a[2])
        elif(a[1] == "專業選修"):
            elective += float(a[2])
        elif(a[1] == "校定必修"):
            school_required += float(a[2])
    total = general + required + elective + school_required
    min = 32 #最少選修學分數

    print("-------------------")
    print("通識:",int(general))
    print("專業必修:",int(required))
    print("專業選修:",int(elective))
    print("校定必修:",int(school_required))
    print("總學分:",int(total))
    if(min - int(elective) < 0 ):
        print("距離專業選修學分(32)差0學分")
    else:
        print("距離專業選修學分(32)差", str(min - int(elective)) + "學分")
    print("距離規定學分(128)差", str(128 - int(total)) + "學分")
    print("-------------------")
    print("叫我帥哥阿欽")

