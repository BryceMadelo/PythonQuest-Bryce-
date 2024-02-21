try:
    with open("story.txt", "r") as story_file:

        line_count = sum(1 for _ in story_file)
        print(f"The total number of line in 'story.txt': {line_count}")
except FileExistsError:
    print("Error! 'story.txt' file cannot be found.")