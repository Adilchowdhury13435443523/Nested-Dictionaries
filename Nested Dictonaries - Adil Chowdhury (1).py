#2_D Arrays & Nested Dictionaries - Adil Chowdhury
#Dec.4, 2023
#Making Nested Dictionaries for our TGB and adding descriptions and
#Inventory

characters = {'Miles':{'Full name':'Miles Gonzalo Morales', #Dictionary 1
                       'Inventory space':'6 Slots',
                       'Health points':'100 Health Points'},
              'Johnny':{'Full name':'Johnny Aronld Smith',
                        'Inventory space':'8 Slots',
                        'Health points':'150 Health Points'},
              'Bill':{'Full name':'Bill Musk',
                      'Inventory space':'8 Slots',
                      'Health points':'150 Health Points'}
              }
              
rooms = {'Conservatory':{'Description':'The Conservatory is well kept and clean'}, # Dictonary 2 
        'Library':{'Description':'The Library is Messy, almost like someone was fighting'},
         'Study':{'Description':'Study is maintained but seems like someone was here'},
         'Ball Room':{'Description':'There is blood across the walls of the room'},
         'Kitchen':{'Description':'Smells really good in here'},
         
         }
         
weapons = {'Miles':{'Description':'Revolver: Can shoot anyone anywhere', #Dictonary 3
                    'Damage':'100 Damage'},
           'Johnny':{'Description':'Wrench: Shiny and never used',
                     'Damage':'50 Damage'},
           'Bill':{'Description':'Dagger: Sharp... Almost too sharp',
                   'Damage':'80 Damage'},
           }

for characters, characters_info in characters.items(): 
    print(f"\nCharacters: {characters}")			   #print all characters 
    full_name = characters_info['Full name']		   #variable for the Full name
    inventory_s = characters_info['Inventory space']   #variable for inventory
    health_points = characters_info['Health points']   #variable for health
    
    print(f"\tFull Name: {full_name.title()}")		   #For each character print
    print(f"\nCharacters: {characters}")			   #the full name, inventory 
    full_name = characters_info['Full name']		   #and health 
    print(f"\tInventory: {inventory_s.title()}")
    print(f"\tHealth points: {health_points.title()}")
    
for rooms, rooms_info in rooms.items():                
    print(f"\nRooms: {rooms}")                         #print all rooms
    description = rooms_info['Description']     	   #variable for descriptions
    
    print(f"\tDescription: {description.title()}")     #print all descriptions in title case
    
for weapons, weapons_info in weapons.items():
    print(f"\n{weapons}'s Inventory:")				   #print's character's inventory
    characters_inventory = weapons_info['Description'] #variable for descriptions
    damage = weapons_info['Damage']  				   #variable for Damages
    
    print(f"\t{characters_inventory.title()}")		   #prints both descriptions and damage
    print(f"\t{damage.title()}")
    






