def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """

    roles_tree_list = []

    for element_categoryIdsSorted in mapping["categoryIdsSorted"]:
        category_dict = dict()
        category_dict["id"] = "category-" + mapping["categories"][element_categoryIdsSorted]["id"]
        category_dict["text"] = mapping["categories"][element_categoryIdsSorted]["name"]

        roles = []
        for role_id in mapping["categories"][element_categoryIdsSorted]["roleIds"]:
            roles.append({"id": mapping["roles"][role_id]["id"], "text": mapping["roles"][role_id]["name"]})

        category_dict["items"] = roles

        roles_tree_list.append(category_dict)

    return {"categories": roles_tree_list}
