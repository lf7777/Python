def trim(par):
    i = 0
    l = len(par)
    while i<l:
        if par[i] != ' ':
            par_01=par[i:]
            if par_01[len(par_01)-1] != ' ':
                return par
            else:
                k = len(par_01)-1
                while k>0: 
                    if par_01[k] != ' ':
                        par_02 = par_01[:k+1]
                        return par_02
                    k = k-1
        i =i+1
res = trim('     hello world       ')
print(res,len(res),sep='\n')
