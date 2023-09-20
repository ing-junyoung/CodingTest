# 3009


# 개수가 1개인 것을 찾기. 

x_points , y_points = [] , []

for _ in range(3):
    
    cnt_x , cnt_y = map(int , input().split())
    
    x_points.append(cnt_x)
    y_points.append(cnt_y)
    
element_x = list(set(x_points))
element_y = list(set(y_points))

solution_xy = []

if x_points.count(element_x[0]) == 1:
    
    solution_xy.append(element_x[0])
    
else:
    
    solution_xy.append(element_x[1])
    
    
if y_points.count(element_y[0]) == 1:
    
    solution_xy.append(element_y[0])
    
else:
    
    solution_xy.append(element_y[1])      

    
    
print(*solution_xy)
