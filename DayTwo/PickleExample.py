import pickle

def searlize_me():
    data = dict(name=['manju','naresh'],
                projects=dict(emc='mahadevpura',
                              Hp='mah'),
                Exp='5')
    pickle.dump(data, open('content.pickle', 'wb'))


def unserilize_me():
    text = pickle.load(open('content.pickle', 'rb'))
    print(text)
searlize_me()
unserilize_me()