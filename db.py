import sqlite3
import maps

def create_db():
    '''
    Creates new database with 3 tables in it
    will overwrite the existing one and all the 

    '''

    cur = conn.cursor()

    drop_users = '''
        DROP TABLE IF EXISTS 'Users';
    '''
    drop_foods = '''
        DROP TABLE IF EXISTS 'Foods';
    '''
    drop_logs = '''
        DROP TABLE IF EXISTS 'Logs';
    '''

    create_users_table = '''
        CREATE TABLE `Users` (
            `UserId`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            `Name`      INTEGER NOT NULL UNIQUE,
            `Gener`     TEXT NOT NULL,
            `Age`       INTEGER NOT NULL,
            `Password`  TEXT NOT NULL
        );
    '''
    create_foods_table = '''
        CREATE TABLE `Foods` (
            `ndbno`     TEXT NOT NULL UNIQUE,
            `Name`      TEXT NOT NULL,
            `Index`     REAL NOT NULL,
            '203'       REAL,
            '204'       REAL,
            '205'       REAL,
            '207'       REAL,
            '208'       REAL,
            '209'       REAL,
            '210'       REAL,
            '211'       REAL,
            '212'       REAL,
            '213'       REAL,
            '214'       REAL,
            '221'       REAL,
            '255'       REAL,
            '257'       REAL,
            '262'       REAL,
            '263'       REAL,
            '268'       REAL,
            '269'       REAL,
            '287'       REAL,
            '291'       REAL,
            '301'       REAL,
            '303'       REAL,
            '304'       REAL,
            '305'       REAL,
            '306'       REAL,
            '307'       REAL,
            '309'       REAL,
            '312'       REAL,
            '313'       REAL,
            '315'       REAL,
            '317'       REAL,
            '318'       REAL,
            '319'       REAL,
            '320'       REAL,
            '321'       REAL,
            '322'       REAL,
            '323'       REAL,
            '324'       REAL,
            '325'       REAL,
            '326'       REAL,
            '328'       REAL,
            '334'       REAL,
            '337'       REAL,
            '338'       REAL,
            '341'       REAL,
            '342'       REAL,
            '343'       REAL,
            '401'       REAL,
            '404'       REAL,
            '405'       REAL,
            '406'       REAL,
            '410'       REAL,
            '415'       REAL,
            '417'       REAL,
            '418'       REAL,
            '421'       REAL,
            '430'       REAL,
            '431'       REAL,
            '432'       REAL,
            '435'       REAL,
            '454'       REAL,
            '501'       REAL,
            '502'       REAL,
            '503'       REAL,
            '504'       REAL,
            '505'       REAL,
            '506'       REAL,
            '507'       REAL,
            '508'       REAL,
            '509'       REAL,
            '510'       REAL,
            '511'       REAL,
            '512'       REAL,
            '513'       REAL,
            '514'       REAL,
            '515'       REAL,
            '516'       REAL,
            '517'       REAL,
            '518'       REAL,
            '521'       REAL,
            '573'       REAL,
            '578'       REAL,
            '601'       REAL,
            '605'       REAL,
            '606'       REAL,
            '607'       REAL,
            '608'       REAL,
            '609'       REAL,
            '610'       REAL,
            '611'       REAL,
            '612'       REAL,
            '613'       REAL,
            '614'       REAL,
            '615'       REAL,
            '617'       REAL,
            '618'       REAL,
            '619'       REAL,
            '620'       REAL,
            '621'       REAL,
            '624'       REAL,
            '625'       REAL,
            '626'       REAL,
            '627'       REAL,
            '628'       REAL,
            '629'       REAL,
            '630'       REAL,
            '631'       REAL,
            '636'       REAL,
            '638'       REAL,
            '639'       REAL,
            '641'       REAL,
            '645'       REAL,
            '646'       REAL,
            '652'       REAL,
            '653'       REAL,
            '654'       REAL,
            '662'       REAL,
            '663'       REAL,
            '664'       REAL,
            '665'       REAL,
            '666'       REAL,
            '669'       REAL,
            '670'       REAL,
            '671'       REAL,
            '672'       REAL,
            '673'       REAL,
            '674'       REAL,
            '675'       REAL,
            '676'       REAL,
            '685'       REAL,
            '687'       REAL,
            '689'       REAL,
            '693'       REAL,
            '696'       REAL,
            '697'       REAL,
            '710'       REAL,
            '711'       REAL,
            '712'       REAL,
            '713'       REAL,
            '714'       REAL,
            '715'       REAL,
            '716'       REAL,
            '731'       REAL,
            '734'       REAL,
            '735'       REAL,
            '736'       REAL,
            '737'       REAL,
            '738'       REAL,
            '740'       REAL,
            '741'       REAL,
            '742'       REAL,
            '743'       REAL,
            '745'       REAL,
            '749'       REAL,
            '750'       REAL,
            '751'       REAL,
            '752'       REAL,
            '753'       REAL,
            '758'       REAL,
            '759'       REAL,
            '762'       REAL,
            '770'       REAL,
            '773'       REAL,
            '785'       REAL,
            '786'       REAL,
            '788'       REAL,
            '789'       REAL,
            '794'       REAL,
            '851'       REAL,
            '853'       REAL,
            '855'       REAL,
            '856'       REAL,
            '857'       REAL,
            '858'       REAL
        );
    '''
    create_logs_table = '''
        CREATE TABLE `Logs` (
            `UserId`    INTEGER NOT NULL,
            `ndbno`     INTEGER NOT NULL,
            `Date`      INTEGER NOT NULL
        );
    '''

    cur.execute(drop_users)
    cur.execute(drop_logs)
    cur.execute(drop_foods)
    cur.execute(create_users_table)
    cur.execute(create_logs_table)
    cur.execute(create_foods_table)
    conn.commit()
    conn.close()

