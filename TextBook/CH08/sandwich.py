import pyinputplus as pyip

# 各アイテムの価格設定
prices = {
    'パン': {'小麦': 100, '白パン': 120, '全粒粉': 150, 'ライ麦': 130},
    'タンパク質': {'チキン': 200, 'ターキー': 250, 'ハム': 180, 'ベーコン': 180, '豆腐': 150},
    'チーズ': {'チェダー': 50, 'スイス': 60, 'モッツァレラ': 70, 'なし': 0},
    'トッピング': {'トマト': 30, 'レタス': 40, '卵': 60, 'ピクルス': 30, 'マヨネーズ': 20, 'マスタード': 20}
}

def yes_no(prompt):
    response = pyip.inputChoice(['はい', 'yes', 'いいえ', 'no'], prompt=prompt)
    return 'はい' if response in ['はい', 'yes'] else 'いいえ'

def sandwich_maker():
    bread = pyip.inputMenu(['小麦', '白パン', '全粒粉', 'ライ麦'], numbered=True, prompt='パンを選んでください:\n')
    protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', 'ベーコン', '豆腐'], numbered=True, prompt='タンパク質の種類を選んでください:\n')
    cheese = yes_no(prompt='チーズを追加しますか？\n')
    
    if cheese == 'はい':
        cheese = pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], numbered=True, prompt='チーズを選んでください:\n')
    else:
        cheese = 'なし'
    
    tomato = yes_no(prompt='トマトは要りますか？\n')
    lettuce = yes_no(prompt='レタスは要りますか？\n')
    egg = yes_no(prompt='ゆで卵は要りますか？\n')
    pickles = yes_no(prompt='ピクルスは要りますか？\n')
    mayo = yes_no(prompt='マヨネーズは要りますか？\n')
    mustard = yes_no(prompt='マスタードは要りますか？\n')

    count = pyip.inputInt(prompt='サンドイッチの数を入力してください:\n', min=1)

    # 合計金額の計算
    total_price = 0
    total_price += prices['パン'][bread]
    total_price += prices['タンパク質'][protein]
    total_price += prices['チーズ'][cheese]
    if tomato == 'はい':
        total_price += prices['トッピング']['トマト']
    if lettuce == 'はい':
        total_price += prices['トッピング']['レタス']
    if egg == 'はい':
        total_price += prices['トッピング']['卵']
    if pickles == 'はい':
        total_price += prices['トッピング']['ピクルス']
    if mayo == 'はい':
        total_price += prices['トッピング']['マヨネーズ']
    if mustard == 'はい':
        total_price += prices['トッピング']['マスタード']

    total_price *= count

    # 注文内容の表示
    print(f'注文内容は以下の通りです:\n'
          f'パン: {bread}\n'
          f'タンパク質: {protein}\n'
          f'チーズ: {cheese}\n'
          f'トマト: {tomato}\n'
          f'レタス: {lettuce}\n'
          f'ゆで卵: {egg}\n'
          f'ピクルス: {pickles}\n'
          f'マヨネーズ: {mayo}\n'
          f'マスタード: {mustard}\n'
          f'サンドイッチの数: {count}\n'
          f'合計金額: ¥{total_price}\n'
          f'ありがとうございました！')

if __name__ == '__main__':
    sandwich_maker()
