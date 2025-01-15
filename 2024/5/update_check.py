# update_check.py
def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    
    # split the values into an array
    values = values.split("\n\n")

    #split out the rules and make them into a 2d array
    rules = values[0]
    rules = rules.split("\n")
    rules = [rule.split("|") for rule in rules]

    #split out the updates and make them into a 2d array
    updates = values[1]
    updates = updates.split("\n")
    updates = [update.split(",") for update in updates]

    sum_of_middle_pages_of_valid_updates = 0
    for update in updates:
        is_valid = True
        for page in update:
            for rule in rules:
                if page in rule:
                    #print("Rule " + "|".join(rule) + " found for page: " + page)
                    if page in rule[0]:
                        try:
                            constraint_page_index = update.index(rule[1])
                            if (constraint_page_index < update.index(page)):
                                pass
                                # print("Problem with page " + page + 
                                #         " in update " + ",".join(update) +
                                #         "in rule" + "|".join(rule))
                                is_valid = False
                        except ValueError:
                            pass
                    # if page in rule[1]:
                    #     try:
                    #         constraint_page_index = update.index(rule[0])
                    #         if (constraint_page_index > update.index(page)):
                    #             print("Problem with page " + page + 
                    #                     " in update " + ",".join(update) +
                    #                     "in rule" + "|".join(rule))
                    #             counter1 += 1
                    #     except ValueError:
                    #         pass
        if is_valid: 
            sum_of_middle_pages_of_valid_updates += int(update[(len(update) - 1) // 2])
    print("Sum of middle pages of valid updates: ", sum_of_middle_pages_of_valid_updates)
if __name__ == "__main__":
    main()