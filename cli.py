from alarm_clock.commands import get_args
from alarm_clock.read_file import read_into_array
from alarm_clock.random_item import get_random_item

time = get_args()

def get_message(time):
  base = 'You asked for an alarm to be set at %s'
  return base % time['hour'] + ':%s' % time['minute']

print(get_message(time))

data = read_into_array('./list.txt')

print('\nI will be using this youtube video as your alarm: \n')
print(get_random_item(data))