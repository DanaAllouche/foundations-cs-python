def count_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num // 10)

def find_max(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        max_rest = find_max(nums[1:])
        return nums[0] if nums[0] > max_rest else max_rest

def count_tags(html, tag):
    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"
    count = 0
    start_index = html.find(open_tag)
    if start_index == -1:
        return 0
    else:
        count += 1
        end_index = html.find(close_tag, start_index + len(open_tag))
        inner_html = html[start_index + len(open_tag):end_index]
        return count + count_tags(inner_html, tag) + count_tags(html[end_index + len(close_tag):], tag)

def main():
    while True:
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")
        print("- - - - - - - - - - - - - - -")
        choice = int(input("Enter a choice: "))
        
        if choice == 1:
            num = int(input("Enter an integer: "))
            count = count_digits(num)
            print("Number of digits:", count)
        elif choice == 2:
            nums = input("Enter a list of integers (space-separated): ").split()
            nums = [int(x) for x in nums]
            max_num = find_max(nums)
            print("Maximum value:", max_num)
        elif choice == 3:
            html = '''
            <html>
            <head>
            <title>My Website</title>
            </head>
            <body>
            <h1>Welcome to my website!</h1>
            <p>Here you'll find information about me and my hobbies.</p>
            <h2>Hobbies</h2>
            <ul>
            <li>Playing guitar</li>
            <li>Reading books</li>
            <li>Traveling</li>
            <li>Writing cool h1 tags</li>
            </ul>
            </body>
            </html>
            '''
            tag = input("Enter a tag: ")
            count = count_tags(html, tag)
            print("Number of occurrences:", count)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
