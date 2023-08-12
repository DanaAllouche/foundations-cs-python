class SocialMediaPlatform:

  def __init__(self):
    self.graph = {}

# Add a user to the platform.

  def add(self, username):
    if username in self.graph:
      print("User already exists. Please choose another username.")
    else:
      self.graph[username] = []
# Remove a user from the platform.

  def removeUser(self, username):
    if username in self.graph:
      del self.graph[username]
      for friend in self.graph.values():
        if username in friend:
          friend.remove(username)
    else:
      print("Didn't find user.")
# Send a friend request to another user.

  def sendRequest(self, fromUser, toUser):
    if fromUser not in self.graph or toUser not in self.graph:
      print("Didn't find user.")
    else:
      self.graph[fromUser].append(toUser)
      self.graph[toUser].append(fromUser)
# Remove a friend from your list.

  def removeFriend(self, user1, user2):
    if user1 in self.graph and user2 in self.graph:
      if user2 in self.graph[user1]:
        self.graph[user1].remove(user2)
        self.graph[user2].remove(user1)
      else:
        print(f"{user1} & {user2} are not friends.")
    else:
      print("Didn't find user.")
# View your list of friends.

  def viewFriends(self, username):
    if username in self.graph:
      friends = self.graph[username]
      print(f"Friends of {username}: {', '.join(friends)}")
    else:
      print("Didn't find user.")
# View the list of users on the platform.

  def viewUsers(self):
    print("List of all registered users:")
    for user in self.graph:
      print(user)

# Display User menu

  def menu(self):
    print("\nMenu:")
    print("1. Add a user to the platform")
    print("2. Remove a user from the platform")
    print("3. Send a friend request to another user")
    print("4. Remove a friend from your list")
    print("5. View your list of friends")
    print("6. View the list of users on the platform")
    print("7. Exit")

  def run(self):
    while True:
      self.menu()
      choice = input("Enter your choice: ")
      if choice == "1":
        username = input("Enter username: ")
        self.add(username)
      elif choice == "2":
        username = input("Enter username to remove: ")
        self.removeUser(username)
      elif choice == "3":
        from_user = input("Enter your username: ")
        to_user = input("Enter friend's username to add: ")
        self.sendRequest(from_user, to_user)
      elif choice == "4":
        user1 = input("Enter username: ")
        user2 = input("Enter friend's username to remove: ")
        self.removeFriend(user1, user2)
      elif choice == "5":
        username = input("Enter username: ")
        self.viewFriends(username)
      elif choice == "6":
        self.viewUsers()
      elif choice == "7":
        print("Exit")
        break
      else:
        print("Invalid choice.")

if __name__ == "__main__":
  platform = SocialMediaPlatform()
  platform.run()
