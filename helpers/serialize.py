def serializeData(originalList: list[dict]) -> set[str]:
    serialized_set = set()
    for item in originalList:
        serialized_set.add(f'{item["properties"]["Name"]["title"][0]["text"]["content"]}--{item["properties"]["ID"]["number"]}')
    return serialized_set