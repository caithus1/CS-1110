import urllib.request


def avg_temp_day(date1, date2):
    for b in dates:
        if date1 == b[0:3]:
            first = b[5]
        if date2 == b[0:3]:
            second = b[5]
    return (int(first)+int(second))/2


def avg_temp_month(year, month):
    temps = []
    for b in dates:
        if year == b[0] and month == b[1]:
            temps.append(b[3])
    return max(temps)

lines = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/cho-temp.csv').read().decode('utf-8').split('\n')
print(lines)
dates = []
for i in lines:
    dates.append(i.split(','))

prompt = input('Is your date [year, month, day] (1) or (year, month) (2)? ')
if prompt == '1':
    data = input('Please enter first dateFORMAT: ').split()
    data2 = input('Please enter second dateFORMAT: ').split()
    # data and data2 must be lists
    print(avg_temp_day(data, data2))
if prompt == '2':
    year_in = input('Enter year: ')
    month_in = input('Enter month: ')
    print(avg_temp_month(year_in, month_in))

'''
Key Prints:
    after file read
        list of lists ['2004,Dec,28,38,15,27',...]
    after prompt
        make sure type matches with check
    after data
        both lists [year, month, day]
        both strings 'year' , 'month'
    in avg_temp_day
        iterating through list of lists
            on iteration: returns whole list
                on match: returns 1 or 2 days
        types of comparisons
        conversion to int when taking average
    in avg_temp_month:
        inputs as strings
        iterating through list of lists
            on iteration: returns whole list
                on match: returns ~30 days
        temps list
        max function


Checks:

Input: Split data, keep as string or convert to int
Check if conversion to str/int to go to prompt
Correct function1: Input as two lists
Account for repeated values: 1, 10, 11, 12 for 1
Conversion to ints/strings
Not decoding/splitting

Format:

Read file
    file = urllib.request.urlopen(url).read().decode('utf-8').split('\n')
    for i in file:
        dates.append(i.split(','))
Prompt user for prompt
    prompt = input('1 or 2?')
Prompt for information
    data = input('').split()
Run and print function
    print(func(data1, data2)

Questions:
    What do you think that should print?
    What functions could you use to do that?
    Where do you think your program is making the mistake and why?
    For me, a helpful thing to do is printing
'''