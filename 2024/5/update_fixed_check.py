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
    rules.sort() # sort the rules so we can make sure we order the pages correctly

    #split out the updates and make them into a 2d array
    updates = values[1]
    updates = updates.split("\n")
    updates = [update.split(",") for update in updates]

    sum_of_middle_pages_of_invalid_updates = 0
    invalid_updates = 0
    valid_updates = 0
    print("number of updates: ", len(updates))
    for update in updates:
        is_valid = True
        for page in update:
            for rule in rules:
                if page in rule:
                    if page in rule[0]:
                        try:
                            constraint_page_index = update.index(rule[1])
                            if (constraint_page_index < update.index(page)):
                                is_valid = False
                                pass
                        except ValueError:
                            pass
        if is_valid: 
            valid_updates += 1
            pass
        else:    
            # make the invalid update ordered correctly
            invalid_updates += 1
            # create a dictionary for each page in the update
            pages_with_scores = {page: 0 for page in update}
            for page in update:
                for rule in rules:
                    if page in rule:
                        if page in rule[0]:
                            try:
                                constraint_page_index = update.index(rule[1])
                                pages_with_scores[page] += 1
                            except ValueError:
                                pass
            # create a new array from the pages_with_scores dictionary using 
            # the key as the value and the score as the index
            corrected_update = [page for page in sorted(pages_with_scores, key=pages_with_scores.get)]
            corrected_update.reverse()
            print(corrected_update)
            # add middle value to the sum
            sum_of_middle_pages_of_invalid_updates += int(corrected_update[(len(corrected_update) - 1) // 2])
    # print("Sum of middle pages of invalid updates: ", sum_of_middle_pages_of_invalid_updates)
    print("number of valid updates: ", invalid_updates)
    print("number of invalid updates: ", valid_updates)
    print("sum_of_middle_pages_of_invalid_updates=",sum_of_middle_pages_of_invalid_updates)
if __name__ == "__main__":
    main()