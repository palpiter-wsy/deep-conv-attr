import pickle

data_file=open('../Model/SP.pkl', 'rb')
my_data=pickle.load(data_file)
print(my_data)