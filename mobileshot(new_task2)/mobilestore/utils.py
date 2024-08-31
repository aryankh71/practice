BAD_WORDS = [
    'کیر', 'کر', 'کون', 'کس', 'کص', 'کث', 'کوس', 'کوص', 'کوث', 'جنده', 'حرامزاده', 'حرومزاده', 'kos', 'ker', 'kir',
    'haroomzade ', 'حرومزاده', 'حرامزاده', 'haramzade', 'koos', 'kus', 'koon', 'abkoon'
    'koooooooooooooooooooooooooooooooooooooooooooooooni','گایدم', 'گایدی', 'گایید'

]


def filter_bad_words(comment, bad_words):
    for word in bad_words:
        comment = comment.replace(word, '*' * len(word))
    return comment
