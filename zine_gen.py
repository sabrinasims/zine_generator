import random

adjective = ['successful', 'shaggy', 'highfalutin', 'deserted', 'hanging', 
'romantic', 'amusing','jaded', 'observant', 'secret', 'thick', 'succinct', 
'heavy', 'childlike', 'draconian', 'immense', 'synonymous', 'nervous', 
'sneaky', 'imperfect', 'deadpan', 'plausible', 'hellish', 'makeshift',
'unnatural', 'permissible', 'understood', 'inquisitive', 'public', 
'equable', 'wandering', 'neighborly', 'empty', 'stimulating',
'scandalous', 'damaging', 'noiseless', 'juicy', 'languid', 'scattered', 
'grotesque', 'old-fashioned', 'wacky', 'tender', 'strong', 'eager', 
'royal', 'gorgeous', 'pathetic', 'womanly', 'natural', 'defiant',
'gruesome', 'placid', 'alleged', 'petite', 'invincible',
'quixotic', 'foamy', 'boiling', 'humdrum', 'erratic', 'quack', 'aberrant',
'wide-eyed', 'careful', 'shivering', 'drunk', 'sick', 'rainy', 'helpless',
'waggish', 'ludicrous', 'afraid', 'aloof', 'repulsive', 'bite-sized', 
'shut', 'silly', 'supreme', 'gullible', 'grubby', 'noisy', 'wealthy', 
'cumbersome', 'long-term', 'acoustic', 'illegal', 'overt',
'fluffy', 'mushy', 'ultra', 'rapid', 'roasted', 'hilarious', 'clammy', 
'inspiring', 'radical', 'innovative']

noun = ['hammer', 'town', 'digestion', 'base', 'friends', 'trucks',
'snakes', 'thing', 'sack', 'sand', 'thunder', 'vein', 'discussion',
'crow', 'thought', 'coat', 'stream', 'trains', 'burst', 'low', 'zoo',
'nest', 'prose', 'boundary', 'detail', 'badge', 'thrill', 'room', 'steam',
'reaction', 'actor', 'house', 'volcano', 'talk', 'button', 'development',
'tomatoes', 'basket', 'wash', 'cat', 'bird', 'dime', 'baby', 'level', 'twist',
'part', 'middle', 'eggs', 'idea', 'walk', 'color', 'pen', 'frog', 'beds',
'ice', 'current', 'card', 'fire', 'stop', 'station', 'box', 'test',
'cakes', 'soda', 'distribution', 'sweater' 'force', 'anger', 'emotions',
'mother', 'sheep' 'star', 'stomach', 'tank', 'pull', 'year', 'bait', 'attraction',
'airplane', 'cent', 'needle', 'book', 'flowers', 'home', 'plough', 'pancake',
'road', 'hydrant', 'mind', 'bridge', 'border', 'toothpaste', 'wall',
'competition', 'line', 'existence', 'philosophy', 'building' 'need', 'bells',
'pleasure', 'office', 'cherry', 'poison', 'smile', 'number', 'whistle',
'friend', 'rainstorm', 'control', 'thread',
'class', 'cream', 'question', 'expansion', 'jellyfish','table']

def choiceGenerator():
	print("A " + random.choice(adjective) + " " + random.choice(noun) + " "
 + random.choice(noun) + " zine")


for choice in range(3):
	choiceGenerator() 
