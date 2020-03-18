with open('script', 'w') as f:
    steps = 36
    for step in range(steps):
        rot = 360 * (step / steps) + 7
        f.write('clear\n')
        f.write('ident\n')
        f.write('box\n')
        f.write('0 0 0 160 160 160\n')
        f.write('rotate\n')
        f.write('x 30\n')
        f.write('rotate\n')
        f.write(f'y {rot}\n')
        f.write('translate\n')
        f.write('250 300 0\n')
        f.write('apply\n')
        f.write('save\n')
        f.write(str(step).zfill(3) + '.png\n')