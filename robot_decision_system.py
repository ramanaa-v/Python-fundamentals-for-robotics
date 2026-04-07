# Robot movement decision system
obstacle_type = 'wall'

if obstacle_type == 'wall':
    print('Turn around')
elif obstacle_type == 'small object':
    print('Go over')
elif obstacle_type == 'gap':
    print('Stop and find another path')
else:
    print('Clear path, continue moving')

# Power-aware robot decision system
battery_level = 20

if obstacle_type == 'wall' and battery_level > 20:
    print('Turn around')
elif obstacle_type == 'small object' and battery_level > 10:
    print('Go over')
elif obstacle_type == 'gap':
    print('Stop and find another path')
else:
    print('Low power: Return to base')
    
