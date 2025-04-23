#!/usr/bin/env python3
import sys
import re

# 1) Read the shift key from the first arg
try:
    key = int(sys.argv[1]) % 26
except (IndexError, ValueError):
    sys.exit(1)

# 2) Read the entire message from stdin
message = sys.stdin.read()

# 3) Keep only letters and uppercase them
letters = re.sub(r'[^A-Za-z]', '', message).upper()

# 4) Apply the Caesar shift
shifted = []
for c in letters:
    # 'A' → 65
    shifted.append(chr((ord(c) - 65 + key) % 26 + 65))
cipher = ''.join(shifted)

# 5) Break into blocks of 5 letters, 10 blocks per line
blocks = [cipher[i:i+5] for i in range(0, len(cipher), 5)]
for i in range(0, len(blocks), 10):
    print(' '.join(blocks[i:i+10]))

