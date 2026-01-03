# Couldnt solve, picked solution from reddit
# https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt2hps9/

p = []
with open("input.txt", 'r') as file:
    for line in file:
        # print(line.strip())
        input = line.strip().split(',')
        p.append(list(map(int, input)))
print(p)

# Couldnt solve, picked solution from reddit
# https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt2hps9/
t = 0
for x1, y1 in p:
    for x2, y2 in p:
        if ( x1, y1 ) > ( x2, y2 ):
            continue
        bx1, bx2 = min( x1, x2 ), max( x1, x2 )
        by1, by2 = min( y1, y2 ), max( y1, y2 )
        for i, ( lx1, ly1 ) in enumerate( p ):
            lx2, ly2 = p[ ( i + 1 ) % len( p ) ]
            if not ( max( lx1, lx2 ) <= bx1 or bx2 <= min( lx1, lx2 ) or
                     max( ly1, ly2 ) <= by1 or by2 <= min( ly1, ly2 ) ):
                break
        else:
            t = max( t, ( bx2 - bx1 + 1 ) * ( by2 - by1 + 1 ) )
print( t )
# m = max(i for _,i in points)
# n = max(i for i,_ in points)
# # print(m,n)
# grid = [['.']*(n + 1) for i in range(m + 1)] 
# for a, b in points:
#     print(a, b)
#     grid[b][a] = "#"
# for row in grid:
#     print(row)

# def find_in_bounds(C) -> bool:
#     xshortlist = [p for p in points if p[0] == C[0]]
#     minx = min([p[1] for p in xshortlist])
#     maxx = max([p[1] for p in xshortlist])
#     if minx <= C[1] <= maxx:
#         return True

#     yshortlist = [p for p in points if p[1] == C[1]]
#     miny = min([p[0] for p in yshortlist])
#     maxy = max([p[0] for p in yshortlist])
#     if miny <= C[0] <= maxy:
#         return True
#     return False

# maxarea = 0
# n = len(points)
# for i in range(n):
#     for j in range(i + 1, n):
#         A = points[i]
#         B = points[j]
#         area = ((A[0] - B[0]) + 1) * ((A[1] - B[1]) + 1)
#         if area < maxarea:
#             continue
#         # check if its inbouds of green
#         # if yes then update maxarea, else ignore
#         # other points
#         C = [A[0], B[1]]
#         D = [B[0], A[1]]

#         # xshortlist = [p for p in points if p[0] == C[0]]
#         # minx = min([p[1] for p in xshortlist])
#         # maxx = max([p[1] for p in xshortlist])
#         # if minx <= C[1] <= maxx:
#         #     continue
#         # print(A, B, C, D, minx, maxx)

#         if find_in_bounds(C) and find_in_bounds(D):
#             print(area, A, B, C, D)
#             maxarea = max(maxarea, area)




# print(maxarea)

