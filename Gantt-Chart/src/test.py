from gantt import GanttChart
 
g = GanttChart()
print('first plot')
g.plot([('kia', 0, 10), ('arash', 10, 20), ('kia', 30, 10),
    ('nia', 40, 10), ('max', 50, 20), ('nia', 70, 10)])
g.save('output.jpg')

print('second plot')
g.plot([('kia', 0, 30), ('arash', 30, 10),
    ('nia', 40, 10), ('max', 50, 20), ('nia', 70, 10)])

g.show()
