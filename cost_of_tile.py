def cal_area(l,b):
    return l*b

def total_cost(area,cost_tile):
    return area*cost_tile

while True:
    print "Enter the value of Length and breath of the Floor you want to cover: "
    l=input()
    b=input()
    print "Enter the cost to cover 1 tile:"
    cost_tile=input()

    if type(l)!=str and type(b)!=str and type(cost_tile)!=str:
        area=cal_area(l,b)
        print total_cost(area,cost_tile)
        break
    
