import hanlp

hanlp.pretrained.pos.ALL
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
get_pos = hanlp.load(hanlp.pretrained.pos.CTB9_POS_ELECTRA_SMALL)

#按行分句
def split_sentence(text):
    sentences = []
    for line in text.split('\n'):
        sentences.append(line)
    return sentences

#按句分词
def split_word(sentence):
    words = HanLP(sentence, tasks='tok/fine')
    words = words["tok/fine"]
    return words


#取出人名
def name_identify(words):
    names = {}
    pos = get_pos(words)
    for i in range(len(words)):
        if pos[i] == 'NR':
            names[words[i]] = names.get(words[i], 0) + 1
    return names

def test_static_name_from_data():
    with open('data/1.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = split_sentence(text)
    names = {}
    for sentence in sentences:
        words = split_word(sentence)
        sentence_name = name_identify(words)
        for name in sentence_name:
            names[name] = names.get(name, 0) + sentence_name[name]
    print(names)

def static_name_from_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = split_sentence(text)
    names = {}
    for sentence in sentences:
        words = split_word(sentence)
        sentence_name = name_identify(words)
        for name in sentence_name:
            names[name] = names.get(name, 0) + sentence_name[name]
    #删除出现次数小于10的人名
    names = {name: names[name] for name in names if names[name] > 10}
    return names

if __name__ == '__main__':
    test_static_name_from_data()
    '''
    text = ("张三是个好人，李四是个坏人。\n"
            "王五是个好人，赵六是个坏人。")
    sentences = split_sentence(text)
    for sentence in sentences:
        words = split_word(sentence)
        names = name_identify(words)
        print(names)
    '''