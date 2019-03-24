
def character :

    name = None

    all_stats = { 'STR', 'DEX', 'CON', 'INT', 'CHA'}

    base_stats    = dict.fromkeys(all_stats, 0)
    saving_throws = dict.fromkeys(all_stats, 0)

    all_skills = { 'Acrobatics', 'Animal Handling', 'Arcana',
                   'Athletics',  'Deception',       'History',
                   'Insight',    'Intimidation',    'Investigation',
                   'Medicine',   'Nature',          'Perception',
                   'Persuasion', 'Religion',        'Sleight of Hand',
                   'Stealth',    'Survival'}

    skill = {value : 0, expertise : False}

    skills = dict.fromkeys(all_skills, skill.copy())

    passive_wisdom = 0
    armor_class    = 0
    initiative     = 0
    speed          = 0

    hp = { 'max'  = 0, 
           'curr' = 0,
           'temp' = 0,
           'dice' = {'type': '0d0', 'remaining' : 0}