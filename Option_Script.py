import numpy as np 
from scipy import stats
from database import DataBase
import pandas as pd

class Option:
	
	'''Create Plain Vanilla Option and let sub-classes explicitly implement price method. Analytics attribute only used for when code
			is extended to calculate delta for each i-th time step when simulation has run'''

	all_options = []
	db = DataBase()

	def __init__(self, ref, S_0, K, r, sigma, T, analytics = {'Stock': [], 'Delta': []}):
		self.ref = ref #Primary key for database 
		self.S_0 = S_0
		self.K = K
		self.r = r
		self.sigma = sigma
		self.T = T
		self.analytics = analytics
		Option.all_options.append(self)


	def d1(self):
		'''d1 helper function for pricing and calculating delta'''
		d1 = (np.log(self.S_0/self.K) + (self.r + (np.square(self.sigma)/2))*self.T) / (self.sigma * np.sqrt(self.T))
		return d1


	def simulate_stock_path(self, M, I):
		'''Vectorised code for simulating stock path for when script is extended to calculate delta at numerous time intervals'''
		dt = (self.T)/M
		S = self.S_0 * np.exp(np.cumsum((self.r - 0.5*self.sigma**2) * dt + self.sigma * np.sqrt(dt) * np.random.standard_normal((M + 1, I)), axis = 0))
		#self.analytics['Stock'] = S


	def price(self):
		'''Explicitly execute via subclass'''
		raise NotImplementedError('Implement via sub-class only')

	


class Call_Option(Option):
	def price(self):
		d1 = self.d1()
		d2 = d1 - (self.sigma*np.sqrt(self.T))
		price = self.S_0 * stats.norm.cdf(d1) - (self.K * np.exp(-self.r * self.T)) * stats.norm.cdf(d2)
		delta = stats.norm.cdf(self.d1())
		Option.db.insert_data(self.ref, price, delta)
	
	
class Put_Option(Option):
	def price(self):
		d1 = self.d1()
		d2 = d1 - (self.sigma*np.sqrt(self.T))
		price = self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-d2) - self.S_0*stats.norm.cdf(-d1)
		delta = stats.norm.cdf(self.d1()) - 1
		Option.db.insert_data(self.ref, price, delta)



#option = sub_class(ref, S_0, K, r, sigma, T)
o1 = Call_Option(123, 42, 40, 0.1, 0.2, 0.5)
o2 = Put_Option(456, 42, 40, 0.1, 0.2, 0.5)
o3 = Call_Option(789, 49, 50, 0.05, 0.2, 0.3846)




def calling_object():
	'''Polymorphically execute the price method of each option and return a pandas dataframe with a list 
			of all options with a price and initial delta for hedging. Calling object could be a portfolio of options '''

	for option in Option.all_options:
		option.price()
	data = Option.db.get_data()
	df = pd.DataFrame(data, columns = ['Option_Ref', 'Price', 'Initial Delta']).set_index('Option_Ref')
	return df

print('{}'.format(calling_object()))


