# initial imports
from datetime import datetime, timezone
import time

# telegram imports
from telethon.sync import TelegramClient

# define a list to store scraped data
scraped_data = []

# setup / change only the first time you use it
username = 'Ishpreet01' # your Telegram username
api_id = '29849471' # your Telegram API ID
api_hash = '35b4d2106178726a132fba85a5f2f5d1' # your Telegram API hash
channel = '@goyalarsh' # the name of the Telegram channel or group you want to scrape
d_min = 1 # start day / this date will be included
m_min = 1 # start month
y_min = 2023 # start year
d_max = 2 # final day / only the day before this date will be included, that is, this date will not be included
m_max = 2 # final month
y_max = 2023 # final year
key_search = 'sde' # optional: a keyword to search for in messages

# scraping
with TelegramClient(username, api_id, api_hash) as client:
 # print("Start time: ",time.time())
  for message in client.iter_messages(channel, search=key_search):
    #print("Start time 2: ",time.time())
    if message.date < datetime(y_max, m_max, d_max, tzinfo=timezone.utc) and message.date > datetime(y_min, m_min, d_min, tzinfo=timezone.utc):

      # prepare message data
      message_data = {
          # 'id': f'#ID{len(scraped_data)+1:05}',
          'group': channel,
          # 'author_id': message.sender_id,
          'text': message.text,
          'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
          # 'message_id': message.id,
          'author': message.post_author,
          'views': message.views,
          'reactions': '',
          # 'shares': message.forwards,
          'media': f'https://t.me/{channel}/{message.id}'.replace('@', '') if message.media else 'no media',
          'comments': [],
      }

      # gather reactions
      if message.reactions:
        message_data['reactions'] = ', '.join([f"{reaction_count.reaction.emoticon} {reaction_count.count}" for reaction_count in message.reactions.results])

      # gather comments
      try:
        for comment in client.iter_messages(channel, reply_to=message.id):
          message_data['comments'].append(comment.text)
      except:
        message_data['comments'] = ['possible adjustment']

      # append message data to scraped data list
      scraped_data.append(message_data)


      # updates the progress counter
      # print(f'Item {len(scraped_data):05} completed!')
      # print(f'Id: {message.id:05}.\n')

      # sleep for a second to avoid rate limiting
      time.sleep(1)
 # print("End time: ",time.time())

# end
print(f'----------------------------------------\n#Concluded! #{len(scraped_data):05} posts were scraped!\n----------------------------------------\n\n\n\n')

