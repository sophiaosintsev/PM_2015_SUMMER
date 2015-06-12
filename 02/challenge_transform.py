# define the input data
data_list = [
    {"id": 123, "name": "abc", "phone": "555.555.5555"},
    {"id": 456, "name": "def", "phone": "444.444.4444"}
]

# define the function that we will call later
def transform(data_list_input):
    data_dictionary_output = {}

    # DO YOUR WORK HERE
    # LOOP THROUGH ALL ITEMS IN data_list
    for item in data_list_input:
        # EXTRACT id from each extracted item
        id = item["id"]
        # CREATE an output item that is a new Dictionary/Object
        output_item = {}

        for key in item.keys():
            if key != "id":
                output_item[key] = item[key]
        # COPY all properties except id from the original item into the new one
        # ADD the new item to data_dictionary using the id as the key.
        data_dictionary_output[id] = output_item
    # INCORRECT NAIVE ATTEMPT WITHOUT LOOPS OR VARIABLES
    # data_dictionary_output[data_list_input[0]["id"]] = {"name": data_list_input[0]["name"]}
    # data_dictionary_output[data_list_input[1]["id"]] = {"name": data_list_input[1]["name"]}

    return data_dictionary_output

# call the transform function passing in the data
data_dictionary_result = transform(data_list)

print(data_dictionary_result)