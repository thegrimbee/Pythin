def clear_yard(pythin):
    items = pythin.get_items()
    item_indices = {
        "rat": [],
        "tiger": []
    }
    count = 0
    for i in range(len(items)):
        item_indices[items[i]].append(i)
    while (count < len(items)):
        if (len(item_indices["tiger"]) > 0):
            pythin.eat(item_indices["tiger"][0])
            count += 1
            item_indices["tiger"].pop(0)
        while (len(item_indices["rat"]) > 0 and not pythin.is_full()):
            pythin.eat(item_indices["rat"][0])
            count += 1
            item_indices["rat"].pop(0)
        pythin.swallow()