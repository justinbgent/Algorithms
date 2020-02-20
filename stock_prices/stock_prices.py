#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # first value [0] represents price
  # second value [1] represents index the price was found at
  max_price = [-1, 0]
  min_price = [-1, 0]
  cur_max_sale = None
  previous_price = None
  for i in range(0, len(prices)):
    if (max_price[0] == -1):
      max_price[0] = prices[i]
    elif (max_price[0] < prices[i]):
      max_price[0] = prices[i]
      max_price[1] = i

    if (min_price[0] == -1):
      min_price[0] = prices[i]
    elif (min_price[0] > prices[i]):
      min_price[0] = prices[i]
      min_price[1] = i

    if(i == 1):
      cur_max_sale = prices[1] - prices[0]

    if(cur_max_sale is not None):
      if(min_price[0] != -1 and (max_price[0] - min_price[0]) > cur_max_sale and min_price[1] < max_price[1]):
        cur_max_sale = max_price[0] - min_price[0]

      if (cur_max_sale < (prices[i] - previous_price)):
        cur_max_sale = prices[i] - previous_price
    previous_price = prices[i]
  return cur_max_sale


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))