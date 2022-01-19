#!/Users/river/Developer/bin/miniforge3/bin/python
#
# LaunchBar Action Script
#
import sys
import json
import subprocess

input = sys.argv[1]



input = input.splitlines()
max_len = len(max(input))
output = [input[0]]

for i in range(len(input)-1):
  last_line = input[i]
  this_line = input[i+1]

  # choose first word in line
  first_word_this_line = this_line.strip().split(' ')[0]

  # if the first word of this line added to the last line tips it over the 
  # max line length, then this was likely due to a hard line wrap
  if (len(first_word_this_line)+len(last_line)+1) > max_len:
    # this was a hard line wrap, so should append this line to the last one
    output[-1] = output[-1]+' '+this_line.strip()
  else:
    # this was an intentional line break
    output.append(this_line)

output = '\n\n'.join(output)

# copy to clipboard
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

write_to_clipboard(output)




# dump into json output
items = [{'title': output}]
print(json.dumps(items))