def connect_db():
    try:
        conn = sqlite3.connect('food.db')
        return conn
    except Exception as e:
        return e

def save_food(data):
    '''
    DESCRIP: saves data from the data to the db file
    RETURNS: the id of the last entree
    REQUIRS: dictionary with food's nutrition
    MODIFIS: db table 'Foods'
    '''
    conn = connect_db()
    cur = conn.cursor()

    ids = list(data.keys())
    first_cols   = [data["ndbno"], data["name"], data["health_index"]]
    nutri_values    = [data[id]['value'] for id in ids if (id not in ids[-4:])]
    insertion       = first_cols + nutri_values
    # this will make ?,?,?...as many as provided
    value_markers = ','.join(['?']*len(insertion))
    
    sql_insert = ''' 
        INSERT INTO "Foods"
        VALUES({}) '''.format(value_markers)
    cur.execute(sql_insert, insertion)

    conn.commit()
    conn.close()

    return cur.lastrowid

def log_food(data, user_id):
    '''
    DESCRIP: logs food to the database for user_id
    RETURNS: nothing
    REQUIRS: nutri_data dictionary, valid user_id
    MODIFIS: db table 'Logs'
    '''

    # TODO: get a way to get a USERName from ID

    # 1. Check if food item already in db
    ndbno = data["ndbno"]
    querry = '''
        SELECT ndbno FROM Foods 
        WHERE ndbno={id}
        '''.format(id=ndbno)

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(querry)

    # db will return None if id doens't exist
    nbdno_exists = cur.fetchone()

    # if ndbno not in db already - add it
    if not nbdno_exists: 
        save_food(data)


    # 2. Logging the food item to the Logs table
    insertion = (user_id, ndbno)
    sql_insert = ''' 
        INSERT INTO "Logs"
        VALUES(?,?,date('now')) '''

    cur.execute(sql_insert, insertion)
    conn.commit()
    conn.close()

def create_user(user_name, gender, age, password):
    '''
    DESCRIP: creates user with the parameters
    RETURNS: nothing
    REQUIRS: name: str, gender: M or F, age: int, password: str
    MODIFIS: db table 'Users'
    '''
    if gender.lower() in ['male','mal','macho','ma','m','manlike','man','manly','boy','musculan','b']:
        gender = "M"
    else:
        gender = "F"

    conn = connect_db()
    cur = conn.cursor()
    insertion = (None, user_name, gender, age, password)
    sql_insert = ''' 
        INSERT INTO "Users"
        VALUES(?,?,?,?,?)'''
    cur.execute(sql_insert, insertion)
    conn.commit()
    conn.close()

