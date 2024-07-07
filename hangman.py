import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["", "baboon", "camel",  "apple", "banana", "orange", "mango", "grape", "lemon", "cherry", "peach", "strawberry", "watermelon", "pineapple", "blueberry", "raspberry", "blackberry", "kiwi", "avocado", "pear", "apricot", "plum", "fig", "date", "grapefruit", "lime", "coconut", "papaya", "melon", "nectarine", "pomegranate", "cranberry", "lychee","passionfruit", "tangerine", "persimmon", "guava", "dragonfruit", "jackfruit", "durian", "kumquat", "starfruit", "clementine", "chestnut", "walnut", "pecan", "almond", "cashew", "pistachio", "hazelnut", "macadamia", "peanut", "sunflower", "corn", "potato", "tomato", "onion", "garlic", "carrot", "cucumber", "lettuce", "spinach", "broccoli", "cauliflower", "cabbage", "kale", "radish", "celery", "bellpepper", "eggplant", "zucchini", "asparagus", "pumpkin", "squash", "sweetpotato", "turnip", "parsnip", "beet", "rhubarb", "artichoke", "okra", "leek", "mushroom", "beans", "lentil", "chickpea", "pea", "soybean", "kidneybean", "blackbean", "pinto", "navybean", "limabean", "greenbean", "fava", "mungbean", "snowpea", "snappea", "pod", "pastries", "beverage", "dairy", "dough", "cake", "cookie", "bread", "cheese", "cream", "butter", "milk", "yogurt", "icecream", "pudding", "custard", "candy", "chocolate", "sugar", "honey", "syrup", "jam", "jelly", "nutella", "spread", "sauce", "mayonnaise", "mustard", "ketchup", "relish", "vinegar", "oil", "soysauce", "salad", "dressing", "gravy", "soup", "stew", "curry", "chili", "porridge", "stirfry", "roast", "grill", "barbecue", "bake", "steam", "boil", "poach", "fry", "saute", "pan", "cook", "mix", "baste", "season", "taste", "spice", "marinate", "garlicbread", "bruschetta", "crouton", "breadstick", "baguette", "croissant", "biscuit", "scone", "muffin", "pancake", "waffle", "crepe", "frenchtoast", "toast", "roll", "bun", "bagel", "sandwich", "wrap", "taco", "burrito", "quesadilla", "enchilada", "tamale", "empanada", "pizza", "calzone", "pasta", "spaghetti", "macaroni", "lasagna", "ravioli", "gnocchi", "penne", "fettuccine", "linguine", "couscous", "rice", "quinoa", "bulgur", "barley", "oatmeal", "granola", "cereal", "porridge", "muesli", "bread", "baguette", "roll", "loaf", "focaccia", "flatbread", "tortilla", "pita", "naan", "chapati", "roti", "tart", "pie", "crisp", "crumble", "cobbler", "turnover", "strudel", "pastry", "danish", "eclair", "profiterole", "creamhorn", "millefeuille", "macaroon", "meringue", "trifle", "pudding", "parfait", "mousse", "sorbet", "sherbet", "gelato", "frozenyogurt", "sundae", "affogato", "smoothie", "shake", "juice", "lemonade", "icedtea", "cocktail", "margarita", "martini", "mojito", "daiquiri", "whiskey", "vodka", "rum", "tequila", "gin", "brandy", "champagne", "wine", "beer", "cider", "punch", "sangria", "soda", "cola", "rootbeer", "sprite", "pepsi", "gingerale", "tonic", "water", "coffee",
            "espresso", "latte", "cappuccino", "macchiato", "americano", "mocha", "frappuccino", "chai", "tea", "matcha",
            "bubbletea", "boba", "herbaltea", "tiger", "lion", "elephant", "giraffe", "zebra", "hippo", "rhino", "buffalo",
            "antelope", "koala", "kangaroo", "koala", "panda", "sloth", "monkey", "gorilla", "chimpanzee", "lemur", "wolf",
            "fox", "bear", "polarbear", "penguin", "seal", "walrus", "dolphin", "whale", "shark", "octopus", "squid",
            "jellyfish", "starfish", "turtle", "frog", "toad", "snake", "lizard", "crocodile", "alligator", "iguana", "gecko",
            "chameleon", "tortoise", "hedgehog", "rabbit", "hare", "hamster", "guineapig", "gerbil", "mouse", "rat", "squirrel",
            "chipmunk", "bat", "bird", "eagle", "hawk", "falcon", "owl", "parrot", "pigeon", "duck", "goose", "swan",
            "peacock", "rooster", "chicken", "turkey", "seagull", "pelican", "flamingo", "crane", "stork", "heron", "puffin",
            "albatross", "crow", "raven", "magpie", "sparrow", "finch", "canary", "bluejay", "cardinal", "robin", "wren",
            "titmouse", "thrush", "nightingale", "bulbul", "starling", "woodpecker", "kingfisher", "hummingbird", "swift", "swallow",
            "martin", "cuckoo", "penguin", "roadrunner", "quail", "falcon", "ostrich", "emu", "cassowary", "kiwi", "penguin",
            "turaco", "trogon", "toucan", "woodcock", "sandpiper", "plover", "killdeer", "snipe", "curlew", "avocet", "lapwing",
            "jacana", "godwit", "turnstone", "phalarope", "dove", "lyrebird", "kookaburra", "serpent", "pangolin", "anteater",
            "armadillo", "anteater", "chinchilla", "agouti", "guinea", "opossum", "wombat", "possum", "mongoose", "meerkat",
            "ferret", "polecat", "weasel", "badger", "raccoon", "redpanda", "skunk", "honeybadger", "hyena", "fossa", "mongoose",
            "bobcat", "lynx", "jaguar", "leopard", "cheetah", "cougar", "panther", "tiger", "lion", "leopard", "snowleopard",
            "tiger", "bear", "panda", "polarbear", "koala", "kangaroo", "wombat", "bandicoot", "echidna", "platypus", "lemur",
            "monkey", "lemur", "tarsier", "sifaka", "galago", "bushbaby", "loris", "potto", "aardvark", "armadillo", "antelope",
            "eland", "gazelle", "oryx", "kudu", "impala", "gnu", "wildebeest", "springbok", "bison", "buffalo", "yak",
            "ox", "muskox", "sheep", "goat", "ram", "ewe", "lamb", "calf", "cow", "bull", "cattle", "bison",
            "llama", "alpaca", "vicuna", "guanaco", "camel", "dromedary", "llama", "alpaca", "guanaco", "vicuna", "camel",
            "dromedary", "camel", "dromedary", "bactrian", "elephant", "rhino", "hippo", "warthog", "zebra", "giraffe", "tapir",
            "pig", "hog", "boar", "sow", "piglet", "hedgehog", "shrew", "mole", "marmot", "woodchuck", "groundhog", "squirrel",
            "chipmunk", "prairie", "dog", "marmot", "groundhog", "woodchuck", "squirrel", "chipmunk", "prairie", "dog", "marmot",
            "groundhog", "woodchuck", "squirrel", "chipmunk", "prairie", "dog", "meerkat", "mongoose", "otter", "seal", "walrus",
            "dolphin", "whale", "porpoise", "manatee", "seacow", "sealion", "fur", "seal", "sea", "lion", "manatee", "seacow",
            "sea", "lion", "manatee", "seacow", "sea", "lion", "sealion", "walrus", "beaver", "muskrat", "capibara", "sloth",
            "anteater", "armadillo", "aardvark", "platypus", "echidna", "wombat", "koala", "kangaroo", "bandicoot", "wallaby", "opossum",
            "possum", "squirrel", "chipmunk", "rat", "mouse", "vole", "lemming", "gerbil", "hamster", "guineapig", "chinchilla",
            "rabbit", "bunny", "hare", "pika", "rodent", "squirrel", "chipmunk", "rat", "mouse", "vole", "lemming", "gerbil",
            "hamster", "guineapig", "chinchilla", "rabbit", "bunny", "hare", "pika", "rodent", "chameleon", "iguana", "gecko",
            "lizard", "snake", "cobra", "viper", "python", "boa", "anaconda", "rattlesnake", "garter", "king", "milk",
            "corn", "snake", "python", "viper", "cobra", "rattlesnake", "garter", "king", "milk", "corn", "snake", "python",
            "viper", "cobra", "rattlesnake", "garter", "king", "milk", "corn", "snake", "python", "viper", "cobra", "rattlesnake",
            "garter", "king", "milk", "corn", "snake", "python", "viper", "cobra", "rattlesnake", "garter", "king", "milk",
            "corn", "sea", "turtle", "turtle", "tortoise", "terrapin", "hawk", "eagle", "falcon", "vulture", "owl", "kestrel",
            "harrier", "kite", "buzzard", "osprey", "eagle", "falcon", "vulture", "owl", "kestrel", "harrier", "kite", "buzzard",
            "osprey", "owl", "hawk", "eagle", "falcon", "vulture", "kestrel", "harrier", "kite", "buzzard", "osprey", "owl",
            "hawk", "eagle", "falcon", "vulture", "kestrel", "harrier", "kite", "buzzard", "osprey", "pelican", "heron", "stork",
            "crane", "egret", "ibis", "flamingo", "spoonbill", "duck", "goose", "swan", "merganser", "teal", "wigeon", "shoveler",
            "pintail", "mallard", "duck", "goose", "swan", "merganser", "teal", "wigeon", "shoveler", "pintail", "mallard", "teal",
            "wigeon", "shoveler", "pintail", "mallard", "teal", "wigeon", "shoveler", "pintail", "mallard", "duck", "goose", "swan",
            "merganser", "teal", "wigeon", "shoveler", "pintail", "mallard", "duck", "goose", "swan", "merganser", "teal", "wigeon",
            "shoveler", "pintail", "mallard", "pigeon", "dove", "quail", "grouse", "ptarmigan", "partridge", "pheasant", "turkey", "peacock",
            "cuckoo", "kingfisher", "woodpecker", "roller", "bee", "hornet", "wasp", "ant", "fly", "mosquito", "moth", "butterfly",
            "dragonfly", "ladybug", "beetle", "grasshopper", "cricket", "cicada", "termite", "bug", "insect", "spider", "tarantula", "scorpion",
            "mantis", "tick", "mite", "scorpion", "mantis", "tick", "mite", "spider", "tarantula", "scorpion", "mantis", "tick", "mite",
            "spider", "tarantula", "scorpion", "mantis", "tick", "mite", "spider", "tarantula", "scorpion", "mantis", "tick", "mite",
            "scorpion", "mantis", "tick", "mite", "spider", "tarantula", "scorpion", "mantis", "tick", "mite", "butterfly", "moth", "beetle",
            "fly", "ant", "wasp", "hornet", "bee", "bumblebee", "buzz", "bat", "vampire", "fruitbat", "flyingfox", "bat", "vampire",
            "fruitbat", "flyingfox", "butterfly", "moth", "beetle", "fly", "ant", "wasp", "hornet", "bee", "bumblebee", "buzz",
            "fly", "butterfly", "moth", "beetle", "ant", "wasp", "hornet", "bee", "bumblebee", "buzz", "bumblebee", "honeybee", "sweatbee",
            "carpenterbee", "masonbee", "bumblebee", "honeybee", "sweatbee"]

word_game = random.choice(word_list)

lives = 6

display = []

for _ in range(len(word_game)):
    display += "_"

end_of_game = False

while not end_of_game:
    print(stages[lives])
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    guessed_correctly = False
    for position in range(len(word_game)):
        letter = word_game[position]
        if letter == guess:
            display[position] = letter
            guessed_correctly = True

    if not guessed_correctly:
        lives -= 1

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("You lose")

print(f"The word was {word_game}")
