def split(values, first, last):
    '''[4]'''
    pivot=values[first]
    savefirst=first

    onCorrectSide=True
    first = first + 1
    while(first<=last):
        onCorrectSide=(first<=last)
        while(onCorrectSide):
            if(values[first]>pivot):
                onCorrectSide=False
            else:
                first=first+1
                onCorrectSide=(first<=last)
        onCorrectSide=(first<=last)
        while(onCorrectSide):
            if(values[last]<=pivot):onCorrectSide=False
            else:
                last=last-1
                onCorrectSide = (first <= last)
        if(first<last):
            values[first],values[last]=values[last],values[first]
            first=first+1
            last=last-1
        if(first<=last):continue
        else:break
    splitpoint=last
    values[savefirst],values[splitpoint]=values[splitpoint],values[savefirst]
    return splitpoint


def quick_sort(values, first, last):
    '''[5]'''

    if(first<last):
        splitpoint = split(values, first, last)
        quick_sort(values,first,splitpoint-1)
        quick_sort(values,splitpoint+1,last)

    return values