from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    if request.method == 'POST':
        master = request.POST.get('master')
        one = request.POST.get('one')
        two = request.POST.get('two')
        three = request.POST.get('three')
        four = request.POST.get('four')

        masterString = master
        res = []
        
        strings = [one, two, three, four]
        for string in strings:
            masterCopy = master
            for alph in string:
                flag = True
                if alph in masterCopy:
                    masterCopy = masterCopy.replace(alph,'',1)
                else:
                    flag = False
                    break
            if flag:
                res.append({'name': string, 'value': 'yes'})
                master = masterCopy
            else:
                res.append({'name': string, 'value': 'no'})
        context = {'results': res,'master':masterString}
    return render(request, 'app/index.html',context)