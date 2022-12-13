#Time : O(N)
#Space : O(1)
#String
def URLify(string,length):
    string = list(string)
    index = length-1
    pos = len(string)-1

    while index>=0 and pos>= 0:
        if string[index] == " ":
            string[pos] = "0"
            pos-=1
            string[pos] = "2"
            pos-=1
            string[pos] = "%"
        else:
            string[pos] = string[index]
        index-=1
        pos-=1
    return "".join(map(str,string))
print(URLify("Hello World  ",11))
print(URLify("Mr John Smith    ",13))
