import sys 

N = int(sys.stdin.readline())
#N = 2
for i in range(1, 10):
  #TextIOWrapper.write() takes exactly one argument (5 given)
  # stdin과 stdout의 차이.
  #write와 writelines의 차이점? 개행문자.
  txt =  ' '.join([str(N),'*',str(i),'=',str(N*i), '\n'])
  sys.stdout.writelines(txt)
  