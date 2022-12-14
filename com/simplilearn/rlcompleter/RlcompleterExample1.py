import rlcompleter

my_completer=rlcompleter.Completer()

pharse_list=['co','cal','asser','contin','exce','finall']

for pharse in pharse_list:
    print(pharse + ' (TAB) ', end='')
    try:
        for i in range(50):
            terms=my_completer.complete(pharse,i)
            if terms is None:
                break
            print(terms,end='\t')
        print()
    except:
        pass