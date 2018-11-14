from db import get_weeks_table, get_templates_table, chris_uuid, erin_uuid
from tinydb import Query
import uuid
import datetime

def get(week_start):
    weeks_table = get_weeks_table()
    
    week_query = Query()
    week = weeks_table.get(week_query.start_date == week_start)
    
    if not week:
        templates_table = get_templates_table()
        
        templates_query = Query()
        new_week = templates_table.get(templates_query.owner == chris_uuid)
        
        print(new_week)
        
        new_week['from_template'] = new_week['id']
        new_week['id'] = uuid.uuid4().hex
        new_week['sub'] = erin_uuid
        new_week['start_date'] = week_start
        new_week['date_created'] = datetime.datetime.utcnow().isoformat()
        new_week['date_updated'] = datetime.datetime.utcnow().isoformat()
        
        weeks_table.insert(new_week)
        
        week = new_week
    
    return week

def update(week):
    table = get_weeks_table()
    
    week['date_updated'] = datetime.datetime.utcnow().isoformat()
    
    week_query = Query()
    table.update(week, week_query.id == week['id'])
    
    return week