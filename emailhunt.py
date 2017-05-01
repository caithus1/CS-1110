import urllib.request
import re


def find_email(word):
    # word = word.strip('<br>')
    word = re.sub('<br>', '', word)
    word = word.rstrip('.?,')
    word = re.sub('NOSPAM', '', word)
    if 'mailto:' in word:
        word = re.search('mailto:(.*)">', word).group(1)
    return word

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')
valid_domains = ['.edu','.com','.ca','.us','.rentals']
all_words = []
for line in stream:
    decoded = line.decode('UTF-8').strip()
    words = decoded.split(' ')
    for word in words:
        all_words.append(word)
# p = re.compile('[a]')
# print(p.match("abcd").group())

final_list = []

for i in range(0,len(all_words)):
    word = all_words[i]
    if '@' in word:
        final = find_email(word)
        #print(final)
        if '.' in final[final.index('@'):]:
            if final[final.rfind('.'):].lower() in valid_domains:
                final_list.append(final)
    elif word == 'at':
        first = all_words[i-1]
        last = all_words[i+1]
        dot_check = ''
        if all_words[i+2] == 'dot':
            dot_check = '.' + all_words[i+3]
        #print(first)
        string = first + '@' + last + dot_check
        final = find_email(string)
        #print(final)
        if not final == 'at':
            if '.' in final[final.index('@'):]:
                final_list.append(final)


s = []
for i in final_list:
    if i not in s:
        s.append(i)

for i in s:
    print(i)
    #print(decoded)