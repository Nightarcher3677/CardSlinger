import json

class save:
    #the read function, returns the card stored at the number selected
    def read(num):
        with open('save.json') as f:
            data = json.load(f)

        for test in data['save']:
            return test['card' + str(num)]

    #writes the save to a json file to be read in later dates
    def write(num, newcontent):
        with open('save.json', 'r+') as f:
            data = json.load(f)
            for test in data['save']:
                test['card'+str(num)] = newcontent # <--- add `id` value.
                f.seek(0)        # <--- should reset file position to the beginning.
                json.dump(data, f, indent=2)
                f.truncate()



print(save.read(11))
save.write(11, 'test')
print(save.read(11))
