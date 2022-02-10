print('\n'.join([' '.join('%sx%s=%-2s'%(x,y,x*y)
                          for x in range(1,y+1))
                          for y in range(1,10)]))
