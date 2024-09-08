from pymongo import MongoClient

client = MongoClient("mongodb://root:root@localhost:27017/")
db = client['cats_db']
collection = db['cats']



def get_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)


def get_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")



def add_cat(name, age, features):
    new_cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(new_cat)
    print(f"Новий кіт доданий з ID: {result.inserted_id}")



def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота {name} оновлено до {new_age}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")



def add_cat_feature(name, new_feature):
    result = collection.update_one(
        {"name": name}, {"$addToSet": {"features": new_feature}})
    if result.matched_count > 0:
        print(f"Характеристика '{new_feature}' додана до кота {name}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")



def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям {name} видалений.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")



def delete_all_cats():
    result = collection.delete_many({})
    print(f"Всі коти видалені. Видалено записів: {result.deleted_count}")


if __name__ == "__main__":
    
    add_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    add_cat("murzik", 5, ["любит рибу", "чорний", "агресивний"])

    print("Всі коти:")
    get_all_cats()

    print("\nІнформація про кота з ім'ям barsik:")
    get_cat_by_name("barsik")

    update_cat_age("barsik", 4)

    add_cat_feature("murzik", "любить спати на дивані")

    delete_cat_by_name("murzik")

    delete_all_cats()