def get_user_id(user_name):
    querry = '''
        SELECT UserId FROM Users
        WHERE Name='{}'
        '''.format(user_name)

    conn    = connect_db()
    cur     = conn.cursor()
    user_id = cur.execute(querry).fetchone()
    conn.close()
    return user_id[0]

def fetch_password(user_name):
    password_q = ''' 
        SELECT Password
        FROM Users as u
        WHERE Name = "{}" 
        LIMIT 1'''.format(user_name)

    conn    = connect_db()
    cur     = conn.execute(password_q).fetchone()
    conn.close()
    return cur

def fetch_nutrient(user_id, nutrients = ['Index'], date = False):
    # returns health index by default
    # name    = data['name'].split(" ")[0].replace(",","")
    # kcal    = data['kcal']

    # kcal    = data['208']['value'] if data['208']['value'] else 0.101
    # carbs   = data['205']['value']
    # fiber   = data['291']['value']
    # sugar   = data['269']['value']
    # sat_f   = data['606']['value']
    # trans_f = data['605']['value']
    # pol_f   = data['646']['value']
    # mon_f   = data['645']['value']
    # vit_c   = data['401']['value']
    # vit_a   = data['318']['value']
    # vit_k   = data['430']['value']
    # vit_d   = data['324']['value']
    # sodium  = data['307']['value']

        # SELECT f.'269'
        # FROM Logs as l
        # JOIN Foods as f
        #     ON l.ndbno = f.ndbno
        # WHERE UserId = '5'

    select_list = []
    select_string = ""
    for nutrient in nutrients:
        select_string += "f.'{}',".format(nutrient)

    password_q = ''' 
        SELECT {}, date
        FROM Logs as l
        JOIN Foods as f
            ON l.ndbno = f.ndbno
        WHERE UserId = "{}"
        '''.format(select_string[:-1],user_id)

    conn    = connect_db()
    cur     = conn.execute(password_q).fetchall()
    conn.close()
    return cur


