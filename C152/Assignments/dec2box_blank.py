# file: dec2box_blank.py
# author: Rick Walker

# Gets input decimal string from user and converts to bin, oct, and hex
# (string) representation
again = True
early_out = False
while again:
    again = False
    val_in = raw_input('Enter a decimal value or press enter to exit: ')
    if len(val_in) == 0:
        print '... exiting ...'
        early_out = True
        break
    elif val_in[0] == '-' and len(val_in) > 1:
        sign = '-'
        work_in = val_in[1:]
    else:
        sign = ''
        work_in = val_in[:]
    for char in work_in:
        if char not in '0123456789':
            print val_in + 'is not a valid decimal value ...'
            again = True
            break
if not early_out:
    print '\n*** Output after input verification ***'
    print 'Input:  ' + val_in
    print 'Working with:  ' + work_in
    work_in = work_in[::-1]
    dec_val = 0
    for index in range(len(work_in)):
        char_val = ord(work_in[index]) - ord('0')
        dec_val += char_val * 10 ** index
    print '\n*** Output after conversion string to value ***'
    print 'Computed value:  ', dec_val
    digits = '0123456789abcdef'
    for base in [2, 8, 16]:
        work_val = dec_val
        num_list = list()
        while work_val <> 0:
            rem = work_val % base
            num_list.insert(0, digits[rem])
            work_val /= base
        if base == 2:
            bin_str = sign + '0b' + ''.join(num_list)
        elif base == 8:
            oct_str = sign + '0' + ''.join(num_list)
        else:
            hex_str = sign + '0x' + ''.join(num_list)
    print '\n*** Final output ***'
    print 'dec:  ' + val_in
    print 'bin:  ' + bin_str
    print 'oct:  ' + oct_str
    print 'hex:  ' + hex_str
