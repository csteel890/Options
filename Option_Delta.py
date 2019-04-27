import numpy as np 
from scipy import stats
import pandas as pd

class Option:
	'''Create Option and implement method for d1 for calculating option price and delta'''

	S_t = [80, 90, 95, 99, 100, 101, 105, 110, 120] #Possible price jumps of next recorded stock price
	all_options = []

	def __init__(self, S_0, K, r, sigma, T, analytics = None):
		if not analytics:
			self.analytics = {'Option_Price': [], 'dV': []}
		self.S_0 = S_0
		self.K = K
		self.r = r
		self.sigma = sigma
		self.T = T
		Option.all_options.append(self)


	def d1(self, S):
		'''Helper function to calculate delta and price of option'''
		d1 = (np.log(S/self.K) + (self.r + (np.square(self.sigma)/2))*self.T) / (self.sigma * np.sqrt(self.T))
		return d1	


class Call(Option):

	def price(self, S):	
		d1 = self.d1(S)
		d2 = d1 - (self.sigma*np.sqrt(self.T))
		price = S * stats.norm.cdf(d1) - (self.K * np.exp(-self.r * self.T)) * stats.norm.cdf(d2)
		return price

	def delta(self, S):
		d1 = self.d1(S)
		delta = stats.norm.cdf(d1)
		return delta


	def __str__(self):
		'''Equation used to determine change in value of portfolio consisting of option and underlying stock'''
		return 'dV = [c(t + dt) - c(t)] - deltaC[S(t + dt) - S(t)]'	


	def __call__(self):
		'''Loop through possible stock prices to examine change of portfolio value for each price'''
		for S in Option.S_t:
			Option_Price = self.price(S)
			dV = (Option_Price - self.price(self.S_0)) - self.delta(self.S_0)*(S - self.S_0)

			self.analytics['Option_Price'].append(Option_Price)
			self.analytics['dV'].append(dV)

		df = pd.DataFrame(self.analytics, index = Option.S_t).rename_axis('Stock_Price')
		return df



o1 = Call(100, 110, 0.05, 0.142470, 1)

def main():
	for option in Option.all_options:
		print('List of possible stock price movements and \ncorresponding changes in portfolio value dV \nfor one time increment: \n \n{} \n \n {}'.format(option, option()))

if __name__ == '__main__':
	main()




