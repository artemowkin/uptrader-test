from django import template
from django.http.request import HttpRequest

from menutree.models import Menu, MenuItem


register = template.Library()


def _unpack_nodes(subitems: list[MenuItem], menu_items: list[MenuItem], item: MenuItem) -> list[MenuItem]:
    """Recursively unpack menu tree nodes. Algorithm:

    1. Iterate each nodes one by one
    2. If node is current - get node subitems (only 1 nesting level),
       extend subnodes and return
    3. If node is not current - get node subitems (recursively call),
       extend subnodes and if searching item in subitems - return extended subnodes
    
    :param subitems: Unpacking nodes list
    :param menu_items: All tree items list
    :param item: Current item
    :returns: Unpacked nodes
    """
    filtered_items = subitems.copy()
    for subitem in subitems:
        if subitem == item:
            filtered_items.extend([i for i in menu_items if i.root_item == subitem])
            return filtered_items
        else:
            new_subitems = [i for i in menu_items if i.root_item == subitem]
            res = _unpack_nodes(new_subitems, menu_items, item)
            filtered_items.extend(res)
            if item in res:
                return filtered_items

    return filtered_items


def _filter_items(menu_items: list[MenuItem], current_item: MenuItem | None = None) -> list[MenuItem]:
    """Filter (unpack) menu tree nodes
    
    :param menu_items: Filtering menu tree items
    :param current_item: Searching item (optional)
    :returns: Filtered list with menu tree nodes (only root nodes if no `current_item`)
    """
    root_items = [item for item in menu_items if not item.root_item]
    if not current_item: return root_items
    return _unpack_nodes(root_items, menu_items, current_item)


@register.inclusion_tag('menu_items.html')
def draw_menu(request: HttpRequest, menu: Menu):
    """Django template tag that draws tree menu
    
    :param request: Django http request object
    :param menu: Drawing menu instance
    """
    current_menu_get_param = request.GET.get(f"menu{menu.id}", '0')
    current = int(current_menu_get_param) if current_menu_get_param.isnumeric() else 0
    menu_items = list(menu.items.all())
    current_item = next((item for item in menu_items if item.id == current), None)
    menu_items = _filter_items(menu_items, current_item)
    return {'menu': menu, 'menu_items': menu_items, 'current': current}
