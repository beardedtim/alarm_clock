import argparse

parser = argparse.ArgumentParser(prog='Alarm Clock', description='Set up an Alarm Clock.')

parser.add_argument('--hour',  type=int, help='The hour that we want to set the alarm for. 24-hour format.')

parser.add_argument('--minute', type=int,  help='The minute that we want to set the alarm for.')

def get_args():
  return vars(parser.parse_args())