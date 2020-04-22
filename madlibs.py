import re

text = """
キリンは大昔から __複数名刺__ の興味の対象でした。キリンは __複数名刺__
の中で一番背が高いのですが、科学者たちはそのような長い __体の一部__ を
どうやって獲得したのか説明できません。キリンの身長は __数値__ __単位__
近くあり、その高さのほとんどは脚と __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分
    は後の2つをアンダースコアで挟んでください。ヒントの単語にはアンダースコア
    を含めないでください。__hint_hint__ はだめです。__hint__ はOKです。
    """
    hints = re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q = "'{}'を入力:".format(word)
            new = raw_input(q)
            mls = mls.replace(word, new, l)
        print('\n')
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)
