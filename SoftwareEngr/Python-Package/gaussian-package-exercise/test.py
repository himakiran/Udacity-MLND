from distributions import Gaussian
g1 = Gaussian(25,2)
g1.read_data_file('numbers.txt')
g1.plot_histogram()
