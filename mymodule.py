import random 

def choose_a_tiktokcontent(content_lists):
    random_item = random.choice(content_lists)
    print("use this contnets for tiktok today:", random_item)
    
def choose_instagramcontent(content_lists):
    random_forinstagram = random.sample(content_lists, 3)
    print("use this contnets for tiktok today:", random_forinstagram)    
  
          
content_lists = ["relatable memes","emotional and relationship" , "edits and aura contents", "anytype at anytime", "mix of all", "something new and unique"]
something_unique = ["relatable memes","emotional and relationship" , "edits and aura contents", "nyash contents", "anytype at anytime", "mix of all",  "nyash content towards a good point"]


choose_a_tiktokcontent(content_lists)
choose_instagramcontent(content_lists)
    
