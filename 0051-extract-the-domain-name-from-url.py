# TITLE: EXTRACT THE DOMAIN NAME FROM A URL
# TASK : Write a function that when given a URL as a string, parses out 
#        just the domain name and returns it as a string.
# Source: https://www.codewars.com/kata/514a024011ea4fb54200004b
# 3 March 2024

# 1st method
def domain_name(url):
    domain_name = ''
    path = ''
    new_url = ''
    
    # Remove the protocol
    if 'https://' in url:
        new_url = url.replace('https://', '')
    elif 'http://' in url:
        new_url = url.replace('http://', '')
    else: 
        new_url = url
    
    # Check the path of url
    curr_char = ''
    prev_char = ''
    for index, char in enumerate(new_url):
        curr_char = char
        if index >= 1:
            prev_char = new_url[index - 1]
            if prev_char == '/' and curr_char != '/':
                path = new_url[index:]
                break
    
    new_url = new_url.replace(path, '')
    new_url = new_url.replace('/', '')
    
    # Check the domain name
    start_index = new_url.find('.')
    end_index = new_url.find('.', start_index + 1)
    if end_index != -1:
        domain_name = new_url[start_index + 1:end_index]
        if len(domain_name) == 2:
            domain_name = new_url[:start_index]
    else:
        domain_name = new_url[:start_index]
    
    return domain_name


# Testing
print(domain_name('https://www.codewars.com/kata'))
print(domain_name('https://www.instagram.com/direct/inbox/'))
print(domain_name('icann.org'))
print(domain_name('http://google.com'))
print(domain_name('http://google.co.jp'))
print(domain_name('http://www.9m94w41p888b55s931nqizopadg6f.co.za/index.php'))