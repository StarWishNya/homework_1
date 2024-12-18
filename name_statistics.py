import cut

def singlenamestatistics(name,file_path):
    names=name.split(" ")
    result={}
    full_name=fullname(name)
    result[full_name]=0
    count=int(0)
    for singlename in names:
        temp=cut.maincut(singlename,file_path)[singlename]
        count+=temp
        result[singlename]=temp
    result[full_name]=count
    return result

def fullname(name):
    names=name.split(" ")
    full_name=""
    for name in names:
        full_name+=name
    return full_name

def Namestatistics(namelist,file_path="data"):
    name_counts_total={}
    for name in namelist:
        name_counts_total[name]=singlenamestatistics(name,file_path)
    name_counts_total=sorted(name_counts_total.items(),key=lambda x:x[1][fullname(x[0])],reverse=True)
    return name_counts_total

def name_format(name_counts):
    return [(name, {name: count}) for name, count in name_counts.items()]