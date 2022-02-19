import random

Nouns=["fossil", "horse", "aardvark", "judge", "chef", "mango","extrovert", "gorilla"]
Verbs=["kicks", "jingles", "bounces", "slurps", "meows","explodes", "curdles"]
Adjectives=["furry", "balding", "incredulous", "fragrant","exuberant", "glistening"]
Prepositions=["against", "after", "into", "beneath", "upon","for", "in", "like", "over", "within"]
Adverbs=["curiously", "extravagantly", "tantalizingly","furiously", "sensuously"]

def make_poem():
    noun=[random.choice(Nouns) for i in range(3)]
    verb=[random.choice(Verbs) for i in range(3)]
    adj=[random.choice(Adjectives) for i in range(3)]
    prep=[random.choice(Prepositions) for i in range(2)]
    adv=[random.choice(Adverbs)]

    if adj[0][0] in 'aeiou':
        article='An'
    else:
        article='A'


    poem=(
        f'{article} {adj[0]} {noun[0]}\n\n'
        f'{article} {adj[0]} {noun[0]} {verb[0]} {prep[0]} the {adj[1]} {noun[1]}\n'
        f'{adv[0]}, the {noun[0]} {verb[1]}\n'
        f'the {noun[1]} {verb[2]} {prep[1]} a {adj[2]} {noun[2]}'
          )

    return poem

print(make_poem())
