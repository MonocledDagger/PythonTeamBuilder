import pickle
import os

filename='player_data.pkl'
players={}

def load_pickle(filename): #Load Pickle
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    else:#make Pickle if not found
        print(f"'{filename}' not found. Creating a new pickle file.")
        make_pickle()
        return {}

def save_pickle(data, filename): #Save pickle
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
        
def make_pickle():
    # Make and save dictionary
    with open(filename, 'wb') as fp:
        pickle.dump(players, fp)
        print('New Dictionary Made')
    