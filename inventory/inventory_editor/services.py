from django.core.serializers import serialize
from inventory_editor.models import Item
import json


def get_all_items():
    items = Item.objects.all()
    serialized_items = serialize('json', items)
    serialized_items = json.loads(serialized_items)
    return serialized_items


def add_new_item(data):
    item_decoded = data.body.decode('utf-8')
    item = json.loads(item_decoded)
    new_item = Item(name = item['name'], price = item['price'], quantity = item['quantity'], description = item['description'])
    new_item.save()

def get_items_by_name(name):
    items = Item.objects.filter(name__icontains=name)
    serialized_items = serialize('json', items)
    serialized_items = json.loads(serialized_items)
    return serialized_items


def get_items_by_desc(desc):
    items = Item.objects.filter(description__icontains=desc)
    serialized_items = serialize('json', items)
    serialized_items = json.loads(serialized_items)
    return serialized_items


def update_item(data):
    data_decoded = data.body.decode('utf-8')
    data = json.loads(data_decoded)
    item = Item.objects.get(id=data['id'])
    item.price = data['price']
    item.quantity = data['quantity']
    item.save()


def get_items_by_field(field, value):
    if(field == 'name'):
        return get_items_by_name(value) 
    if(field == 'desc'):
        return get_items_by_desc(value)


