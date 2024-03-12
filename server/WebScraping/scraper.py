# # initial imports
# from datetime import datetime, timezone
# import time

# # telegram imports
# from telethon.sync import TelegramClient

# # define a list to store scraped data
# scraped_data = []

# # setup / change only the first time you use it
# username = 'Ishpreet01' # your Telegram username
# api_id = '29849471' # your Telegram API ID
# api_hash = '35b4d2106178726a132fba85a5f2f5d1' # your Telegram API hash
# channel = '@goyalarsh' # the name of the Telegram channel or group you want to scrape
# d_min = 1 # start day / this date will be included
# m_min = 1 # start month
# y_min = 2023 # start year
# d_max = 2 # final day / only the day before this date will be included, that is, this date will not be included
# m_max = 2 # final month
# y_max = 2023 # final year
# key_search = 'sde' # optional: a keyword to search for in messages

# # scraping
# with TelegramClient(username, api_id, api_hash) as client:
#  # print("Start time: ",time.time())
#   for message in client.iter_messages(channel, search=key_search):
#     #print("Start time 2: ",time.time())
#     if message.date < datetime(y_max, m_max, d_max, tzinfo=timezone.utc) and message.date > datetime(y_min, m_min, d_min, tzinfo=timezone.utc):

#       # prepare message data
#       message_data = {
#           # 'id': f'#ID{len(scraped_data)+1:05}',
#           'group': channel,
#           # 'author_id': message.sender_id,
#           'text': message.text,
#           'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
#           # 'message_id': message.id,
#           'author': message.post_author,
#           'views': message.views,
#           'reactions': '',
#           # 'shares': message.forwards,
#           'media': f'https://t.me/{channel}/{message.id}'.replace('@', '') if message.media else 'no media',
#           'comments': [],
#       }

#       # gather reactions
#       if message.reactions:
#         message_data['reactions'] = ', '.join([f"{reaction_count.reaction.emoticon} {reaction_count.count}" for reaction_count in message.reactions.results])

#       # gather comments
#       try:
#         for comment in client.iter_messages(channel, reply_to=message.id):
#           message_data['comments'].append(comment.text)
#       except:
#         message_data['comments'] = ['possible adjustment']

#       # append message data to scraped data list
#       scraped_data.append(message_data)


#       # updates the progress counter
#       # print(f'Item {len(scraped_data):05} completed!')
#       # print(f'Id: {message.id:05}.\n')

#       # sleep for a second to avoid rate limiting
#       time.sleep(1)
#  # print("End time: ",time.time())

# # end
# print(f'----------------------------------------\n#Concluded! #{len(scraped_data):05} posts were scraped!\n----------------------------------------\n\n\n\n')



# from telethon.sync import TelegramClient
# from datetime import datetime, timezone
# import time

# # Your Telegram API credentials
# username = 'Ishpreet01'
# api_id = '29849471'
# api_hash = '35b4d2106178726a132fba85a5f2f5d1'

# # Your other scraping parameters
# channel = '@goyalarsh'
# d_min = 1
# m_min = 1
# y_min = 2023
# d_max = 1
# m_max = 1
# y_max = 2024
# key_search = 'sde'

# # Set the phone number programmatically (replace it with your actual phone number)
# phone_number = '+919927077188'

# with TelegramClient(username, api_id, api_hash) as client:
#     client.connect()

#     # Ensure you're authorized. If not, send the code and log in.
#     if not client.is_user_authorized():
#         client.send_code_request(phone_number)
#         client.sign_in(phone_number, input('Enter the code: '))

#     # Your scraping logic...
#     # Append data to scraped_data list
#     scraped_data = []

#     for message in client.iter_messages(channel, search=key_search):
#         if message.date < datetime(y_max, m_max, d_max, tzinfo=timezone.utc) and \
#            message.date > datetime(y_min, m_min, d_min, tzinfo=timezone.utc):
#             # Prepare message data and append to scraped_data list
#             message_data = {
#                 'group': channel,
#                 'text': message.text,
#                 'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
#                 'author': message.post_author,
#                 'views': message.views,
#                 'reactions': '',
#                 'comments': [],
#             }

