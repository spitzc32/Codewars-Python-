def likes(nam):
    n= len(nam)  
    return  ('no one likes this' if n==0 else f"{nam[0]} likes this" if n==1 else f"{nam[0]} and {nam[1]} like this" if n==2 else f"{nam[0]}, {nam[1]} and {nam[2]} like this" if n==3 else f"{nam[0]}, {nam[1]} and {len(nam)-2} others like this")
