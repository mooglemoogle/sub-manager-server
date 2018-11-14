from tinydb import TinyDB, Query
import uuid
import datetime

db = None
users_table = None
templates_table = None
weeks_table = None

chris_uuid = "0de529c6-397c-4575-b8c2-b2574335065f"
erin_uuid = "1c786393-4095-4441-bb88-85c0e31646fd"

default_template = {
    'id': uuid.uuid4().hex,
    'name': 'Main Template',
    'owner': chris_uuid,
    'date_created': datetime.datetime.utcnow().isoformat(),
    'date_updated': datetime.datetime.utcnow().isoformat(),
    'duties': [
        {
            'name': 'Sex',
            'description': 'Make a solid attempt at mutually pleasurable sex',
            'responsible_party': 'sub',
            'times_per_week': 1,
            'complete': []
        },
        {
            'name': 'Exercise',
            'description': 'Take a walk with Finn',
            'responsible_party': 'sub',
            'requires_approval': False,
            'times_per_week': 3,
            'complete': []
        },
        {
            'name': 'Shower',
            'description': 'Take a shower',
            'responsible_party': 'sub',
            'requires_approval': False,
            'times_per_week': 3,
            'complete': []
        },
        {
            'name': 'Laundry',
            'description': 'Do a load of laundry (wash and dry)',
            'responsible_party': 'sub',
            'requires_approval': False,
            'times_per_week': 1,
            'complete': []
        },
        {
            'name': 'Home On Time',
            'description': 'Leave work by 5:30PM',
            'responsible_party': 'dom',
            'requires_approval': False,
            'times_per_week': 3,
            'complete': []
        }
    ],
    'rules': [
        {
            'name': "Cereal Milk",
            'description': "Don't let your master come across bowls of cereal milk",
            'responsible_party': 'sub',
            'times_violated': 0
        },
        {
            'name': "Mustache Length",
            'description': "Don't subject your sub to long, itchy mustache hair",
            'responsible_party': 'dom',
            'times_violated': 0
        }
    ]
}

def initialize():
    global db, users_table, templates_table, weeks_table
    db = TinyDB('subDb.json')
    users_table = db.table('users')
    templates_table = db.table('templates')
    weeks_table = db.table('weeks')
    
    chris_query = Query()
    chris = users_table.get(chris_query.id == chris_uuid)
    if not chris:
        users_table.insert({
            'id': chris_uuid,
            'role': 'dom',
            'owns': [
                erin_uuid
            ]
        })
    
    erin_query = Query()
    erin = users_table.get(erin_query.id == erin_uuid)
    if not erin:
        users_table.insert({
            'id': erin_uuid,
            'role': 'sub',
            'owned_by': chris_uuid
        })
    
    template_query = Query()
    template = templates_table.get(template_query.owner == chris_uuid)
    if not template:
        print("No Template Found")
        print(template)
        templates_table.insert(default_template)

def get_users_table():
    global users_table
    return users_table

def get_templates_table():
    global templates_table
    return templates_table

def get_weeks_table():
    global weeks_table
    return weeks_table