if __name__=="__main__":
    # MAIN:
    # create_db()

    # sample data to play with  
    data = {'203': {'name': 'Protein', 'unit': 'g', 'value': 5.38},
     '204': {'name': 'Total lipid (fat)', 'unit': 'g', 'value': 5.38},
     '205': {'name': 'Carbohydrate, by difference', 'unit': 'g', 'value': 17.29},
     '207': {'name': ' ', 'unit': 'None', 'value': 0},
     '208': {'name': 'Energy', 'unit': 'kcal', 'value': 138.0},
     '209': {'name': ' ', 'unit': 'None', 'value': 0},
     '210': {'name': ' ', 'unit': 'None', 'value': 0},
     '211': {'name': ' ', 'unit': 'None', 'value': 0},
     '212': {'name': ' ', 'unit': 'None', 'value': 0},
     '213': {'name': ' ', 'unit': 'None', 'value': 0},
     '214': {'name': ' ', 'unit': 'None', 'value': 0},
     '221': {'name': ' ', 'unit': 'None', 'value': 0},
     '255': {'name': 'Water', 'unit': 'g', 'value': 71.1},
     '257': {'name': ' ', 'unit': 'None', 'value': 0},
     '262': {'name': 'Caffeine', 'unit': 'mg', 'value': 0.0},
     '263': {'name': ' ', 'unit': 'None', 'value': 0},
     '268': {'name': ' ', 'unit': 'None', 'value': 0},
     '269': {'name': 'Sugars, total', 'unit': 'g', 'value': 8.46},
     '287': {'name': ' ', 'unit': 'None', 'value': 0},
     '291': {'name': 'Fiber, total dietary', 'unit': 'g', 'value': 1.2},
     '301': {'name': 'Calcium, Ca', 'unit': 'mg', 'value': 135.0},
     '303': {'name': 'Iron, Fe', 'unit': 'mg', 'value': 1.73},
     '304': {'name': 'Magnesium, Mg', 'unit': 'mg', 'value': 38.0},
     '305': {'name': 'Phosphorus, P', 'unit': 'mg', 'value': 115.0},
     '306': {'name': 'Potassium, K', 'unit': 'mg', 'value': 138.0},
     '307': {'name': 'Sodium, Na', 'unit': 'mg', 'value': 77.0},
     '309': {'name': 'Zinc, Zn', 'unit': 'mg', 'value': 1.73},
     '312': {'name': ' ', 'unit': 'None', 'value': 0},
     '313': {'name': ' ', 'unit': 'None', 'value': 0},
     '315': {'name': ' ', 'unit': 'None', 'value': 0},
     '317': {'name': ' ', 'unit': 'None', 'value': 0},
     '318': {'name': 'Vitamin A, IU', 'unit': 'IU', 'value': 480.0},
     '319': {'name': ' ', 'unit': 'None', 'value': 0},
     '320': {'name': 'Vitamin A, RAE', 'unit': 'µg', 'value': 84.0},
     '321': {'name': ' ', 'unit': 'None', 'value': 0},
     '322': {'name': ' ', 'unit': 'None', 'value': 0},
     '323': {'name': 'Vitamin E (alpha-tocopherol)', 'unit': 'mg', 'value': 5.19},
     '324': {'name': 'Vitamin D', 'unit': 'IU', 'value': 92.0},
     '325': {'name': ' ', 'unit': 'None', 'value': 0},
     '326': {'name': ' ', 'unit': 'None', 'value': 0},
     '328': {'name': 'Vitamin D (D2 + D3)', 'unit': 'µg', 'value': 2.3},
     '334': {'name': ' ', 'unit': 'None', 'value': 0},
     '337': {'name': ' ', 'unit': 'None', 'value': 0},
     '338': {'name': ' ', 'unit': 'None', 'value': 0},
     '341': {'name': ' ', 'unit': 'None', 'value': 0},
     '342': {'name': ' ', 'unit': 'None', 'value': 0},
     '343': {'name': ' ', 'unit': 'None', 'value': 0},
     '401': {'name': 'Vitamin C, total ascorbic acid', 'unit': 'mg', 'value': 23.1},
     '404': {'name': 'Thiamin', 'unit': 'mg', 'value': 0.144},
     '405': {'name': 'Riboflavin', 'unit': 'mg', 'value': 0.163},
     '406': {'name': 'Niacin', 'unit': 'mg', 'value': 1.537},
     '410': {'name': ' ', 'unit': 'None', 'value': 0},
     '415': {'name': 'Vitamin B-6', 'unit': 'mg', 'value': 0.269},
     '417': {'name': ' ', 'unit': 'None', 'value': 0},
     '418': {'name': 'Vitamin B-12', 'unit': 'µg', 'value': 0.81},
     '421': {'name': ' ', 'unit': 'None', 'value': 0},
     '430': {'name': 'Vitamin K (phylloquinone)', 'unit': 'µg', 'value': 12.3},
     '431': {'name': ' ', 'unit': 'None', 'value': 0},
     '432': {'name': ' ', 'unit': 'None', 'value': 0},
     '435': {'name': 'Folate, DFE', 'unit': 'µg', 'value': 65.0},
     '454': {'name': ' ', 'unit': 'None', 'value': 0},
     '501': {'name': ' ', 'unit': 'None', 'value': 0},
     '502': {'name': ' ', 'unit': 'None', 'value': 0},
     '503': {'name': ' ', 'unit': 'None', 'value': 0},
     '504': {'name': ' ', 'unit': 'None', 'value': 0},
     '505': {'name': ' ', 'unit': 'None', 'value': 0},
     '506': {'name': ' ', 'unit': 'None', 'value': 0},
     '507': {'name': ' ', 'unit': 'None', 'value': 0},
     '508': {'name': ' ', 'unit': 'None', 'value': 0},
     '509': {'name': ' ', 'unit': 'None', 'value': 0},
     '510': {'name': ' ', 'unit': 'None', 'value': 0},
     '511': {'name': ' ', 'unit': 'None', 'value': 0},
     '512': {'name': ' ', 'unit': 'None', 'value': 0},
     '513': {'name': ' ', 'unit': 'None', 'value': 0},
     '514': {'name': ' ', 'unit': 'None', 'value': 0},
     '515': {'name': ' ', 'unit': 'None', 'value': 0},
     '516': {'name': ' ', 'unit': 'None', 'value': 0},
     '517': {'name': ' ', 'unit': 'None', 'value': 0},
     '518': {'name': ' ', 'unit': 'None', 'value': 0},
     '521': {'name': ' ', 'unit': 'None', 'value': 0},
     '573': {'name': ' ', 'unit': 'None', 'value': 0},
     '578': {'name': ' ', 'unit': 'None', 'value': 0},
     '601': {'name': 'Cholesterol', 'unit': 'mg', 'value': 4.0},
     '605': {'name': 'Fatty acids, total trans', 'unit': 'g', 'value': 0.0},
     '606': {'name': 'Fatty acids, total saturated', 'unit': 'g', 'value': 0.42},
     '607': {'name': ' ', 'unit': 'None', 'value': 0},
     '608': {'name': ' ', 'unit': 'None', 'value': 0},
     '609': {'name': ' ', 'unit': 'None', 'value': 0},
     '610': {'name': ' ', 'unit': 'None', 'value': 0},
     '611': {'name': ' ', 'unit': 'None', 'value': 0},
     '612': {'name': ' ', 'unit': 'None', 'value': 0},
     '613': {'name': ' ', 'unit': 'None', 'value': 0},
     '614': {'name': ' ', 'unit': 'None', 'value': 0},
     '615': {'name': ' ', 'unit': 'None', 'value': 0},
     '617': {'name': ' ', 'unit': 'None', 'value': 0},
     '618': {'name': ' ', 'unit': 'None', 'value': 0},
     '619': {'name': ' ', 'unit': 'None', 'value': 0},
     '620': {'name': ' ', 'unit': 'None', 'value': 0},
     '621': {'name': ' ', 'unit': 'None', 'value': 0},
     '624': {'name': ' ', 'unit': 'None', 'value': 0},
     '625': {'name': ' ', 'unit': 'None', 'value': 0},
     '626': {'name': ' ', 'unit': 'None', 'value': 0},
     '627': {'name': ' ', 'unit': 'None', 'value': 0},
     '628': {'name': ' ', 'unit': 'None', 'value': 0},
     '629': {'name': ' ', 'unit': 'None', 'value': 0},
     '630': {'name': ' ', 'unit': 'None', 'value': 0},
     '631': {'name': ' ', 'unit': 'None', 'value': 0},
     '636': {'name': ' ', 'unit': 'None', 'value': 0},
     '638': {'name': ' ', 'unit': 'None', 'value': 0},
     '639': {'name': ' ', 'unit': 'None', 'value': 0},
     '641': {'name': ' ', 'unit': 'None', 'value': 0},
     '645': {'name': 'Fatty acids, total monounsaturated',
             'unit': 'g',
             'value': 2.551},
     '646': {'name': 'Fatty acids, total polyunsaturated',
             'unit': 'g',
             'value': 0.122},
     '652': {'name': ' ', 'unit': 'None', 'value': 0},
     '653': {'name': ' ', 'unit': 'None', 'value': 0},
     '654': {'name': ' ', 'unit': 'None', 'value': 0},
     '662': {'name': ' ', 'unit': 'None', 'value': 0},
     '663': {'name': ' ', 'unit': 'None', 'value': 0},
     '664': {'name': ' ', 'unit': 'None', 'value': 0},
     '665': {'name': ' ', 'unit': 'None', 'value': 0},
     '666': {'name': ' ', 'unit': 'None', 'value': 0},
     '669': {'name': ' ', 'unit': 'None', 'value': 0},
     '670': {'name': ' ', 'unit': 'None', 'value': 0},
     '671': {'name': ' ', 'unit': 'None', 'value': 0},
     '672': {'name': ' ', 'unit': 'None', 'value': 0},
     '673': {'name': ' ', 'unit': 'None', 'value': 0},
     '674': {'name': ' ', 'unit': 'None', 'value': 0},
     '675': {'name': ' ', 'unit': 'None', 'value': 0},
     '676': {'name': ' ', 'unit': 'None', 'value': 0},
     '685': {'name': ' ', 'unit': 'None', 'value': 0},
     '687': {'name': ' ', 'unit': 'None', 'value': 0},
     '689': {'name': ' ', 'unit': 'None', 'value': 0},
     '693': {'name': ' ', 'unit': 'None', 'value': 0},
     '696': {'name': ' ', 'unit': 'None', 'value': 0},
     '697': {'name': ' ', 'unit': 'None', 'value': 0},
     '710': {'name': ' ', 'unit': 'None', 'value': 0},
     '711': {'name': ' ', 'unit': 'None', 'value': 0},
     '712': {'name': ' ', 'unit': 'None', 'value': 0},
     '713': {'name': ' ', 'unit': 'None', 'value': 0},
     '714': {'name': ' ', 'unit': 'None', 'value': 0},
     '715': {'name': ' ', 'unit': 'None', 'value': 0},
     '716': {'name': ' ', 'unit': 'None', 'value': 0},
     '731': {'name': ' ', 'unit': 'None', 'value': 0},
     '734': {'name': ' ', 'unit': 'None', 'value': 0},
     '735': {'name': ' ', 'unit': 'None', 'value': 0},
     '736': {'name': ' ', 'unit': 'None', 'value': 0},
     '737': {'name': ' ', 'unit': 'None', 'value': 0},
     '738': {'name': ' ', 'unit': 'None', 'value': 0},
     '740': {'name': ' ', 'unit': 'None', 'value': 0},
     '741': {'name': ' ', 'unit': 'None', 'value': 0},
     '742': {'name': ' ', 'unit': 'None', 'value': 0},
     '743': {'name': ' ', 'unit': 'None', 'value': 0},
     '745': {'name': ' ', 'unit': 'None', 'value': 0},
     '749': {'name': ' ', 'unit': 'None', 'value': 0},
     '750': {'name': ' ', 'unit': 'None', 'value': 0},
     '751': {'name': ' ', 'unit': 'None', 'value': 0},
     '752': {'name': ' ', 'unit': 'None', 'value': 0},
     '753': {'name': ' ', 'unit': 'None', 'value': 0},
     '758': {'name': ' ', 'unit': 'None', 'value': 0},
     '759': {'name': ' ', 'unit': 'None', 'value': 0},
     '762': {'name': ' ', 'unit': 'None', 'value': 0},
     '770': {'name': ' ', 'unit': 'None', 'value': 0},
     '773': {'name': ' ', 'unit': 'None', 'value': 0},
     '785': {'name': ' ', 'unit': 'None', 'value': 0},
     '786': {'name': ' ', 'unit': 'None', 'value': 0},
     '788': {'name': ' ', 'unit': 'None', 'value': 0},
     '789': {'name': ' ', 'unit': 'None', 'value': 0},
     '794': {'name': ' ', 'unit': 'None', 'value': 0},
     '851': {'name': ' ', 'unit': 'None', 'value': 0},
     '853': {'name': ' ', 'unit': 'None', 'value': 0},
     '855': {'name': ' ', 'unit': 'None', 'value': 0},
     '856': {'name': ' ', 'unit': 'None', 'value': 0},
     '857': {'name': ' ', 'unit': 'None', 'value': 0},
     '858': {'name': ' ', 'unit': 'None', 'value': 0},
     'kcal': 138.0,
     'name': 'Beverages, NESTLE, Boost plus, nutritional drink, ready-to-drink',
     'ndbno': '14041'}

    conn = connect_db()
    # create_db()
    create_user('Vanya', 'M', 24, 'SI206')
    # log_food(data,17)
