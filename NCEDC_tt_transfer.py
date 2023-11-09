# --- 0. Assign file names of your input and output file here ---
input_file = 'input.txt'
output_file = 'output.txt'

# --- 1. Load input file ---
f = open(input_file, 'r')
line_lst = []
for line in f:
    line_lst.append(line)

# --- 2. Transfer fmt ---
output_lst = []
for line in line_lst:
    try:
        first_letter = int(line[0])
        output_lst.append(line)
    except:
        sta, tt = line[:5], line[87:100]
        print("Station and Travel time: ", sta, tt)
        text = sta + "   " + tt
        output_lst.append(text)

# --- 3. Save output file
f = open(output_file, 'w')
for line in output_lst:
    print(line)
    f.write(line+"\n")
f.close()

print(f"Data transfer finish!! [Input file]: {input_file}, [Output file]: {output_file}")
