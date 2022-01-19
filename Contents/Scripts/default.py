#!/Users/river/Developer/bin/miniforge3/bin/python
#
# LaunchBar Action Script
#
import sys
import json

input = sys.argv[1]

input = input.splitlines()
max_len = len(max(input))
output = [input[0]]
for i in range(len(input)-1):
  last_line = input[i]
  this_line = input[i+1]
  # if the first word of this line added to the last line tips it over the 
  # max line length, then this was likely due to a hard line wrap
  first_word_this_line = this_line.split(' ')[0]
  if (len(first_word_this_line)+len(last_line)+1) > max_len:
    # this was a hard line wrap, so should append this line to the last one
    output[-1] = output[-1]+' '+this_line
  else:
    # this was an intentional line break
    output.append(this_line)
output = '\n\n'.join(output)


# dump into json output
items = [{'title': output}]
print(json.dumps(items))