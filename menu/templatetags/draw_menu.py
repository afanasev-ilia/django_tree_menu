from typing import Any, Dict, List

from django import template
from django.template.context import RequestContext
from django.db.models.query import QuerySet
from django.utils.safestring import SafeText

from menu.models import ItemMenu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(
    context: RequestContext,
    menu: SafeText,
) -> Dict[str, List[Dict[str, Any]]]:
    """Основная логика отображения меню."""
    items = ItemMenu.objects.filter(menu__title=menu)
    items_values = items.values()
    main_item = [item for item in items_values.filter(parent=None)]
    try:
        active_item = items.get(id=int(context['request'].GET[menu]))
        parent_items_id_list = get_parent_items(active_item, main_item)
        for item in main_item:
            if item['id'] in parent_items_id_list:
                item['child_items'] = get_child_items(
                    items_values,
                    item['id'],
                    parent_items_id_list,
                )
        result_dict = {'items': main_item, 'menu': menu}
    except Exception:
        result_dict = {'items': main_item, 'menu': menu}
    return result_dict


def get_child_items(
    items_values: QuerySet,
    current_item_id: int,
    neighbors_items_id_list: List[int],
) -> List[Dict]:
    """Получение списка id первого уровня вложенности под активным пунктом."""
    item_list = [
        item for item in items_values.filter(parent_id=current_item_id)
    ]
    for item in item_list:
        if item['id'] in neighbors_items_id_list:
            item['child_items'] = get_child_items(
                items_values, item['id'], neighbors_items_id_list
            )
    return item_list


def get_parent_items(
    active_item: ItemMenu,
    main_item: List[Dict],
) -> List[int]:
    """Получение списка id родительских пунктов."""
    parent_items_id_list = []
    while active_item:
        parent_items_id_list.append(active_item.id)
        active_item = active_item.parent
    if not parent_items_id_list:
        for item in main_item:
            if item['id'] == active_item.id:
                parent_items_id_list.append(active_item.id)
    return parent_items_id_list
