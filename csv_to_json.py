 with open('/home/mohammed/Desktop/formats/input/data.csv', 'rb') as csvfile:       
 	csv_r = csv.reader(csvfile)
    for row in csv_r:
        result.append(row)


new_result =map(lambda x : {x[0]: x[1]}, result)
def group_all_dicts(ls_of_dicts):
	final_dict = {}
	for i in ls_of_dicts :
		final_dict.update(i)
	return final_dict

final_json_dict =  group_all_dicts(new_result)
with open('data.txt', 'w') as outfile:
    json.dump(final_json_dict, outfile, indent = 2)
