#Print most active users and number of actions. 
# Output:
# Most active User: user1, user2 and Action: 3 

logs = [
    "user1 2026-05-27 10:00:00 LOGIN",
    "user2 2026-05-27 10:05:00 UPLOAD",
    "user1 2026-05-27 10:10:00 DOWNLOAD",
    "user3 2026-05-27 10:15:00 LOGIN",
    "user1 2026-05-27 10:20:00 LOGOUT",
    "user2 2026-05-27 10:25:00 DOWNLOAD",
    "user2 2026-05-27 10:00:00 LOGIN"
]

counts = {}

for log in logs:
    user = log.split()[0]
    if user not in counts:
        counts[user] = 1
    else:
        counts[user] += 1

max_actions = max(counts.values())

most_active_users = []

for user, count in counts.items():
    if count == max_actions:
        most_active_users.append(user)

print(f"Most active User: {', '.join(most_active_users)} and Action: {max_actions}")

## without usig max():
# counts = {}

# for log in logs:
#     user = log.split()[0]

#     if user not in counts:
#         counts[user] = 1
#     else:
#         counts[user] += 1

# max_actions = -1

# for count in counts.values():
#     if count > max_actions:
#         max_actions = count

# most_active_users = []

# for user, count in counts.items():
#     if count == max_actions:
#         most_active_users.append(user)

# print(f"Most active User: {', '.join(most_active_users)} and Action: {max_actions}")

#using dict.get()
# logs = [
#     "user1 2026-05-27 10:00:00 LOGIN",
#     "user2 2026-05-27 10:05:00 UPLOAD",
#     "user1 2026-05-27 10:10:00 DOWNLOAD",
#     "user3 2026-05-27 10:15:00 LOGIN",
#     "user1 2026-05-27 10:20:00 LOGOUT",
#     "user2 2026-05-27 10:25:00 DOWNLOAD",
#     "user2 2026-05-27 10:00:00 LOGIN"
# ]

# counts = {}

# for log in logs:
#     user = log.split()[0]
#     counts[user] = counts.get(user, 0) + 1

# max_actions = max(counts.values())

# most_active_users = [
#     user for user, count in counts.items()
#     if count == max_actions
# ]

# print(f"Most active User: {', '.join(most_active_users)} and Action: {max_actions}")