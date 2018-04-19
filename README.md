# auxiliary-tools-for-python
some auxiliary tools for python, like grammar transformation etc.


#First tool performs an auto Transform.

#It Transforms python of version 2.x as below
    import re
    print 'this is a test'
    a = 1 + 2
    for i in range(a):
        print i
    print 'this test'
#To
    import re
    print ('this is a test')
    a = 1 + 2
    for i in range(a):
      print (i)
    print('this test')
