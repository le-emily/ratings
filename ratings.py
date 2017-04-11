
def get_restaurant_ratings(filename):
    """Restaurant rating lister."""

    my_file = open(filename)

    ratings = {}

    for line in my_file:
        line = line.rstrip()
        line = line.split(":")

        ratings[line[0]] = line[1]

        return ratings


rating_list = get_restaurant_ratings("scores.txt")


def add_restaurant(get_ratings):
    """Asks user for restaurant and rating, then adds to list."""

    restaurant_name = raw_input("Restaurant Name: ")

    # print "\n"

    while True:
        try:
            restaurant_score = raw_input("Restaurant Score (1-5): ")
            restaurant_score = int(restaurant_score)
            if 1 <= restaurant_score <= 5 and restaurant_score.isdigit():

                break
                
        except:
            print "That's not a valid score!"


        # restaurant_score > 5 or int(restaurant_score) < 1 or not restaurant_score.digit():
        #     continue
        # else:    
        #     return False

    get_ratings[restaurant_name] = restaurant_score

    for key, value in sorted(get_ratings.items()):
        print key, "is rated at", value

add_restaurant(rating_list)