#             # Gather reactions
#             if message.reactions:
#                 message_data['reactions'] = ', '.join([f"{reaction_count.reaction.emoticon} {reaction_count.count}" for
#                                                        reaction_count in message.reactions.results])

#             # Gather comments
#             try:
#                 for comment in client.iter_messages(channel, reply_to=message.id):
#                     message_data['comments'].append(comment.text)
#             except:
#                 message_data['comments'] = ['possible adjustment']

#             # Append message data to scraped data list
#             scraped_data.append(message_data)

#     # Sleep for a second to avoid rate limiting
#     time.sleep(1)

# # Process the scraped data further or return it as needed
# print(scraped_data)



# from telethon.sync import TelegramClient
# from datetime import datetime, timezone
# import time
# import sys
# import os

# # Your Telegram API credentials
# username = 'Ishpreet01'
# api_id = '29849471'
# api_hash = '35b4d2106178726a132fba85a5f2f5d1'

# # Your other scraping parameters
# channel = '@goyalarsh'
# d_min = 1
# m_min = 1
# y_min = 2023
# d_max = 1
# m_max = 1
# y_max = 2024
# key_search = 'sde'

# # Set the phone number programmatically (replace it with your actual phone number)
# phone_number = os.environ.get('TELEGRAM_PHONE')

# #phone_number = input('Please enter your phone number: ')

# # Disable standard input (stdin) to avoid the EOFError
# # sys.stdin = open('nul', 'r')

# with TelegramClient(username, api_id, api_hash) as client:
#   client.connect()

#     # Ensure you're authorized. If not, send the hardcoded verification code.
#   if not client.is_user_authorized():
#     client.send_code_request(phone_number)
#     # Replace the next line with your verification code
#     verification_code = '32789'  # Replace with your actual verification code
#     client.sign_in(phone_number, verification_code)


#     # Your scraping logic...
#     # Append data to scraped_data list
#     scraped_data = []

#     for message in client.iter_messages(channel, search=key_search):
#         if message.date < datetime(y_max, m_max, d_max, tzinfo=timezone.utc) and \
#            message.date > datetime(y_min, m_min, d_min, tzinfo=timezone.utc):
#             # Prepare message data and append to scraped_data list
#             message_data = {
#                 'group': channel,
#                 'text': message.text,
#                 'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
#                 'author': message.post_author,
#                 'views': message.views,
#                 'reactions': '',
#                 'comments': [],
#             }

#             # Gather reactions
#             if message.reactions:
#                 message_data['reactions'] = ', '.join([f"{reaction_count.reaction.emoticon} {reaction_count.count}" for reaction_count in message.reactions.results])

#             # Gather comments
#             try:
#                 for comment in client.iter_messages(channel, reply_to=message.id):
#                     message_data['comments'].append(comment.text)
#             except:
#                 message_data['comments'] = ['possible adjustment']

#             # Append message data to scraped data list
#             scraped_data.append(message_data)

#     # Sleep for a second to avoid rate limiting
#     time.sleep(1)

# # Process the scraped data further or return it as needed
# print(scraped_data)



from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def predict():
      # Load the iris dataset
      iris = datasets.load_iris()
      X = iris.data  # Features
      y = iris.target  # Target variable

      # Split the data into training and testing sets
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

      # Create a K-Nearest Neighbors classifier
      knn = KNeighborsClassifier(n_neighbors=3)

      # Train the classifier
      knn.fit(X_train, y_train)

      # Make predictions on the test set
      y_pred = knn.predict(X_test)

      # Print the accuracy of the model
      accuracy = knn.score(X_test, y_test)

      print(accuracy)

      return accuracy



