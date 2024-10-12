import os


# This function will return a list of string with all the file types within a folder.
def find_types_set(_source_folder):
    file_types = []
    for root, dirs, files in os.walk(_source_folder):
        for file in files:
            if os.path.splitext(file)[1] not in file_types:
                file_types.append(os.path.splitext(file)[1])
    return file_types


# Prints out the data types within folder and returns the type that the user wants to collect.
def choose_type(_source_folder):
    for i in find_types_set(_source_folder):
        print(i)
    return input("Which file type do you want to collect? ").lower()


def find_all_and_copy(_source_folder, _destination_folder):
    # Check if the destination of the directory exists.
    if not os.path.exists(_destination_folder):
        os.makedirs(_destination_folder)

    desired_file_type = choose_type(_source_folder)

    for root, dirs, files in os.walk(_source_folder):
        for file in files:
            extension = os.path.splitext(file)[1]

            if extension == desired_file_type:

                source_path = os.path.join(root, file)
                destination_path = os.path.join(_destination_folder, file)

                with open(source_path, 'rb') as source:
                    with open(destination_path, 'wb') as destination:
                        destination.write(source.read())

                print(f" {file} was copied to {_destination_folder}")













def main():
    source_folder = input("What folder should we look at? ")
    destination_folder = input("Destination folder? Ex: C:/Users/HP/Documents/PersonalDocuments/ElPerro ")

    find_all_and_copy(source_folder, destination_folder)


main()


# This creates a Directory
# os.makedirs("C:/Users/HP/Documents/PersonalDocuments/ElPerro")

# This returns a tuple with [0] = name of file, [1] = extension
# os.path.splitext(file)






