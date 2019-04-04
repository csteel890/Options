# Options
#Options project



Derivatives project utilising OOP in Python. 

The assumption is that a financial institution is writing options and would like a way to store their price and initial hedge data.

Options are priced using the Black Scholes equation with an initial hedge being calculated on the basis the only source of risk is fluctuations in the underlying stock. The Option is created within the parent class (acting as an abstract class) with specific methods polymorphically delegated to each respective child class representing either a call option or a put option.
          

An in-memory database has been created with SQLite3 to store the price and initial delta of any new option which is created.

The code can be extended by amending the calling_object to be a portfolio of options. Once an option has been sold, the portfolio would not care how the option is being hedged, only that it is being hedged correctly. Hence why the calling object is currently polymorphically executing the delta method.

