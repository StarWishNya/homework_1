import os

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
    names =  {}
    #如果file 为文件夹，则遍历文件夹下所有文件
    if os.path.isdir(file):
        for root, dirs, files in os.walk(file):
            for file in files:
                if file.endswith('.txt'):
                    names.update(static_name_from_data(os.path.join(root, file)))
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = split_sentence(text)
    names = {}
    number = len(sentences)
    count = 0
    for sentence in sentences:
        words = split_word(sentence)
        sentence_name = name_identify(words)
        for name in sentence_name:
            names[name] = names.get(name, 0) + sentence_name[name]
        count += 1
        print(f'\r{count}/{number}', end='')
    #删除出现次数小于10的人名
    names = {name: names[name] for name in names if names[name] > 10}
    return names

if __name__ == '__main__':
    file = 'download/2930.txt'
    names = static_name_from_data(file)
    print(names)