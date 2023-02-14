#
# ["ps 1 3", "ps 2 4", "ps 1 5", "ps 3 4"]
#
# return duration about in one number what was maz

ll = ["ps 1 3", "ps 2 5", "ps 1 5", "ps 3 4","ps 1 6"]


def longest_log_duration(list_logs):
    logs = list_logs
    res = []
    for x in logs:
        name = str(x).split(" ")[0]
        dura = int(str(x).split(" ")[2],base=10) - int(str(x).split(" ")[1],base=10)
        res.append(""+name+" "+str(dura))
    
    return max(sorted(res,reverse=True))

print(longest_log_duration(ll))

def lld(list_logs):
    res = max(sorted([int(x.split(" ")[2])-int(x.split(" ")[1]) for x in list_logs]))
    return res

print("-----")
print(lld(ll))

def llfast(list_logs):
    return max(sorted(list_logs,key=lambda x: str(x.split(" ")[0])+" "+str(int(x.split(" ")[2]) - int(x.split(" ")[1]))))

print('-----')
print(llfast(ll))
