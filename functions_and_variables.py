################ Global variables ################
# paths for the three files
train_file = "./data/train.txt"
test_file = "./data/test.txt"
val_file = "./data/val.txt"





################ Useful functions ################

# process text files so that a list is returned with [<sentence>,<emotion>]
def read_file(file_path):
    data = []
    with open(file_path,'r') as file:
        for line in file:
            data.append(line.strip().split(";"))
    return data