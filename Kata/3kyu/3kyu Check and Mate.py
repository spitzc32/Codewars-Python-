""" Returns an array of threats if the arrangement of 
 the pieces is a check, otherwise false

 created by: Neet/Spitcz32

"""
pieces = {"rook":(0,7), "knight":(4,4), "bishop":(7,7),"king":(1,1),"queen":(9,9),'pawn':(2,1)}
def isCheck(pieces, player):
    own = next((p for p in pieces if p['owner'] == player),None)
    
                 
def kingstep(own):
    x,y = own['x'],own['y']
    #horizontalL,horizontalR,verticalT,verticalD,diagonalLT,diagonalRT,diagonalLD,diagonalRD
    return  [(x-1,y) if x > 0,(x+1,y) if x < 7,(x,y-1) if y > 0,(x,y+1) if y < 7, 
     (x-1,y+1) if x > 0 and y < 7,(x+1, y+1) if x <7 and y < 7,(x-1,y-1) if x>0 and y>0,
     (x+1,y-1) if x<7 and y>0]

""" Returns true if the arrangement of the
 pieces is a check mate, otherwise false """
def isMate(pieces, player):
    own = next((p for p in pieces if p['owner'] == player and p['piece']=='king'),None)
    dangerZone, ks = [],[], kingstep(own)
    pieHV = next((p for p in pieces if p['owner'] != own['owner'] and (p['piece']== 'queen' or p['piece']== 'rook' or p['piece']== 'king')),None)
    pieD = next((p for p in pie if p['owner'] != own['owner'] and (p['piece']== 'queen' or p['piece']== 'bishop' or p['piece']== 'pawn')),None)
         
    #getting threat zones Horizontal and Vertical
    for p in pieHV:
        [dangerZone.append((p['x'],y)) for y in xrange(p['y'],8) if (p['x'],y) in ks] if y<own['y'] else [dangerZone.append((p['x'],y)) for y in range(7,p['y']-1,-1) if (p['x'],y) in ks] #vertical threat points
        [dangerZone.append((x,p['y'])) for x in xrange(p['x'],9) if (x,p['y']) in ks] if x<own['x'] else [dangerZone.append((x,p['y'])) for x in range(9,p['x'],-1) if (x,p['y']) in ks]#horizontal right threat points

    #getting threat zones Diagonal  
    for p in pieD:
         if p['piece'] == 'pawn':
             dangerZone.append((p['x']+1,y+1)) if (p['x']+1,y+1) in ks and (x<own['x'] and y<own['y']) #DTR
             dangerZone.append((p['x']+1,y-1)) if (p['x']+1,y-1) in ks and (x<own['x'] and y<own['y']) #DTL
             dangerZone.append((p['x']-1,y+1)) if (p['x']-1,y+1) in ks and (x<own['x'] and y<own['y']) #DDR
             dangerZone.append((p['x']-1,y-1)) if (p['x']-1,y-1) in ks and (x<own['x'] and y<own['y']) #DDL
         else:
             []
    return any([False if d in ks else True for d in dangerZone])
    
    
