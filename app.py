import re, sys

file_1 = sys.argv[1]
file_2 = sys.argv[2]
table = sys.argv[3]
insert_index = sys.argv[4]
replacement_value = sys.argv[5]

def main():

    file = open(file_1, "r")
    newfile = open(file_2, "w")

    for aline in file:
        insert_statement = re.compile(r"^(INSERT INTO\s(.*)\sVALUES\s\()(.*)(\).*)$").split(aline)
        
        if len(insert_statement) != 6:
            newfile.write(aline)
            continue

        table_found = insert_statement[2]
        statement_start = insert_statement[1]
        statement_values = insert_statement[3]
        statement_end = insert_statement[4]
        old_statement = statement_start + statement_values + statement_end

        if table_found != table:
            newfile.write(aline)
            continue

        statement_values = replace_value(statement_values, insert_index, replacement_value)
        new_statement = statement_start + statement_values + statement_end

        print ("\n\n-------------------------------------------------\nReplacing:\n")
        print (old_statement)
        print ("\nWith:\n")
        print (new_statement)
        newfile.write(new_statement+"\n")
    
    file.close()
    newfile.close()

def replace_value(values_list, index, new_value):
    raw_values = values_list.split(',')
    raw_values[int(index)] = " "+new_value
    return ",".join(raw_values)

main()