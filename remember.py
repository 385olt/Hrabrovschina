import pickle

LAST_RESULT_FILE = 'last_result.pickled'
REMEMBERED_FILE = 'remembered.pickled'

last_result = pickle.load(open(LAST_RESULT_FILE, 'rb'))
remembered = pickle.load(open(REMEMBERED_FILE, 'rb'))

remembered.append(last_result)

pickle.dump(remembered, open(REMEMBERED_FILE, 'wb'))

print(' # Remembered: "' + ' '.join(last_result[:3]) + '..."')
