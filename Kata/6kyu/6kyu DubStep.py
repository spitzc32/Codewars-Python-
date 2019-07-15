"""
    Created by: Neet/ Spitcz32
    
"""

def song_decoder(song):
    return ' '.join([c for c in song.split("WUB") if c.isalpha()])
 
