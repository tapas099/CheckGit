def foo(required,*args,**kargs):  # required argument is mandatory
    print(f'required:{required}')
    if args:
        print(args) # will return tuple
    if kargs:
        print(kargs) # will return key:values or dictionary

foo(123)

foo([23,45,'yho'],'this','that')
foo("abc",345,34,'taios',amul=3,dan=7)