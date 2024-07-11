
def Longest_prefix(strings):
       l = list(zip(*strs))
       prefix = ""
       for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                 break
       return prefix
strs =["flower","flow","flight"]        