import check_response

b = input('Input website address:')
c = input()
if check_response.check_re(c):
    print('Website is still alive!')
else:
    print('We are so sorry...')
