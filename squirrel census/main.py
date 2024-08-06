import pandas

data = pandas.read_csv("pandas library/squirrel census/NY squirrel data.csv")     ## Entire Dataframe

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]     ##pulls out all data of gray squirrels
 
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])



squirrel_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],                          ### Creates a new dictionary
    "Count": [gray_count, cinnamon_count, black_count]
}

s_count = pandas.DataFrame(squirrel_dict)          ### Creates new dataframe
s_count.to_csv("Squirrel count.csv")               ### Saves new dataframe