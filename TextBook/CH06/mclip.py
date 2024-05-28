TEXT = {'yes':  'いいですよ',
        'no': 'ダメです',
        'wait': 'ちょっと待ってください',
        'late': '遅れます',
        'sorry': 'すみません'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python mclip.py [キーワード]')
    print('キーワードに対応するテキストをクリップボードにコピーします')
    sys.exit()

keyword = sys.argv[1]



if keyword in TEXT:
    pyperclip.copy(TEXT[keyword])
    print(keyword + 'のテキストをクリップボードにコピーしました')
else:
    print(keyword + 'に対応するテキストはありません')