from stack_viewer import Stack


s = Stack()
end = s.var('end',False)

x = s.var('x',0)
while x < 10:
    x.set(x+ 1)
    s.sleep(1)

end.set(True)